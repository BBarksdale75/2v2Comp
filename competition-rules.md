# 2 v 2 Competition Guidelines

## Topic 

### Create an incident tracking application

#### Description
Create an application that allows a company to create a new event for a cyber security incident. While it is up to said company to determine what warants an event, they need to be able to track whatever events they create. This includes collecting information and evidence about that event. Some information will be collected on creation of the event automatically and some needs to be able to be inputed by the company. 

Once an event is created the company needs to be able to add status tags to the event for tracking purposes. Once an event is complete the item must be able to be marked complete, closed, and then logged for historical purposes.

### Requirements
overall
- [] Allows for user managment
  - [] Users need to belong to a company
  - [] Create users
  - [] Edit users
  - [] delete users
  - [] manage user permissions
- [] Allow users to create and manage incident `Events`
  - [] Create events
  - [] delete an event
  - [] Set Event status
  - [] Mark Events complete
  - [] Allow comments on the events
  - [] Allows users to tag events based on the risk - like high, medium, low
  - [] EXTRA - Events need to get archived and then be able to list old archieved events
- [] Allow evidence collection on a per event basis
  - [] Evidence needs to be associated with one event
    - [] Allow for basic information to be collected on event creation.
      - Time/Date Create (auto)
      - Incident Time and Date
      - Incident Information
        - Title
        - Description
        - Affected Items
        - Who is affected
  - [] Need to allow comments on events
  - [] Evidence needs to be able to be images or text
- [] Other
  - [] Need to be able to track the length of an event
  - [] EXTRA - Export - Allow users to export events in PDF format
 

- [] UI
  - [] login page
  - [] MFA - Depending on free version of Auth0
  - [] Home page
    - [] lists recent events
    - [] shows a total number of each event category with a focus on any high risk events
  - [] Event Page
    - [] Create Events
    - [] Mange exsisting events
    - [] Ability to click on events and have them bring up a seperate box to mangae it there and add comments. This is also where you would add evidence to the page
  - [] Admin Page
    - Manage Users
    - Manage permissions
  - [] EXTRA - Archieved Page see old events and their evidence/comments
  - [] EXTRA - Management Page - Allows users to see the length of events and what the time it took and see over time if the response time is increasing or decreasing


### Rules

- No more then 60% of the code can be written by either David or Tony on their applicable teams
  - This allows for Hank and Brandon to get practice and be more involved
  - This will be checked using githubs available tools
- Code MUST be commented well. A 3rd party needs to be able to walk through it in a traditional code review setting.
- As a gentlemens agreement try to use chat gpt as little as possible.
  - If you are both stuck on something and it is gating you from completing something you may use it after you have exhausted other means.
  - It will be easy to see the difference between your code and chat GPTs code.
- The ChatGPT rule applies for code found online. While you are more than welcome to use online resources the idea is that you learn, not copy.
- The application needs to be completed on time. (Enter time constraint here)
  - For everyday that the application is completed late you will lose a points.
- Each teams repositories should be private and control access using GitHubs tools. This prevents the other team from accessing the others code.

### Point System 

1. **User Management**: 10 points
2. **Incident Events Management**: 20 points
3. **Evidence Collection**: 15 points
4. **UI Elements**:
   - Login Page: 5 points
   - MFA: 5 points
   - Home Page: 10 points
   - Event Page: 15 points
   - Admin Page: 10 points
   - Archived Page: 5 points (extra)
   - Management Page: 5 points (extra)
5. **Code Quality**:
   - Well-commented code: 10 points
   - Clean code structure and organization: 10 points
6. **Additional Requirements**:
   - Event History: 5 points
   - Dashboard: 10 points
   - Export/Import: 5 points (Extra)
7. **Timeline**: Deduct 5 point for each day late.


