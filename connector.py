import pandas as pd
import mysql.connector
from mysql.connector import Error
def create_connection(host, database, user, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Connected to MySQL server")
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
    return connection

from sqlalchemy import create_engine
import pandas as pd

# Create a connection string (adjust this according to your MySQL setup)
# Format: dialect+driver://username:password@host:port/database
#connection_string = "mysql+mysqlconnector://root:ichcha@09@127.0.0.1:3306/sapreplica"

password = "ichcha%4009"  # Assuming your password is 'ichcha@09'

connection_string = f"mysql+mysqlconnector://root:{password}@127.0.0.1:3306/sapreplica"

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Now, you can use this engine with pandas to_sql method
TableList = ['BKPF','BSEC','BSEG','BSET', 'BVOR','BSIP','BSAD','BSID','BSAS','BSIS','BSAK','BSIK','PAYR','KNC1',
             'LFC1','LFA1','LFBK','LFB1','LFM1','LFB5','LFM2','KNA1', 'KNB1','KNVV','KNVD', 'KNVP','KNB5']
for table in TableList:
    print(table)
    try:
        df = pd.read_csv(f'{table}_data.csv')
        df.to_sql(name=table, con=engine, if_exists='append', index=False)
    except Exception as e:
        print(e)
        continue

# df = pd.read_csv('BKPF_Data.csv')
# df.to_sql(name='BKPF', con=engine, if_exists='replace', index=False)






'''
# dataframe
host = '127.0.0.1'
database = 'sapreplica'
user = 'root'
password = 'ichcha@09'
#connection = create_connection(host, database, user, password)

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user="root",
  password="ichcha@09",
    database="sapreplica"
)

print(mydb)
df = pd.read_csv('BKPF_Data.csv')
df.to_sql(name='BKPF', con=mydb, if_exists='append', index=False)

# MySQL database connection configuration

# Function to establish MySQL connection
# Function to copy DataFrame to MySQL table
# def copy_df_to_mysql(df, table_name, connection):
#     try:
#         # Copy DataFrame to MySQL table
#         df.to_sql(name=table_name, con=connection, if_exists='append', index=False)
#         print(f"DataFrame copied to MySQL table '{table_name}' successfully")
#     except Error as e:
#         print(f"Error copying DataFrame to MySQL table: {e}")
#
# # Connect to MySQL server
#
# # Specify table name in MySQL
# table_name = 'BKPF'

# # Copy DataFrame to MySQL table
# copy_df_to_mysql(df, table_name, connection)

# Close MySQL connection
"""
if connection:
    connection.close()
    print("MySQL connection closed")
"""
'''