CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE DATABASE trackwolf; 

\c trackwolf 

CREATE TABLE Account_Role (
    AccountRoleId SERIAL PRIMARY KEY,
    AccountRoleName VARCHAR
);

CREATE TABLE Account (
    UserUUID UUID PRIMARY KEY,
    UserFName VARCHAR,
    UserLName VARCHAR,
    CreatedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
    AccountRoleId INT,
    isActive BOOLEAN,
    FOREIGN KEY (AccountRoleId) REFERENCES Account_Role(AccountRoleId)
);

CREATE TABLE ResponseTeam (
    ResponseTeamUUID UUID PRIMARY KEY,
    ResponseTeamDescription TEXT,
    ResponseTeamName VARCHAR
);

CREATE TABLE ResponseTeam_Account (
    UserUUID UUID,
    ResponseTeamUUID UUID,
    FOREIGN KEY (UserUUID) REFERENCES Account(UserUUID),
    FOREIGN KEY (ResponseTeamUUID) REFERENCES ResponseTeam(ResponseTeamUUID),
    PRIMARY KEY (UserUUID, ResponseTeamUUID)
);

CREATE TABLE Event_Type (
    EventTypeId SERIAL PRIMARY KEY,
    EventTypeName VARCHAR,
    EventTypeDesc TEXT
);

CREATE TABLE Event_Status (
    EventStatusId SERIAL PRIMARY KEY,
    EventStatusName VARCHAR,
    EventStatusDesc TEXT
);

CREATE TABLE Event_Severity (
    EventSeverityId SERIAL PRIMARY KEY,
    EventSeverityLevel VARCHAR,
    EventSeverityDesc TEXT
);

CREATE TABLE Event (
    EventUUID UUID PRIMARY KEY,
    EventTypeId INT,
    EventName VARCHAR,
    EventStatusId INT,
    CommanderUserUUID UUID,
    EventSeverityId INT,
    CreatedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (EventTypeId) REFERENCES Event_Type(EventTypeId),
    FOREIGN KEY (EventStatusId) REFERENCES Event_Status(EventStatusId),
    FOREIGN KEY (CommanderUserUUID) REFERENCES Account(UserUUID),
    FOREIGN KEY (EventSeverityId) REFERENCES Event_Severity(EventSeverityId)
);

CREATE TABLE Event_Timeline_Entry_Type (
    TimelineEntryTypeId SERIAL PRIMARY KEY,
    TimelineEntryTypeName VARCHAR,
    TimelineEntryTypeDesc TEXT
);


CREATE TABLE Event_Timeline (
    EventUUID UUID,
    TimelineUUID UUID PRIMARY KEY,
    TimelineNoteUUID VARCHAR,
    TimelineEntryTypeId INT,
    EnteredByUserUUID UUID,
    CreatedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (EventUUID) REFERENCES Event(EventUUID),
    FOREIGN KEY (TimelineEntryTypeId) REFERENCES Event_Timeline_Entry_Type(TimelineEntryTypeId),
    FOREIGN KEY (EnteredByUserUUID) REFERENCES Account(UserUUID)
);


CREATE TABLE Event_Timeline_Notes (
    TimelineNoteUUID UUID,
    TimelineUUID UUID,
    EntryNote TEXT,
    CreatedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
    PRIMARY KEY (TimelineUUID, TimelineNoteUUID),
    FOREIGN KEY (TimelineUUID) REFERENCES Event_Timeline(TimelineUUID)
);
