from fastapi import FastAPI
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import os




# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
mysql_url = os.getenv('MYSQL_URL')
user  = os.getenv('MYSQLUSER')
password = os.getenv('MYSQLPASSWORD')
host = os.getenv('MYSQLHOST')
port = os.getenv('MYSQLPORT')
database = os.getenv('MYSQLDATABASE')
port = os.getenv('MYSQLPORT')
config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database,
    'port': port,
}
print('---------------')
print(config)
print('-------------')

try:
    engine = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(f'Erro na conexão com o banco de dados 1:{str(err)}')
    print(err)
    print('-------------')
    engine.close()
print('-------------')


app = FastAPI()
@app.get("/")
async def root():
    df = ''
    try:
        engine = mysql.connector.connect(**config)
        df = pd.read_sql(f'SELECT * FROM cgh_fae WHERE id = {id}', con=engine)
        engine.close()
    except mysql.connector.Error as err:
        engine.close()
        return {'error': str(err)}
    return df.to_json()


@app.get("/consulta_id/{id}")
async def consulta_id(id: int):
    # try:
    #     engine = create_engine(mysql_url)
    #
    #     df = pd.read_sql(f'SELECT * FROM cgh_fae WHERE id = {id}', con=engine)
    #     return df.to_json()
    # except Exception as e:
    #     query = f'SELECT * FROM cgh_fae WHERE id = {id}'
    return {'error': e,'query': query}
