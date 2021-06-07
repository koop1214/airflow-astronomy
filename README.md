# Airflow Astronomy
Данный DAG служит для загрузки астрономический данных с [https://api.weatherapi.com](https://www.weatherapi.com/docs/#apis-astronomy) по дате и METAR-коду и вставки их таблицу:
```sql
CREATE TABLE IF NOT EXISTS astronomy
(
    metar             VARCHAR(4)  NOT NULL,
    date              DATE        NOT NULL,
    sunrise           TIME        NOT NULL,
    sunset            TIME        NOT NULL,
    moonrise          TIME        NOT NULL,
    moonset           TIME        NOT NULL,
    moon_phase        VARCHAR(30) NOT NULL,
    moon_illumination INT         NOT NULL,
    UNIQUE (metar, date)
);

```

## Инициализация окружения

Перед первым запуском Airflow требуется подготовить окружение: создать необходимые директории и файлы:

```shell
mkdir ./logs
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

Также необходимо проинициализироват базу данных: запустить миграции и создать акканут:

```shell
docker-compose up airflow-init
```

Для запуска всех служб:

```shell
docker-compose up -d
```
          
## Web Apps

* Airflow Webserver: http://localhost:8080. Дефолтный логин и пароль - `airflow`.
* Flower: http://localhost:5555

## Connections
Для корректной работы необходимо создать соединения:
* postgres_default - типа postgres
* weather_api_conn_id - типа http с API Key от https://www.weatherapi.com/ в качестве пароля
