# Backend Python
Backend codé en python utilisant Flask


## Installation

1. Clone the project from GitHub
```shell
git clone https://github.com/Matribuk/backend_python.git
```
2. Build & Run project
```shell
docker-compose up --build -d
```
3. Execute curl request like this :
```shell
curl http://localhost:5001/
```
```shell
curl http://localhost:5001/tasks
```
```shell
curl -X DELETE http://localhost:5001/tasks/0
```
```shell
curl -X POST -H "Content-Type: application/json" -d '{"task": "Acheter du sel"}' http://localhost:5001/tasks
```
```shell
curl -X DELETE http://localhost:5001/clear_users
```

