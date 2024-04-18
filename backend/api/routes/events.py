from fastapi import APIRouter
from api.models import EventModel, EventTimelineEntry
from db.sql import Events, EventTimeline

router = APIRouter() 
event_handler = Events()
timeline_handler = EventTimeline()

@router.get('/event')
async def get_events_async(): 
    return event_handler.get_events()

@router.post('/event')
async def create_event_async(body: EventModel):
    return event_handler.create_event(body)

@router.get('/event/types')
async def get_event_types_async():
    return event_handler.get_event_types()

@router.get('/event/{event_uuid}')
async def create_event_async(event_uuid: str):
    return event_handler.get_event_by_id(event_uuid=event_uuid)

@router.patch('/event/{event_uuid}')
async def update_event_async(event_uuid: str, body:EventModel): 
    return event_handler.update_event(event_uuid=event_uuid, 
                                      updated_information=body)

@router.get('/event/{event_uuid}/timeline')
async def get_event_timeline_entries_async(event_uuid: str):
    return timeline_handler.get_event_timeline_entries_by_event_uuid(event_uuid=event_uuid)

@router.post('/event/{event_uuid}/timeline')
async def create_event_timeline_entry(event_uuid: str, body: EventTimelineEntry):
    body.event_uuid = event_uuid
    return  timeline_handler.create_event_timeline(body)

@router.delete('/event/{event_uuid}')
async def delete_event_async(event_uuid: str):
    return event_handler.delete_event(event_uuid=event_uuid)

@router.get('/event/severity/')
async def get_event_severity_async(): 
    raise NotImplementedError(f'This is not yet implemented and is pending the completion of the event severity SQLManager functions')
