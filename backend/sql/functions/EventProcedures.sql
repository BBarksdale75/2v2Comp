-- Procedure to create a new event type
CREATE OR REPLACE PROCEDURE CreateEventType(EventTypeName VARCHAR, EventTypeDesc TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
   INSERT INTO Event_Type (EventTypeName, EventTypeDesc)
   VALUES (EventTypeName, EventTypeDesc);
END;
$$;

-- Function to get an event type by its ID
CREATE OR REPLACE FUNCTION GetEventTypeById(TypeId INT)
RETURNS TABLE (
    EventTypeId INT,
    EventTypeName VARCHAR,
    EventTypeDesc TEXT
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT et.EventTypeId, et.EventTypeName, et.EventTypeDesc
    FROM Event_Type et
    WHERE et.EventTypeId = TypeId; 
END;
$$;

-- Function to get all event types
CREATE OR REPLACE FUNCTION GetAllEventTypes()
RETURNS TABLE (
    EventTypeId INT,
    EventTypeName VARCHAR,
    EventTypeDesc TEXT
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT et.EventTypeId, et.EventTypeName, et.EventTypeDesc
    FROM Event_Type et; 
END;
$$;

-- Procedure to update an event type
CREATE OR REPLACE PROCEDURE UpdateEventType(TypeId INT, 
    TypeName VARCHAR DEFAULT NULL, 
    TypeDesc TEXT DEFAULT NULL)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Event_Type
    SET EventTypeName = COALESCE(TypeName, Event_Type.EventTypeTypeName),
        EventTypeDesc = COALESCE(TypeDesc, Event_Type.EventTypeDesc)
    WHERE EventTypeId = TypeId;
END;
$$;

-- Procedure to delete an event type
CREATE OR REPLACE PROCEDURE DeleteEventType(TypeId INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Event_Type
    WHERE EventTypeId = TypeId;
END;
$$;

-- Procedure to create a new event status
CREATE OR REPLACE PROCEDURE CreateEventStatus(StatusName VARCHAR, StatusDesc TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
   INSERT INTO Event_Status (EventStatusName, EventStatusDesc)
   VALUES (StatusName, StatusDesc);
END;
$$;

-- Function to get an event status by its ID
CREATE OR REPLACE FUNCTION GetEventStatusById(StatusId INT)
RETURNS TABLE (
    EventStatusId INT,
    EventStatusName VARCHAR,
    EventStatusDesc TEXT
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT es.EventStatusId, es.EventStatusName, es.EventStatusDesc
    FROM Event_Status es
    WHERE es.EventStatusId = StatusId; 
END;
$$;

-- Function to get all event statuses
CREATE OR REPLACE FUNCTION GetAllEventStatuses()
RETURNS TABLE (
    EventStatusId INT,
    EventStatusName VARCHAR,
    EventStatusDesc TEXT
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT es.EventStatusId, es.EventStatusName, es.EventStatusDesc
    FROM Event_Status es; 
END;
$$;

-- Procedure to update an event status
CREATE OR REPLACE PROCEDURE UpdateEventStatus(StatusId INT, 
    StatusName VARCHAR DEFAULT NULL, 
    StatusDesc TEXT DEFAULT NULL)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Event_Status
    SET EventStatusName = COALESCE(StatusName, Event_Status.EventStatusName),
        EventStatusDesc = COALESCE(StatusDesc, Event_Status.EventStatusDesc)
    WHERE EventStatusId = StatusId;
END;
$$;

-- Procedure to delete an event status
CREATE OR REPLACE PROCEDURE DeleteEventStatus(StatusId INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Event_Status
    WHERE EventStatusId = StatusId;
END;
$$;

CREATE OR REPLACE PROCEDURE CreateEvent(
    EventTypeParam INT,
    EventNameParam VARCHAR,
    EventStatusIdParam INT,
    CommanderUserUUIDParam UUID,
    EventSeverityIdParam INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Event (EventTypeId, EventName, EventStatusId, CommanderUserUUID, EventSeverityId)
    VALUES (EventTypeParam, EventNameParam, EventStatusIdParam, CommanderUserUUIDParam, EventSeverityIdParam);
END;
$$;

-- Function to get an event by its ID
CREATE OR REPLACE FUNCTION GetEventById(EventUUIDParam UUID)
RETURNS TABLE (
    EventUUID UUID,
    EventTypeId INT,
    EventName VARCHAR,
    EventStatusId INT,
    CommanderUserUUID UUID,
    EventSeverityId INT
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT e.EventUUID, e.EventTypeId, e.EventName, e.EventStatusId, e.CommanderUserUUID, e.EventSeverityId
    FROM Event e
    WHERE e.EventUUID = EventUUIDParam; 
END;
$$;

-- Function to get all events
CREATE OR REPLACE FUNCTION GetAllEvents()
RETURNS TABLE (
    EventUUID UUID,
    EventTypeId INT,
    EventName VARCHAR,
    EventStatusId INT,
    CommanderUserUUID UUID,
    EventSeverityId INT
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT event.EventUUID, e.EventTypeId, e.EventName, e.EventStatusId, e.CommanderUserUUID, e.EventSeverityId
    FROM Event e ; 
END;
$$;

CREATE OR REPLACE PROCEDURE UpdateEvent(
    EventUUIDParam UUID, 
    EventTypeIdParam INT DEFAULT NULL, 
    EventNameParam VARCHAR DEFAULT NULL, 
    EventStatusIdParam INT DEFAULT NULL, 
    CommanderUserUUIDParam UUID DEFAULT NULL, 
    EventSeverityIdParam INT DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Event
    SET 
        EventTypeId = COALESCE(EventTypeIdParam, Event.EventTypeId),
        EventName = COALESCE(EventNameParam, Event.EventName),
        EventStatusId = COALESCE(EventStatusIdParam, Event.EventStatusId),
        CommanderUserUUID = COALESCE(CommanderUserUUIDParam, Event.CommanderUserUUID),
        EventSeverityId = COALESCE(EventSeverityIdParam, Event.EventSeverityId)
    WHERE EventUUID = EventUUIDParam;
END;
$$;

CREATE OR REPLACE PROCEDURE DeleteEvent(EventUUIDParam UUID)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Event
    WHERE EventUUID = EventUUIDParam;
END;
$$;

CREATE OR REPLACE PROCEDURE CreateEventTimelineEntryType(
    TimelineEntryTypeNameParam VARCHAR,
    TimelineEntryTypeDescParam TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Event_Timeline_Entry_Type (TimelineEntryTypeName, TimelineEntryTypeDesc)
    VALUES (TimelineEntryTypeNameParam, TimelineEntryTypeDescParam);
END;
$$;

CREATE OR REPLACE FUNCTION GetEventTimelineEntryTypes()
RETURNS TABLE (
    TimelineEntryTypeId INT,
    TimelineEntryTypeName VARCHAR,
    TimelineEntryTypeDesc TEXT
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT TimelineEntryTypeId, TimelineEntryTypeName, TimelineEntryTypeDesc
    FROM Event_Timeline_Entry_Type; 
END;
$$;

CREATE OR REPLACE FUNCTION GetEventTimelineEntryTypeById(TimelineEntryTypeIdParam INT)
RETURNS TABLE (
    TimelineEntryTypeId INT,
    TimelineEntryTypeName VARCHAR,
    TimelineEntryTypeDesc TEXT
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT TimelineEntryTypeId, TimelineEntryTypeName, TimelineEntryTypeDesc
    FROM Event_Timeline_Entry_Type
    WHERE TimelineEntryTypeId = TimelineEntryTypeIdParam; 
END;
$$;

CREATE OR REPLACE PROCEDURE UpdateEventTimelineEntryType(
    TimelineEntryTypeIdParam INT,
    TimelineEntryTypeNameParam VARCHAR DEFAULT NULL,
    TimelineEntryTypeDescParam TEXT DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Event_Timeline_Entry_Type
    SET 
        TimelineEntryTypeName = COALESCE(TimelineEntryTypeNameParam, Event_Timeline_Entry_Type.TimelineEntryTypeName),
        TimelineEntryTypeDesc = COALESCE(TimelineEntryTypeDescParam, Event_Timeline_Entry_Type.TimelineEntryTypeDesc)
    WHERE TimelineEntryTypeId = TimelineEntryTypeIdParam;
END;
$$;

CREATE OR REPLACE PROCEDURE DeleteTimelineEntryType(TimelineEntryTypeIdParam INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Event_Timeline_Entry_Type
    WHERE TimelineEntryTypeId = TimelineEntryTypeIdParam;
END;
$$;

CREATE OR REPLACE PROCEDURE CreateEventTimeline(
    EventUUIDParam UUID,
    TimelineUUIDParam UUID,
    TimelineNoteUUIDParam VARCHAR,
    TimelineEntryTypeIdParam INT,
    EnteredByUserUUIDParam UUID
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Event_Timeline (EventUUID, TimelineUUID, TimelineNoteUUID, TimelineEntryTypeId, EnteredByUserUUID)
    VALUES (EventUUIDParam, TimelineUUIDParam, TimelineNoteUUIDParam, TimelineEntryTypeIdParam, EnteredByUserUUIDParam);
END;
$$;

CREATE OR REPLACE FUNCTION GetEventTimelineByUUID(TimelineUUIDParam UUID)
RETURNS TABLE (
    EventUUID UUID,
    TimelineUUID UUID,
    TimelineNoteUUID VARCHAR,
    TimelineEntryTypeId INT,
    EnteredByUserUUID UUID,
    CreatedOn TIMESTAMP
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT EventUUID, TimelineUUID, TimelineNoteUUID, TimelineEntryTypeId, EnteredByUserUUID, CreatedOn
    FROM Event_Timeline
    WHERE TimelineUUID = TimelineUUIDParam; 
END;
$$;

CREATE OR REPLACE PROCEDURE UpdateEventTimeline(
    TimelineUUIDParam UUID,
    TimelineNoteUUIDParam VARCHAR DEFAULT NULL,
    TimelineEntryTypeIdParam INT DEFAULT NULL,
    EnteredByUserUUIDParam UUID DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Event_Timeline
    SET 
        TimelineNoteUUID = COALESCE(TimelineNoteUUIDParam, Event_Timeline.TimelineNoteUUID),
        TimelineEntryTypeId = COALESCE(TimelineEntryTypeIdParam, Event_Timeline.TimelineEntryTypeId),
        EnteredByUserUUID = COALESCE(EnteredByUserUUIDParam, Event_Timeline.EnteredByUserUUID)
    WHERE TimelineUUID = TimelineUUIDParam;
END;
$$;

CREATE OR REPLACE PROCEDURE DeleteEventTimeline(TimelineUUIDParam UUID)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Event_Timeline
    WHERE TimelineUUID = TimelineUUIDParam;
END;
$$;

CREATE OR REPLACE PROCEDURE CreateEventTimelineNote(
    TimelineNoteUUIDParam UUID,
    TimelineUUIDParam UUID,
    EntryNoteParam TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Event_Timeline_Notes (TimelineNoteUUID, TimelineUUID, EntryNote)
    VALUES (TimelineNoteUUIDParam, TimelineUUIDParam, EntryNoteParam);
END;
$$;

CREATE OR REPLACE FUNCTION GetEventTimelineNotesByTimelineUUID(TimelineUUIDParam UUID)
RETURNS TABLE (
    TimelineNoteUUID UUID,
    TimelineUUID UUID,
    EntryNote TEXT,
    CreatedOn TIMESTAMP
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT TimelineNoteUUID, TimelineUUID, EntryNote, CreatedOn
    FROM Event_Timeline_Notes
    WHERE TimelineUUID = TimelineUUIDParam; 
END;
$$;

CREATE OR REPLACE PROCEDURE UpdateEventTimelineNote(
    TimelineNoteUUIDParam UUID,
    EntryNoteParam TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Event_Timeline_Notes
    SET 
        EntryNote = COALESCE(EntryNoteParam, Event_Timeline_Notes.EntryNote)
    WHERE TimelineNoteUUID = TimelineNoteUUIDParam;
END;
$$;

CREATE OR REPLACE PROCEDURE DeleteEventTimelineNote(TimelineNoteUUIDParam UUID)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Event_Timeline_Notes
    WHERE TimelineNoteUUID = TimelineNoteUUIDParam;
END;
$$;

