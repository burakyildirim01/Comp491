from flask import Flask, request,make_response
from replit import web
from BlackBoardAPI import BlackBoardAPI
from KusisAPI import KusisAPI
import json


# Create a flask app
app = Flask(__name__)

@app.route('/')
def hello():
  return 'hello'
# Index page
@app.route('/allCourses')
def getAllCourses():
  cookie = request.headers.get('Cookie')
  bb_API = BlackBoardAPI(cookie)
  courses = bb_API.getAllCourses()
  json_string = json.dumps([ob.__dict__ for ob in courses])
  r = make_response( json_string )
  r.mimetype = 'application/json'
  return r
  
@app.route('/mygrades/<course_id>')
def getGrade(course_id):
  cookie = request.headers.get('Cookie')
  bb_API = BlackBoardAPI(cookie)
  grades = bb_API.getGrades(course_id)
  
  json_string = json.dumps([ob.__dict__ for ob in grades])
  
  r = make_response( json_string )
  r.mimetype = 'application/json'
  return r
  
@app.route('/calendarEvents')
def getCalendarEvent():
  cookie = request.headers.get('Cookie')
  
  from_ms = request.args.get('from')
  to_ms = request.args.get('to')
  
  bb_API = BlackBoardAPI(cookie)
  events = bb_API.getCalendarEvents(from_ms, to_ms)
  json_string = json.dumps(events)
  r = make_response( json_string )
  r.mimetype = 'application/json'
  return r
  
@app.route('/letterGrades')
def getLetterGrades():
  cookie = request.headers.get('Cookie')
  records = KusisAPI(cookie).getLetterGrades()
  json_string = json.dumps([record.__dict__ for record in records])
  r = make_response( json_string )
  r.mimetype = 'application/json'
  return r
  
web.run(app)