<h1> Overview </h1>
Independent study project for SIUE. Using twitter API and sentiment analysis for emotion visualization.

# ToDo
- [x] connect to tweepy api
- [x] connect to mysql database
- [x] filter tweets based on a certain tag
- [x] setup script to run on dedicated computer
- [ ] sentiment analysis
- [ ] visualization

<h1> Setup </h1>
Python v3.6.6 (any version of Python 3 _should_ work--no guarentees)
MySQL v8.0.12


<h2> Mac OSX </h2>
<h4> Setup Virtualenv</h4>
run `pip install virtualenv` if you don't already have it installed. Now you can create a virtual environment for this project. 
Now, create the environment with `virtualenv -p python3 venv`, and activate it with `source venv/bin/activate`. 
Next, run `pip install -r requirements.txt` to install the required libraries.
<h4>Setup Auth Variables</h4>
First, you'll need to create the auth.py file with all 4 keys from your twitter developer project, as well as the connections to your database. (this step is the same for any environment)

Be sure to name your variables as follows: 
* Twitter
  * CONSUMER_KEY
  * CONSUMER_SECRET
  * ACCESS_TOKEN
  * ACCESS_TOKEN_SECRET
* Database
  * HOST
  * DATABASE
  * PASSWORD
  * USER

<h4> Notes</h4>
The MySQL server for Mac OSX has issues storing emojis (unicode_ci) characters. However, this isn't an issue with running this project on Windows. I currently do not have a solution for this issue.

<h2> Windows</h2>
<h4> Setup Virtualenv</h4>
run `pip install virtualenv` if you don't already have it installed. You'll also need to install `pip virtualenvwrapper-win`. Now you can create a virtual environment for this project. 
This is done by running `makevirtualenv venv`. 
Next, run `pip install -r requirements.txt` to install the required libraries.

<h4>Setup Auth Variables</h4>
First, you'll need to create the auth.py file with all 4 keys from your twitter developer project, as well as the connections to your database. (this step is the same for any environment)

Be sure to name your variables as follows: 
* Twitter
  * CONSUMER_KEY
  * CONSUMER_SECRET
  * ACCESS_TOKEN
  * ACCESS_TOKEN_SECRET
* Database
  * HOST
  * DATABASE
  * PASSWORD
  * USER
  
  
# Using the Project
The driver file for this script is the analyze_data.py file. This is that file that you could edit to filter for specific tweets. 
auth.py is just for keeping track of your authentication variables for the project. 
db_stream.py is for connecting to the database, and writing data to the database. 
