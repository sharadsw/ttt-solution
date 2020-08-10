# ttt-solution
A solution to the terribly tiny tales challenge. Deployed on Heroku over here: [ttt-solution.herokuapp.com](https://ttt-solution.herokuapp.com)

### Dependencies
* flask
* flask-wtf
* requests
* gunicorn (only for deploying on heroku)

### Installing
Clone repo
```
git clone https://github.com/sharadsw/ttt-solution
```
Install all dependencies
```
pip install -r requirements.txt
```
Create config variables
```
export FLASK_APP=main.py
export SECRET_KEY=key-goes-here
```

### Usage
Run the flask app. It runs on http://127.0.0.1:5000/
```
flask run
```
![screenshot](http://u.cubeupload.com/gooseyloosey/ttt1.png)

### Code
The frontend is written with Bootstrap and jinja templating. The backend is written in Flask.

#### freq.py
This module calculates the word frequency from any given text.
* The get_file() function retrieves the text from a given url using the requests module.
* The clean_text() function cleans the given text. Unicode characters, escape characters, punctuations, and extra spaces are removed and then the string is converted to lowercase for consistency.
* The parse_text() function calculates the word frequency from the given text. The text is split into an array of words. The function iterates over this array and inputs each word into a dict with its corresponding frequency. Using python's sorted() function, this dict is sorted into a list of (word:freq) tuples in descending order which is then returned to the caller.

#### forms.py
This module uses [Flask-WTForms](https://github.com/lepture/flask-wtf) to define the form to be used in the frontend. WTForms provide backend validation and security against CSRF attacks.

#### app.py
This module creates the Flask instance to be used to run the app.

#### routes.py
This module defines the routes to the application. It handles the incoming request when a form is submitted.

#### main.py
This module ties the app.py and routes.py modules together and runs the application. The reason for this split into three different modules is to avoid any circular dependencies.