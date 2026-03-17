import mysql.connector



class SqlConnector:
    def __init__(self,host,port,user,password,database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        self.connection = mysql.connector.connect(
            host= self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
            
            )
        
        self.cursor = self.connection.cursor()
