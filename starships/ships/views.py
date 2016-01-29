from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import math
from .models import Ship

def index(request):
  s = []
  if len(request.path.split('/')) > 1:
    log = 0
    lat = 0
    st = ""
    latt = False
    cc = 0
    for i in request.path.split('/')[-1]:
      if i == ':':
        if st == "lat":
          latt = True
        st = ""
      elif i == ',':
        cc += 1
        if latt:
          lat = float(st)
          latt = False
        else:
          log = float(st)
        st = ""
        if cc == 2:
          break
      elif i not in "1234567890" and (len(st) > 0) and st[-1] in "1234567890":
        if latt:
          lat = float(st)
        else:
          log = float(st)
        st = "" + i
      else:
        st += i
    if latt:
      lat = float(st)
    coords = [lat,log]
    s = sort_by_distance(Ship.objects.all(), coords)
  else:
    for ship in Ship.objects.all():
      s += [ship]
  context = {'ships':s}
  return render(request, 'ships/index.html', context)

def api(request):
  ships_per_page = 25
  search = {}
  if "search" == request.path.split('/')[-1][:6]:
    if "coords=" in request.path.split('/')[-1]:
      s = request.path.split('/')[-1].split("coords=")
      log = 0
      lat = 0
      st = ""
      latt = False
      cc = 0
      for i in s[1]:
        if i == ':':
          if st == "lat":
            latt = True
          st = ""
        elif i == ',':
          cc += 1
          if latt:
            lat = float(st)
            latt = False
          else:
            log = float(st)
          st = ""
          if cc == 2:
            break
        elif i not in "1234567890" and (len(st) > 0) and st[-1] in "1234567890":
          if latt:
            lat = float(st)
          else:
            log = float(st)
          st = "" + i
        else:
          st += i
      if latt:
        lat = float(st)
      search['coords'] = [lat,log]
      print search['coords']
  paginator = Paginator(Ship.objects.all(), ships_per_page)
  if 'coords' in search.keys():
    paginator = Paginator(sort_by_distance(Ship.objects.all(), search['coords']), ships_per_page)
  page = request.GET.get('page')
  if ("page" in request.path.split('/')[-1] or "page" in request.path.split('/')[-2]) and (page == 1 or page == None):
    print 'page'
    try:
      if "page" in request.path.split('/')[-1]:
        page = int(request.path.split('/')[-1].split('=')[1])
      else:
        page = int(request.path.split('/')[-2].split('=')[1])
    except ValueError:
      page = 1
  slist = []
  try:
    slist = paginator.page(page)
  except PageNotAnInteger:
    slist = paginator.page(1)
  except EmptyPage:
    slist = paginator.page(paginator.num_pages)
  ret = '{\"ships\":['
  for ship in slist.object_list:
    ret += ship.to_json() + ','
  ret = ret[:-1] + ']}'
  return HttpResponse(ret)

def distance(lat1, long1, lat2, long2):
  degrees_to_radians = math.pi/180.0
  phi1 = (90.0 - lat1)*degrees_to_radians
  phi2 = (90.0 - lat2)*degrees_to_radians
  theta1 = long1*degrees_to_radians
  theta2 = long2*degrees_to_radians
  cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
  math.cos(phi1)*math.cos(phi2))
  arc = math.acos( cos )
  return arc

def sort_by_distance(ships, coords):
  ret = []
  ret += [ships[0]]
  for s in ships[1:]:
    d = distance(s.docking_station_latitide, s.docking_station_longitude, coords[0], coords[1])
    for i in range(len(ret)):
      if distance(ret[i].docking_station_latitide, ret[i].docking_station_longitude, coords[0], coords[1]) > d:
        ret = ret[:i] + [s] + ret[i:] # if time, make into binary tree
        break
      elif i == len(ret) - 1:
        ret += [s]
  return ret
