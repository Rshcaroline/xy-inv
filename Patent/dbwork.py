from sqlalchemy import create_engine
import pandas as pd

sqlserver_url = "mssql+pymssql://shihan.ran:Caroline970505@192.168.66.12:1433"
engine = create_engine(sqlserver_url)

sql_query = '''SELECT [InnerCode],[CompanyCode],[SecuCode] FROM [Public].[dbo].[QL_ASharesList]
  order by InnerCode '''

dic = pd.read_sql_query(sql_query, engine)

print dic