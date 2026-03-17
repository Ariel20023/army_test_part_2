import mysql.connector



class SqlConnector:
    def __init__(self,host,port,password,database):
        self.host = host
        self.port = port
        self.password = password
        self.database = database

        self.connection = mysql.connector.connect(
            host= self.host,
            port = self.port,
            password = self.password,
            database = self.database
            
            )
        
        self.cursor = self.connection.cursor()
