import psycopg2
from psycopg2 import Error
from config import DBConfig
import logging
from backend.api.models import UserAccount
from uuid import UUID

class DatabaseManager:
    """
    A class to manage interactions with a PostgreSQL database.

    Attributes:
        dbname (str): The name of the database.
        user (str): The username for database authentication.
        password (str): The password for database authentication.
        host (str): The hostname of the database server.
        port (str): The port number to connect to the database.
        connection: The connection object to the database.
        cursor: The cursor object to execute SQL commands.
    """

    def __init__(self):
        """
        Initializes the DatabaseManager object by establishing a connection to the database.
        """
        dbconfig = DBConfig()
        self.dbname = dbconfig.db_name
        self.user = dbconfig.db_user
        self.password = dbconfig.db_password
        self.host = dbconfig.db_host_name
        self.port = dbconfig.db_port
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """
        Establishes a connection to the PostgreSQL database.
        """
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            logging.info("Connected to the database successfully.")
        except Error as e:
            logging.error(f"Error connecting to the database: {e}")

    def execute_query(self, query, params=None):
        """
        Executes a SQL query on the database.

        Args:
            query (str): The SQL query to be executed.
            params (tuple, optional): Parameters to be passed to the SQL query.

        Returns:
            list: The result of the query execution.
        """
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            logging.debug(f"Query executed successfully: {query}")
            return self.cursor.fetchall()
        except Error as e:
            logging.error(f"Error executing query: {e} - QueryString: {query}")

    def call_stored_procedure(self, procedure_name, params=None):
        """
        Calls a stored procedure in the database.

        Args:
            procedure_name (str): The name of the stored procedure to be called.
            params (dict): Dictionary of parameters to be passed to the stored procedure.
        """
        try:
            self.cursor.callproc(procedure_name, params)
            self.connection.commit()
            logging.debug(f"Stored procedure with name: {procedure_name} called successfully.")
        except Error as e:
            logging.error(f"Error calling stored procedure: {e}")

    def close_connection(self):
        """
        Closes the connection to the database.
        """
        if self.connection:
            self.cursor.close()
            self.connection.close()
            logging.info("Connection closed.")

    def get_user_accounts(self):
        """
        Retrieves all user accounts from the database.

        Returns:
            list: A list of dictionaries representing user accounts.
        """
        qstring = 'SELECT * from GetAccounts()'
        result = self.execute_query(query=qstring)
        accounts = []
        for row in result:
            account = dict(zip(UserAccount.model_fields.keys(), row))
            accounts.append(account)
        return accounts

    def get_user_account_by_id(self, user_guid: UUID):
        """
        Retrieves a user account from the database by its ID.

        Args:
            user_guid (UUID): The UUID of the user account to retrieve.

        Returns:
            dict: A dictionary representing the user account.
        """
        qstring = 'SELECT * FROM GetAccountById(%s) '
        result = self.execute_query(query=qstring, params=user_guid)

        if len(result) > 1:
            raise ValueError(f'Multiple accounts found with user guid: {user_guid}')
        else:
            account = dict(zip(UserAccount.model_fields.keys(), result[0]))
            return account
        
    def create_user_account(self, user:UserAccount): 
        qstring = 'CALL Create CreateAccount(%s,%s,%s,%s,%s)'
        self.call_stored_procedure(procedure_name='CreateAccount',params=(
            user.user_fname,
            user.user_lname,
            user.account_role_id, 
            user.is_active
        ))

# Example usage:
if __name__ == "__main__":
    logging.error("Don't do that yo")
