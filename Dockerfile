FROM python:3.12.8

RUN pip install pandas sqlalchemy psycopg2 pyarrow 

WORKDIR /pipeline

COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "bash" ] 