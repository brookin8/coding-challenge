# Referral Manager API

### Problem

-	The team needs to create a simple referral system to promote the World Wide Web. 
-	The system should allow the customer to create, edit, delete, track, and view landing pages for referral links.
-	As a back-end developer, I need to build an API that supports all of these actions. 

### Solution (Back-end)

-	Use Django, Django Rest Framework, PostgreSQL, and Heroku to build and deploy a straightforward REST API for referrals. 

### Reasoning

#### Technologies: 

-	Django, Django Rest Framework, and Heroku were specified by the customer. 
-	PostgreSQL is open source, easy to startup quickly, provides better scalability than the default SQLite, and plays well with Heroku. Additionally, from the information provided, the Referral system can be easily represented by a basic relational setup. 

#### Architecture:

-	First, a call out: I was constrained a little bit with directory choices by sticking to what works with Heroku. 
-	I kept everything to a single Referral model given that we aren't keeping track of any other type of entity or relationship. 
-	Within the Referral model, I only added the two 'Title' and 'Clicks' fields, given that the link will always just be a standard '{url}/ + title'
- 	I debated having the 'Clicks' increment action just be a part of the same endpoint as the GET call for the details of a single referral. However, I could think of a few other instances where that endpoint might be utilized and the customer would not want clicks incremented (IE a "details" screen, an edit screen that doesn't take the referral information directly from the rows in the list page). 
-	I chose instead to create a separate endpoint where a deliberate 'POST' call will increment the Clicks number for the relevant referral entry. 

### Trade-Offs and Next Steps

-	Given more time, I would possibly have investigated different data storage options to see if there's a better option. 
-	If I were working on this professionally, I would likely have clarified requirements around the landing page behavior to help me better make the decision around the click incrementing setup I outlined above. 
-	Also, I would eventually like to build the outlined UI using React and Redux. I might add a simple auth setup, too. 

### Link to the Hosted API: https://referralmanager.herokuapp.com/api/referrals/

- The URL above will list all referrals (GET) or create a new referral (POST). 
- Adding the referral ID to the very end of the API will access the GET/PUT/DELETE actions for that referral. 


