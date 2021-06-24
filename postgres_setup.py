import psycopg2
import pandas as pd
import os
import sqlalchemy

engine = sqlalchemy.create_engine(
    'postgresql://rpzvmzry:aVau2gYj_xxQ4OIhJ3ye_50ZvgNA7K1q@batyr.db.elephantsql.com/rpzvmzry'
)

# setting up connection for elephant db
dbname = os.environ['PG_DB']
user = os.environ['PG_User']
password = os.environ['PG_Password']
host = os.environ['PG_Host']
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# creating the elephant db table for the song data
table = pd.read_csv('data/data_o_clean.csv')
table.set_index('Unnamed: 0', inplace=True)
table.to_sql('Spotify_Songs', engine, if_exists='replace')
