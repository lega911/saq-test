#!/bin/sh

echo Start Redis
/bin/redis-server > /dev/null 2>&1 &
sleep 1

cd /app
rm -f /tmp/logs
python3 -u -m saq worker.settings &
python3 -u -m saq worker.settings &
python3 -u -m saq worker.settings &

sleep 1

python3 -u ./client.py --stop &
python3 -u ./client.py &
python3 -u ./client.py &

sleep 120
