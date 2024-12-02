import snowflake.connector

class SnowflakeConnector:
    def __init__(self,accountname,username,password,schemaname,dbname,warehousename,rolename):
        self.accountname = accountname
        self.username = username
        self.password =password
        self.schemaname = schemaname
        self.dbname = dbname
        self.warehousename = warehousename
        self.rolename = rolename
    def connect(self):
        self.connection = snowflake.connector.connect(
                                                        account = self.accountname,
                                                        user= self.username,
                                                        password = self.password,
                                                        schema = self.schemaname,
                                                        database = self.dbname,
                                                        warehouse = self.warehousename,
                                                        role = self.rolename

                                                     )
        self.cursor = self.connection.cursor()
    def excuateQueery(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def closeConnection(self):
        self.cursor.close()
        self.connection.close()

