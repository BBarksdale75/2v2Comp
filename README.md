# TrackWolf

## Overview

This web application is being developed by Brandon and Tony with the purpose of tracking incidents as they occur, and allows the incident responder to take notes on their investigation timeline in real-time. 

## Implementation Notes

When a user account is created they are going to beassinged a user id and will configure first name and last name
In the accoutn creation ui they will be able to set up first name and last name.
After users login they will be able to see a dashboard for all cyber events. 
So users will create an incident and the default status will be open (something along those lines) 

### Event Statuses 

1. Created
    - The Open status indicates that an event has been created, however, no action has been taken on the event. 
1. Investigating
    - This indicates that and incident responder has been assigned to the incident and is ungoing detection and analysis phase.
1. Containment 
    - Isolation/Segmentation of networks and systems to prevent the spread of the threat. 
1. Eradication 
    - Remove the intruders access to any systems, services, or accounts that were leveraged as a result of the incident. 
    - Remove malware/services that were created as a result of the incident 
    - Identify and patch the vulnerability used within the incident 
1. Recovery 
    - Confirmation of threat removal, as well as implementing additional monitoring on affected systems.
    - Return systems to operational ready state. 
1. Lessons Learned 
    - Discussing with stake-holders how we can better respond in the future and the likelyhood of the incident reoccuring and any controls we have put in place to resolve the incident.
1. Resolved 
    - There is no further actions required at this time.

### Event Types

1. Phishing Attacks
   - Attempts to deceive individuals into providing sensitive information such as passwords, credit card numbers, or personal information by posing as a legitimate entity.
1. Malware Infections
   - Malicious software designed to infiltrate and damage computer systems, steal data, or gain unauthorized access.
1. Ransomware Attacks
   - Malware that encrypts files or locks users out of their systems, demanding payment (usually in cryptocurrency) for the decryption key.
1. Denial of Service (DoS) and Distributed Denial of Service (DDoS) Attacks
   - Attempts to make a network resource or website unavailable to users by overwhelming it with a flood of traffic.
1. Data Breaches
   - Unauthorized access to sensitive or confidential information, resulting in its exposure, theft, or compromise.
1. Social Engineering Attacks
   - Manipulating individuals into divulging confidential information or performing actions that compromise security, often through psychological manipulation.
1. Account Compromise
   - Unauthorized access to user accounts through various means such as stolen credentials, weak passwords, or exploitation of vulnerabilities.
1. Man-in-the-Middle (MitM) Attacks
   - Interception of communication between two parties by an attacker, allowing them to eavesdrop, modify, or inject data without either party's knowledge.

### Event Severity

1. A 
   - Highest level of severity. All Hands on Decks, Most Senior IR teams engaged. Most customers impacted or sensitive services/data have been compromised.
2. B 
   - Medium level of severity. Many customers impacted but business can continue. 
3. C 
   - Low Level of severity. Minimal or no customer impact. No impact to business continuity. 
4. D 
   - Very low level of severity. No customer impact, Ir team engaged as needed.  


#### Event Severity Notes
The above severity levels are in place for the Minimal Viable Product, however orginizations should be able to accept what levels they should use (A,B,C,D or 1,2,3,4) and enter custom descriptions.

### Account Roles 

1. Admin 
   1. Allows a user to create incidents, manage users, manage teams, and resolve incidents 
2. Responder
   1. Responders can be added to a response team, manage incidents, and update incidents
3. ReadOnly 
   1. Read only users are able to view reports about an incident and review an incident timeline but are unable to actually add notes to an incident, change the incidents status, or perform any administrative actions.

### Event Timeline Entry Type

1. Status Change
   1. The status of the event has been updated.
2. Note Added
   1. A note was added at its current stage.
1. Severity Change
   1. The severity event has been changed.
1. Team Assigned
   1. An Incident Response team has been assigned to the incident.
1. Type Change
   1. The Event Type was changed.


## TODO: 

### SQL.py functions 

functions: 

-  test

-  call the following functions -

   - ~~GetEventTypeById~~
   - ~~GetAllEventTypes~~
   - ~~GetEventStatusById~~
   - ~~GetAllEventStatuses~~
   - ~~CreateEvent~~
   - ~~GetEventById~~
   - ~~GetAllEvents~~
   - ~~UpdateEvent~~
   -  ~~DeleteEvent~~

   -  CreateEventTimelineEntryType
   -  GetEventTimelineEntryTypes
   -  GetEventTimelineEntryTypeById
   -  UpdateEventTimelineEntryType
   -  DeleteTimelineEntryType

   -  CreateEventTimeline
   -  GetEventTimelineByUUID
   -  UpdateEventTimeline
   -  DeleteEventTimeline

   -  CreateEventTimelineNote 
   -  ~~GetEventTimelineNotesByTimelineUUID~~
   -  ~~UpdateEventTimelineNote~~
   -  ~~DeleteEventTimelineNote~~

### Method of Operations for creating sql.py functions 

#### Reviewing the stored procedure 
1. Get the name of the stored procedure you're going to call from Python 
 - `CreateEventTimelineNote` 

2. Determine what parameters you must provide to the SQL Stored Procedure and their Data Type 
   - TimelineUUIDParam UUID 
   - EntryNoteParam TEXT 

EXAMPLE PROCEDURE: 

```sql  
CREATE OR REPLACE PROCEDURE CreateEventTimelineNote(
    TimelineUUIDParam UUID,
    EntryNoteParam TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Event_Timeline_Notes (TimelineNoteUUID, TimelineUUID, EntryNote)
    VALUES (uuid_generate_v4(), TimelineUUIDParam, EntryNoteParam);
END;
$$;

```

#### Calling the stored procedure using Python 

1. Create a model class if one does not already exist 
   1. Query the table that the stored procedure is running against to get the schema of the table or review the `TableSchema.dbml` file 
   2. Replicate the table within a Pydantic BaseModel class, mapping the SQL data type for each row to a Python datatype. 
      1. TEXT, UUID, VARCHAR = str
      2. INT, SERIAL = int 
      3. TIMESTAMP, DATETIME = datetime 

   EXAMPLE Base Model: 

   ```Python 

   class EventTimelineNote(BaseModel): 
    timeline_note_uuid: str | None = None
    timeline_uuid: str | None = None
    entry_note: str | None = None
    created_on: datetime | None = None
   
   ```

2. Name the function pythonically 
   1. Python uses `snake_case` for it's function names 

   EXAMPLE: 
      1. Calling a stored procedure named       `CreateEventTimelineNote` would be done via a Python function called `create_event_timeline_note` 

3. Determine what arguments you need to provide to the Python function that will be passed to the SQL query as parameters 
   1. Are all of the parameters covered in the Model class, or must we pass additional arguments? 

4. Create the qstring variable that will be used to invoke the SQL query 
   1. Stored procedures will be called using the `CALL` syntax. 
   
   > EXAMPLE for a stored procedure named `CreateEventTimelineNote` that accepts the parameters `TimelineUUIDParam` and `EntryNoteParam`: 
   > 
   >  `CALL CreateEventTimelineNote TimelineUUIDParam => %s, EntryNoteParam => %s ` 
