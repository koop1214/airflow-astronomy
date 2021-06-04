## Initializing Environment

Before starting Airflow for the first time, You need to prepare your  environment, i.e. create the necessary files, directories and initialize the database.

```shell
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

You need to run database migrations and create the first user account. To do it, run.

```shell
docker-compose up airflow-init
```

Now you can start all services:

```shell
docker-compose up
```
          
## Web Apps

`airflow-webserver` is available at http://localhost:8080

The default account has the login `airflow` and the password `airflow`.
                                 

[The flower app](https://flower.readthedocs.io/en/latest/) (for monitoring the environment) is available at http://localhost:5555
