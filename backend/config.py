import os
from dotenv import load_dotenv 

class DBConfig:
    def __init__(self):
        load_dotenv() 
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_host_name = os.getenv('DB_HOST_NAME')
        self.db_port = os.getenv('DB_PORT')