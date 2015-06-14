import bottle
import sys
import os
import json
sys.path.insert(0, '/home/martyni/bottlesite')

from update import speed_project
from static import default
from bus_times import Bus_Times
my_db = speed_project()

@bottle.get('/download/<speed>')
def get_download(speed):
   speed = float(speed)
   return my_db.get_date(speed)

@bottle.get('/bus')
def get_bus_times():
   my_times = Bus_Times()
   return json.dumps(my_times.bus_times)

@bottle.get('/upload/<speed>')
def get_upload(speed):
   speed = float(speed)
   return my_db.get_date(speed, direction='Upload')

@bottle.get('/average_day')
def get_average_day():
   report = my_db.average_day_report()
   return report

@bottle.get('/average_time')
def get_average_day():
   report = my_db.average_time()
   return report

@bottle.route('/')
def thing():
   return os.path.abspath('./')
 
@bottle.route('/static')
def templ():
   return bottle.template(default)

@bottle.route('/mystyle.css')
def style():
   return bottle.static_file('/mystyle.css',root='/home/martyni/bottlesite/static')

@bottle.post('/json')
def deal_with_it():
   post = bottle.request.body
   d = json.loads(post.read())
   my_db = speed_project()
   obj_id = my_db.update_speed(d) 
   return str(obj_id)

@bottle.route('/static/<filepath:path>')
def serve_static(filepath):
   return bottle.static_file(filepath, root='/home/martyni')

@bottle.get('/mongo')
def get_stuff():
   objects = str(my_db.test())
   return objects

@bottle.get('/average')
def get_average():
  aggregate =  my_db.get_aggregate()
  return aggregate

@bottle.get('/last_40')
def get_last():
  last = my_db.last_40()
  return last

