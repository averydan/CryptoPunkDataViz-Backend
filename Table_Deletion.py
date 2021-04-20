import os

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Delete generated files

os.remove("Market_Data.csv")
os.remove("market_data.txt")

# Start a PostgreSQL database session

psqlCon = psycopg2.connect("dbname=CryptoPunks user=postgres password=Lizst_52")

psqlCon.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Open a database cursor

psqlCursor = psqlCon.cursor()

# Name of the tables to be deleted

tableName1 = "market_df"
tableName2 = "punks_df"
 
# Form the SQL statement - DROP TABLE

dropTableStmt1 = "DROP TABLE %s;"%tableName1
dropTableStmt2 = "DROP TABLE %s;"%tableName2
 
# Execute the drop table commands

psqlCursor.execute(dropTableStmt1)
psqlCursor.execute(dropTableStmt2)
 
# Free the resources

psqlCursor.close()

psqlCon.close()


