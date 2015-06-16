import pymongo
import datetime
import bottle
import json

class speed_project(object):
   def __init__(self):
      '''sets up mongo connection'''
      self.repl_set = ["mongodb://mongo%s:27017" % i for i in range(1,4)]
      self.repl_set_name = "rs0"
      self.write_concern = 2
      self.j = True
      self.connection = pymongo.MongoClient(host=self.repl_set, replicaSet=self.repl_set_name, w=self.write_concern, j=self.j)
      self.db = self.connection.speeds
      self.col = self.db.test

   def average_day_report(self):
      '''Runs an aggregate report grouping by day'''
      project = {"$project" : { 
                 "_id" : "$_id", 
                 "download" : "$Download",
                  "upload" : "$Upload" , 
                  "day" : {"$dayOfWeek" :"$date"}}}
      group = {"$group" : {
               "_id" : "$day", 
               "avg_d" : {"$avg" : "$download"},
               "avg_u" : { "$avg" : "$upload"}}}
      aggregate = self.col.aggregate([ project , group ])
      return aggregate

   def test(self):
      '''tests mongo connection'''
      db = self.connection.test
      cursor = db.test.find()
      stuff = [document for document in cursor]
      return stuff

   def add_date_now(self, doc):
     '''adds the date now'''
     doc['date'] = datetime.datetime.utcnow()
     return doc

   def update_speed(self, doc):
      '''updates document'''
      doc = self.add_date_now(doc)
      doc = self.col.insert(doc)
      return doc

   def get_date(self, speed, direction='Download'):
      '''returns a date if given a speed assumes speed is download unless direction="Upload"'''
      cursor = self.col.find({direction: speed},{"_id":False,"date":True})
      date = cursor.next()['date']
      return str(date)

   def get_aggregate(self):
      '''aggregates speed, accepts upload/download as argument'''
      aggregation_object = {
                     "$group" : {
                        "_id"    : "Aggregate",
                        "Average download" : {"$avg" : "$Download"},
                        "Average upload" : {"$avg" : "$Upload"},
                        "Max Download" : {"$max" : "$Download"},
                        "Max Upload" : {"$max" : "$Upload"},
                        "Min Download" : {"$min" : "$Download"},
                        "Min Upload" : {"$min" : "$Upload"}
                                }
                           }
      average = self.col.aggregate(aggregation_object)
      return average

   def average_time(self):
      '''aggregates speed according to the hour in the day'''
      aggregation_object = {
                     "$group" : {
                        "_id"   : {"$hour":"$date"},
                        "download" : {"$avg":"$Download"},
                        "upload": {"$avg" : "$Upload"}
                                }
                           }
      average_time = self.col.aggregate(aggregation_object)
      return average_time


   def last_40(self):
     sort = [("date", -1)]
     find_filter = {"_id":0}
     limit = 40
     cursor = self.col.find({},find_filter).sort(sort).limit(limit)
     most_recent = {}
     for i in range(40,0,-1):
        most_recent[i] = cursor.next()
        most_recent[i]["date"] = most_recent[i]["date"].hour * 100 + most_recent[i]["date"].minute
     return most_recent
     
