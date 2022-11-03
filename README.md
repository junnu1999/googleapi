# googleapi
For run this project on a local machine:

pip install - r requriments.txt
Endpoint:
/rest/v1/calendar/init/ -> GoogleCalendarInitView()
This view should start step 1 of the OAuth. Which will prompt user for his/her credentials

/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
This view will do two things

Handle redirect request sent by google with code for token. You need to implement mechanism to get access_token from given code
Once got the access_token get list of events in users calendar

You'll need to set a redirect URL to your Google Cloud account and preserve your Google account credentials in the project directory in order to complete this assignment. Please read the references and documents section below.


Google Identity: Using OAuth 2.0 for Web Server Applications
https://developers.google.com/identity/protocols/oauth2/web-server
Google Calendar API
https://developers.google.com/calendar/api/v3/reference

Google Account Credentials
https://developers.google.com/identity/protocols/oauth2/web-server#exchange-authorization-codee
