docker build -t rpi/sensors .

docker run --rm -it -d --name sensors rpi/sensors

docker-compose up -d

