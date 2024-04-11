import psycopg2
from psycopg2 import Error
from config import DBConfig
import logging
from api.models import UserAccount, ResponseTeam, ResponseTeamAccount, EventType, EventStatus, EventModel, EventTimelineNote
from psycopg2.errors import InvalidTextRepresentation

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
            cursor = self.connection.cursor()  # Create a new cursor
            cursor.execute(query, params)
            self.connection.commit()
            logging.debug(f"Query executed successfully: {query}")
            result = cursor.fetchall() if cursor.description else []  # Check for None result
            cursor.close()  # Close the cursor
            return result
        except Error as e:
            self.connection.rollback()  # Rollback transaction on error
            logging.error(f"Error executing query: {e} - QueryString: {query}")
            return []  # Return empty list to prevent subsequent errors

    def close_connection(self):
        """
        Closes the connection to the database.
        """
        if self.connection:
            self.cursor.close()
            self.connection.close()
            logging.info("Connection closed.")        

class Events(DatabaseManager): 
    def get_event_types(self):
        """
        Retrieves all event types from the database.

        Returns:
            list: A list of dictionaries representing event types.
        """
        qstring = 'SELECT * FROM GetAllEventTypes()'
        result = self.execute_query(query=qstring)
        event_types = []
        for row in result:
            event_type = dict(zip(EventType.model_fields.keys(), row))
            event_types.append(event_type)
        return event_types
    
    def get_event_type_by_id(self, type_id):
        """
        Retrieves an event type from the database by its ID.

        Args:
            type_id (int): The ID of the event type to retrieve.

        Returns:
            dict: A dictionary representing the event type.
        """
        qstring = 'SELECT * FROM GetEventTypeById(%s)'
        result = self.execute_query(query=qstring, params=(type_id,))
        event_type = {}
        for row in result:
            event_type = dict(zip(EventType.model_fields.keys(), row))
        return event_type

    def update_event_type_by_id(self, event_type_id: int, updated_information: EventType): 
        try: 
            logging.info(f'Updating Event Type with Id: {event_type_id}')
            qstring = 'CALL UpdateEventType(TypeId => %s,TypeName => %s,TypeDesc => %s)'
            result = self.execute_query(query=qstring, params=(event_type_id,
                                                            updated_information.event_type_name,
                                                            updated_information.event_type_description
                                                            )) 
            return result
        except InvalidTextRepresentation as err: 
            raise ValueError(f'Shit broke yo {err}')
        
    def get_event_status_by_id(self,event_status_id: int): 
        """
        Retrieves an event type from the database by its ID.

        Args:
            type_id (int): The ID of the event type to retrieve.

        Returns:
            dict: A dictionary representing the event type.
        """
        qstring = 'SELECT * FROM GetEventStatusById(StatusId => %s)'
        result = self.execute_query(query=qstring, params=(event_status_id,))
        event_type = {}
        for row in result:
            event_type = dict(zip(EventStatus.model_fields.keys(), row))
        return event_type

    def get_event_statuses(self): 
        """
        Retrieves an event type from the database by its ID.

        Args:
            type_id (int): The ID of the event type to retrieve.

        Returns:
            dict: A dictionary representing the event type.
        """
        qstring = 'SELECT * FROM GetAllEventStatuses(%s)'
        result = self.execute_query(query=qstring)
        event_type = {}
        for row in result:
            event_type = dict(zip(EventStatus.model_fields.keys(), row))
        return event_type

    def create_event(self, event:EventModel): 
        qstring = 'CALL CreateEvent (EventTypeParam=> %s, EventNameParam => %s, EventStatusIdParam=> %s, CommanderUserUUIDParam=> %s, EventSeverityIdParam => %s)'
        result = self.execute_query(query=qstring, params=(
            event.event_type_id,
            event.event_name,
            event.event_status_id,
            event.commander_user_uuid, 
            event.event_severity_id
        ))
        return result
    
    def get_event_by_id(self, event_uuid: str): 
        qstring =   'SELECT * FROM GetEventById(EventUUIDParam => %s)'
        result = self.execute_query(query=qstring, params=(event_uuid,))
        event = {}
        for row in result:
            event = dict(zip(EventModel.model_fields.keys(), row))
        return event
    
    def get_events(self): 
        qstring = 'SELECT * from GetAllEvents()'
        result = self.execute_query(query=qstring)
        events = []
        if result is not []: 
            for row in result: 
                events.append(dict(zip(EventModel.model_fields.keys(),row)))
            return events
        else: 
            return None
    
    
    def update_event(self,event_uuid, updated_information: EventModel): 
        qstring = """ 
                  CALL UpdateEvent(EventUUIDParam=> %s,EventTypeIdParam=> %s, EventNameParam => %s, EventStatusIdParam => %s, CommanderUserUUIDParam => %s, EventSeverityIdParam => %s )
                  """
        result = self.execute_query(qstring, params=(
            event_uuid,
            updated_information.event_type_id,
            updated_information.event_name,
            updated_information.event_status_id,
            updated_information.commander_user_uuid,
            updated_information.event_severity_id
        ))
        return result 
    
    def delete_event(self, event_uuid: str): 
        try: 
            logging.info(f'Deleting event with uuid: {event_uuid}')
            qstring = 'CALL DeleteEvent(EventUUIDParam => %s)'
            result = self.execute_query(qstring,params=(event_uuid,))
            return result
        except Exception as err: 
            logging.error(f'Unable to delete event with Id: {event_uuid} Error: {err}')
        

