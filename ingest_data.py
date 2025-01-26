import pandas as pd 
from sqlalchemy import create_engine
import time 
import argparse

def main(args):
    engine = create_engine(url=f"postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}")

    df = (pd.read_parquet(args.url) if args.url.endswith('.parquet') 
            else pd.read_csv(args.url) if args.url.endswith('.csv') 
            else pd.read_csv(args.url, compression='gzip', low_memory=False) if args.url.endswith('.csv.gz') 
            else None
        )

    # schema = print(pd.io.sql.get_schema(df, name=args.table_name, con=engine))

    st = time.time()
    df.to_sql(name=args.table_name, con=engine, if_exists='replace', chunksize=100_000)

    et = time.time()
    print(f"Time to ingest data: {et - st} seconds")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--user", default='root')
    args.add_argument("--password", default='root')
    args.add_argument("--host", default='localhost')
    args.add_argument("--port", default=5432)
    args.add_argument("--db", default='ny_taxi')
    args.add_argument("--table_name", default='yellow_taxi_data')
    args.add_argument("--url", help="CSV file path")

    args = args.parse_args()

    main(args)