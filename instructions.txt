# Creatre Network for Postgres and PgAdmin to work together

docker network ls
docker network inspect ..
docker network rm ..

ntwrk=pg-network; docker network create $ntwrk

# Create Postgres Database
dir=ny_taxi_postgres_data; [ -d $dir ] && rm -rf $dir; mkdir $(dir); docker run -it -e POSTGRES_USER=youssef.l -e POSTGRES_PASSWORD=9999 -e POSTGRES_DB=ny_taxi -v $(pwd)/$(dir):/var/lib/postgresql/data -p 5432:5432 --network=$ntwrk --name=pgdb postgres:13

# Ingest Data
python ingest_data.py --user youssef.l --password 9999 --host postgresDB --port 5432 --db ny_taxi --table_name green_taxi_trips --url https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-01.parquet

# Connect to Postgres Database to see the data
- Using docker: docker exec -it pgdb psql -U youssef.l -d ny_taxi
- Using pgAdmin: http://localhost:8080 (login and set up server)
- Using pgcli: pgcli -h localhost -p (host port) -U (user) -d (db name)

# Create PgAdmin
docker run -it -e PGADMIN_DEFAULT_EMAIL="laouinayoussef1999@gmail.com" -e PGADMIN_DEFAULT_PASSWORD=9999 -p 8080:80 --network=$ntwrk --name=pgadmin dpage/pgadmin4

## Navigate to http://localhost:8080
- Login with youssef.l/9999
- Add New Server
    - Name: pgdb
    - Host: localhost
    - Port: 5432

# Usefull commands:

- 1. Check Ports in Use on the Host Machine:
    - sudo lsof -i -P -n
    	•	-i: Shows network files (including ports).
        •	-P: Shows port numbers instead of service names.
        •	-n: Avoids resolving hostnames, speeds up the output.

    - sudo netstat -tuln
    	•	-t: Shows TCP ports.
        •	-u: Shows UDP ports.
        •	-l: Shows listening ports.
        •	-n: Shows numerical addresses and ports.

2. Check Ports in Use by Docker Containers:
    - docker ps
    - docker port <container_name_or_id>
        •	To get detailed information about the port mappings for a specific container, e.g.:
            - docker port pgdb

Notes:
    - pgAdmin connection to postgres can be done in two ways:
        1. Setting Host name/service to db (service name)
        2. Setting Host name/service to psotgres (container name)
    - Services Ports on docker are always the same. What we change are ports on the host machine.
    