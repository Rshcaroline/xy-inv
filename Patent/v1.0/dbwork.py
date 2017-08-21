from sqlalchemy import create_engine
import pandas as pd

sqlserver_url = "mssql+pymssql://shihan.ran:Caroline970505@192.168.66.12:1433"
engine = create_engine(sqlserver_url)

sql_query = '''
SELECT TOP (1000) 
      [InnerCode]
      ,[SecuCode]
      ,[ChiName]
      ,[ChiNameAbbr]    
  FROM [JYDB].[dbo].[SecuMain]
  '''

dic = pd.read_sql_query(sql_query, engine)

print dic