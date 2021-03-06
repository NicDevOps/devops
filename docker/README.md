# Basic docker commands and syntaxe examples
#
```console
                     _-----o----_
            /|__/|  /            |
            |_  _/ /              |
              | |_|          () __|
               |               |_
                |     %__%       /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
## Run docker using multiple parameters
#
#### -d for detatch mode (in background), named 'blue-app',
#### port mapped on host 38282 and container on 8080, 
#### -e for seting up environment variable 'APP_COLOR' to blue
#### on image 'kodekloud/simple-webapp'

```console
docker run -d --name blue-app -p 38282:8080 -e APP_COLOR=blue kodekloud/simple-webapp
```
## Deploy a mysql database using the mysql image and name it # mysql-db.
#
### Set the database password to use db_pass123. Lookup the mysql # image on Docker Hub and identify the correct environment # variable to use for setting the root password
#
```console
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 -d mysql 
```
# Build a docker image using 'Docker build' in current directory
```console
docker build -t webapp-color .
```
## Create a new network named wp-mysql-network using the bridge driver. Allocate subnet 182.18.0.1/24. Configure # Gateway 182.18.0.1
```console
docker network create --driver bridge --subnet 182.18.0.1/24 --gateway 182.18.0.1 wp-mysql-network

docker run -d --name mysql-db --network wp-mysql-network -e MYSQL_ROOT_PASSWORD=db_pass123 mysql:5.6

docker run -d --name webapp -p 38080 -e DB_Host=mysql-db --network wp-mysql-network kodekloud/simple-webapp-mysql
```
## Deploy mysql database using /opt/data on container, data persists in /var/lib/mysql

docker run -v /opt/data:/var/lib/mysql --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 -d mysql

# Use a volume with docker, for data to persists

## Create a volume : 
```console
docker volume create data_volume
```
## Run : 
```console
docker run -v data_volume:/var/lib/mysql mysql
```
## Run using '\' : 
```console
docker run \ --mount type=bind,source=data/mysql,target=/var/lib/mysql mysql
```
# Docker-compose
```console
version: "2"
services:
  db:
    image: postgres
    environment:
      - POSTGRES_PASSWORD=mysecretpassword
  wordpress:
    image: wordpress
    ports:
      - 8085:8085
    links:
      - "db"
```
# Docker for jupyter 
```console
docker run --rm -d -p 8888:8888 -v "$PWD":/home/jovyan/work jupyter/scipy-notebook:latest
```
