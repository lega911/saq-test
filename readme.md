
# Build and run

docker build -t saq-test .
docker run --rm -v `pwd`:/app saq-test /app/run.sh
