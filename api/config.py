import os




class Config:
    def __init__ (self):
        self.mysql_host = os.getenv("MYSQL_HOST")
        self.mysql_port = os.getenv("MYSQL_PORT")
        self.mysql_password = os.getenv("MYSQL_ROOT_PASSWORD")
        self.mysql_database = os.getenv("MYSQL_DATABASE")
        