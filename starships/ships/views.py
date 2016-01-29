from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Ship

def index(request):
  s = []
  for ship in Ship.objects.all():
    s += [ship]
  context = {'ships':s}
  return render(request, 'ships/index.html', context)

def api(request):
  ships_per_page = 25
  paginator = Paginator(Ship.objects.all(), ships_per_page)
  page = request.GET.get('page')
  if "page" in request.path.split('/')[-1] and (page == 1 or page == None):
    try: 
      page = int(request.path.split('/')[-1].split('=')[1])
    except ValueError:
      page = 1
  slist = []
  print page
  try:
    slist = paginator.page(page)
  except PageNotAnInteger:
    slist = paginator.page(1)
  except EmptyPage:
    slist = paginator.page(paginator.num_pages)
  ret = '{\"ships\":['
  print request.path
  for ship in slist.object_list:
    ret += ship.to_json() + ','
  ret = ret[:-1] + ']}'
  return HttpResponse(ret)
