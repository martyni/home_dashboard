import requests
import bs4
from pprint import pprint

class Bus_Times(object):
   def __init__(self,url="http://www.tfl.gov.uk/bus/stop/490015531T/camden-town-station-bayham-street/"):
      self.url = url
      self.station = url.split('/')[-2]
      self.site = requests.get(self.url)
      self.soup = bs4.BeautifulSoup(self.site.content) 
      self.raw_timetable = [i for i in self.soup.find_all("li",{"class":"live-board-feed-item"})]
      self.bus_times = []
      for time in self.raw_timetable:
         try:
            self.bus_times.append({
            'bus': time.find('span',{'class':'live-board-route'}).contents[0].split()[0],
            'destination': time.find('span', {'class':'train-destination'}).contents[0],
            'eta' : time.find('span', {'class':'live-board-eta'}).contents[0]
                      }
                     )
         except:
            pass
   def print_times(self):
      pprint(self.bus_times)

if __name__=="__main__":
   my_times = Bus_Times()
   my_times.print_times()