class EventTimeline(DatabaseManager): 

    def delete_event_timeline_note(self,timeline_note_uuid: str): 
        try:
            logging.info(f'Deleting timeline note: {timeline_note_uuid}')
            qstring = 'CALL DeleteEventTimelineNote(TimelineNoteUUIDParam => %s)'
            result = self.execute_query(query=qstring, params=(timeline_note_uuid,))  # Pass UUID as a tuple
            return result                
        except Exception as err:
                logging.error(f'Unable to delete timeline note: {err}')  
            
    def update_event_timeline_note (self,timeline_note_uuid: str, timeline_note: EventTimelineNote):
        try:
            logging.info(f'Updating timeline note: {timeline_note_uuid}')
            qstring = 'CALL UpdateEventTimelineNote(TimeLineNoteUUIDParam => %s, EntryNoteParam => %s)'
            result = self.execute_query(query=qstring, params=(timeline_note_uuid,timeline_note.entry_note))
            return result
        except Exception as err:
            logging.error(f'Unable to update Event Timeline note: {err}')

    def get_event_timeline_notes_by_timeline_note_uuid (self,timeline_uuid: str):
        try:
            logging.info(f'Getting Event Timeline Notes by Timeline Note UUID: {timeline_uuid}')
            qstring = 'SELECT * from GetEventTimelineNotesByTimelineUUID(TimelineUUIDParam => %s)'
            result = self.execute_query(query=qstring, params=(timeline_uuid))
            event_timeline_notes = []
            if result is []: 
                return None
            else: 
                for row in result:
                    event_timeline_note = dict(zip(EventTimelineNote.model_fields.keys(),row))
                return event_timeline_note
        except Exception as err:
            logging.error(f'Unable to update Event Timeline note: {err}')

    # Python formatted name of the function. Use 'Snake' case. Example 'function_name_here' 
    def function_name(self, argument_1: str, argument_2: str):
        # Begin the 'Try' block. If any errors happen in this block, it will go to the 'Except' blcok 
        try: 
            # Logging statement. This logs to the console what the command will do when it runs. 
            logging.info(f'Log goes here. Add the argument between the curly braces: {argument_1}')

            # Define the query string for the SQL function or stored procedure you will run. 
            qstring = 'CALL ProcedureName(ProcedureParameter1 => %s , ProcedureParameter2 => %s)'

            # Execute the sql query. This will run the command as it is written in the backend/sql/functions directory 
            # It will then store it in a variable called 'result' 
            # The library that is running the query will replace '%s' above with the Python argument that you define 
            # below
            result = self.execute_query(query=qstring,params=(argument_1, argument_2))

            # Return the result of the query 
            return result 
        # If something goes wrong with everything in the 'Try' block, store the error that is thrown
        # In a variable named 'err'. Log the error as it is raised. 
        except Exception as err: 
            logging.error(f'Error thrown in try block: {err}')


