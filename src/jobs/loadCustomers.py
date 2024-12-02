from src.utils.snowUtils import  SnowflakeConnector
accountname = "XXXXXXXXXXXX"
username = "XXXXXXXXXXXX"
password = "XXXXXXXXXXXX"
schemaname = "TPCH_SF1"
dbname = "SNOWFLAKE_SAMPLE_DATA"
warehousename = "COMPUTE_WH"
rolename = "SYSADMIN"

sf_connection_obj = SnowflakeConnector(accountname,username,password,schemaname,dbname,warehousename,rolename)

sf_connection_obj.connect()

query = "select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER limit 10"
result = sf_connection_obj.excuateQueery(query)
print(result)
sf_connection_obj.closeConnection()