#ONE TIME USE SCRIPT

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starships.settings')

import django
django.setup()

from ships.models import *

def populate():
  f = file('starships.csv')
  l = f.readline() # discard top line
  l = f.readline()[:-1]
  while l != "":
    print l
    sa = []
    c = ""
    b = False
    for i in l:
      if i == '\"':
        b = not b
      elif i == ',' and not b:
        sa += [c]
        c = ""
      else:
        c += i
    sa += [c]
    print sa
    s = add_ship(sa)
    print s.to_json()
    print l
    l = f.readline()

def add_ship(sa):
  s = Ship.objects.create(name = sa[0])
  s.setup(sa)
  s.manufacturer = sa[1]
  s.cost_in_credits = sa[2]
  s.length = sa[3]
  s.max_atmosphering_speed = sa[4]
  s.cargo_capacity_kg = sa[5]
  s.hyperdrive_rating = sa[6]
  s.docking_station_latitide = sa[7]
  s.docking_station_longitude = sa[8]
  return s

populate()