class Teams(DatabaseManager): 
     
    def get_teams(self):
        qstring = 'SELECT * from GetResponseTeams()'
        result = self.execute_query(query=qstring)
        teams = []
        for row in result:
            team = dict(zip(ResponseTeam.model_fields.keys(), row))
            teams.append(team)
        return teams


    def get_team_by_id(self, team_uuid: str):
        logging.info(f'Getting team with Id: {team_uuid}')
        qstring = 'SELECT * FROM GetResponseTeamById(%s)'
        result = self.execute_query(query=qstring, params=(team_uuid,))  
        return result


    def create_team(self, team:ResponseTeam): 
        qstring = 'CALL CreateResponseTeam (%s, %s)'
        result = self.execute_query(query=qstring, params=(
            team.response_team_name,
            team.response_team_description
        ))
        return result
    
    def delete_team_by_id(self, team_uuid: str):
        logging.info(f'Deleting team with Id: {team_uuid}')
        qstring = 'CALL DeleteResponseTeam(TeamId => %s)'
        result = self.execute_query(query=qstring, params=(team_uuid,))  # Pass UUID as a tuple
        return result

    def update_team_by_id(self, team_uuid: str, updated_information:ResponseTeam):
            try: 
                logging.info(f'Updating team with Id: {team_uuid}')
                qstring = 'CALL UpdateResponseTeam(TeamId => %s,TeamDesc => %s,ResponseTeamName => %s)'
                result = self.execute_query(query=qstring, params=(team_uuid,
                                                                updated_information.response_team_desc,
                                                                updated_information.response_team_name
                                                                ))  # Pass UUID as a tuple
                return result
            except InvalidTextRepresentation as err: 
                raise ValueError(f'Shit broke yo {err}')
                 
    def insert_team_user(self, team_uuid: str, user_uuid: str):
            try:
                logging.info(f'Inserting user with UUID: {user_uuid} into team with UUID: {team_uuid}')
                qstring = 'CALL InsertResponseTeamUser(TeamId => %s, UserUUID => %s)'
                result = self.execute_query(query=qstring, params=(team_uuid, user_uuid))
                return result
            except Exception as err:
                    logging.error(f'Unable to insert team user: {err}')
                        

    def delete_team_user(self, team_uuid: str, user_uuid: str):
            try:
                # This log should look more like "Deleting user: {user_uuid} from team: {team_uuid} "
                logging.info(f'Deleting user: {user_uuid} from team: {team_uuid}')
                qstring = 'CALL DeleteResponseTeamUser(TeamId => %s, Userid => %s)'
                result = self.execute_query(query=qstring, params=(team_uuid,user_uuid))  # Pass UUID as a tuple
                return result                
            except Exception as err:
                    logging.error(f'Unable to delete user from team: {err}')    

class Accounts(DatabaseManager): 
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

    def get_user_account_by_id(self, user_uuid: str):
        """
        Retrieves a user account from the database by its ID.

        Args:
            user_guid (UUID): The UUID of the user account to retrieve.

        Returns:
            dict: A dictionary representing the user account.
        """
        logging.info(f'Getting account with Id: {user_uuid}')
        qstring = 'SELECT * FROM GetAccountById(%s) '
        result = self.execute_query(query=qstring, params=(user_uuid,))  # Pass UUID as a tuple
        return result

        
    def create_user_account(self, user:UserAccount): 
        qstring = 'CALL CreateAccount (%s, %s, %s, %s )'
        result = self.execute_query(query=qstring,params=(
            user.user_fname,
            user.user_lname,
            user.account_role_id, 
            user.is_active
        ))
        return result
    
    def delete_user_account_by_id(self, user_uuid: str):
        """
        Retrieves a user account from the database by its ID.

        Args:
            user_guid (UUID): The UUID of the user account to retrieve.

        Returns:
            dict: A dictionary representing the user account.
        """
        logging.info(f'Deleting account with Id: {user_uuid}')
        qstring = 'CALL DeleteAccount(Id => %s)'
        result = self.execute_query(query=qstring, params=(user_uuid,))  # Pass UUID as a tuple
        return result
    
    
    def update_user_account_by_id(self, user_uuid: str, updated_information:UserAccount):
        """
        Updates a user account from the database by its ID.

        Args:
            user_uuid (UUID): The UUID of the user account to retrieve.
            user (UserAccount): The parameters to update for the user account

        Returns:
            dict: A dictionary representing the user account.

        # TODO: Fix error handling on this 
        """
        try: 
            logging.info(f'Updating account with Id: {user_uuid}')
            qstring = 'CALL UpdateAccount(Id => %s,FirstName => %s,LastName => %s,RoleId => %s,Active => %s)'
            result = self.execute_query(query=qstring, params=(user_uuid,
                                                            updated_information.user_fname,
                                                            updated_information.user_lname,
                                                            updated_information.account_role_id,
                                                            updated_information.is_active
                                                            ))  # Pass UUID as a tuple
            return result
        except InvalidTextRepresentation as err: 
            raise ValueError(f'Shit broke yo {err}')

# Example usage:
if __name__ == "__main__":
    logging.error("Don't do that yo")


# git add -A; git commit -m 'Add event timeline notes and event creation functions' ; git push 