
import time
import os
import random
import asyncio
from saq import Queue

pid = os.getpid()
queue = Queue.from_url('redis://localhost')


async def rpc(ctx, *, d):
    print(f'  Worker #{pid}: request {d["id"]} ({d})')
    await asyncio.sleep(random.random() + 1)
    r = d['a'] + d['b']
    print(f'  Worker #{pid} response {d["id"]} ({r})')
    return {'id': d['id'], 'result': r, 'pid': pid}


time.sleep(random.random() * 0.1)
print(f'Worker #{pid} has started')

settings = {
    "queue":     queue,
    "functions": [rpc],
    "timers": {"sweep": 1},
    "concurrency": 20
}
