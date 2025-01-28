test-up:
	docker-compose -f docker-compose.test.yaml up -d
d-build:
	docker build -f Dockerfile.python -t datatalks-pipeline:0.0.1 .
d-run:
	docker run -it --network=postgresxpgadmin_default datatalks-pipeline:0.0.1 
d-ingest-green:
	python ingest_data.py --user youssef.l --password 9999 --host postgresDB --port 5432 --db ny_taxi --table_name green_taxi_trips --url https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz
d-ingest-zones:
	python ingest_data.py --user youssef.l --password 9999 --host postgresDB --port 5432 --db ny_taxi --table_name zones --url https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv