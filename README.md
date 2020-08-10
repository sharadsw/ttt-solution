# ttt-solution
A solution to the terribly tiny tales challenge.

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
python main.py
```
![screenshot](http://u.cubeupload.com/gooseyloosey/ttt1.png)
