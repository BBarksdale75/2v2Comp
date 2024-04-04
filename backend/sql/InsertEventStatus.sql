INSERT INTO Event_Status (EventStatusName, EventStatusDesc) 
VALUES ('Created', 'The Open status indicates that an event has been created, however, no action has been taken on the event.'),
('Investigating' ,'This indicates that and incident responder has been assigned to the incident and is ungoing detection and analysis phase.'), 
('Containment', 'Isolation/Segmentation of networks and systems to prevent the spread of the threat.'),
('Eradication', 'Remove the intruders access to any systems, services, or accounts that were leveraged as a result of the incident. -Remove malware/services that were created as a result of the incident. -Identify and patch the vulnerability used within the incident'),
('Recovery', 'Confirmation of threat removal, as well as implementing additional monitoring on affected systems. -Return systems to operational ready state.'),
('Lessons Learned', 'Discussing with stake-holders how we can better respond in the future and the likelyhood of the incident reoccuring and any controls we have put in place to resolve the incident.'),
('Resolved', '-There is no further actions required at this time.');

