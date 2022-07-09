# pyspark-venv

This is an experiment to test if it's possible to mix spark jobs with customized virtual environments.

## How to install

It's not really necessary to install top-level dependencies except for proper IDE support:
```
poetry install
```

Install customized virtual environment:
```
cd myvenv
poetry install
```

This is mounted as volume to all spark nodes.

## How to run

Start all containers:
```
docker-compose up
```

Jump into spark master node container:
```
docker-compose exec spark bash
```

Inside of container:
```
spark-submit /main.py
```

The output:
```
--- venv ----
+----------+---------+----------+
|first_name|last_name|instrument|
+----------+---------+----------+
|      John| Coltrane|       Sax|
|       Joe|     Pass|    Guitar|
|     Louis|Armstrong|   Trumpet|
+----------+---------+----------+
```
