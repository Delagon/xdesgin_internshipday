Running the server:
  Built using python 2.7, with the packages described in requirements.txt, use:
  $ pip install requirements.txt
  to get needed software
  To run the server use:
  $ python startships/manage.py runserver
  sever should contain all needed files in the database

Using the API:
  api returns upto 25 results per page
  string:
    ships/api/
      -Returns the first 25 ships
    ships/api/page=n
      -Returns the ships from 25*(n-1) to 25n
    ships/api/seach{coords=lat:x,long:y}
      -Returns the closest 25 ships to the point with a lattitiude of x and longatuide of y
    ships/api/page=n/search{coords=lat:x,long:y}
      -Returns the ships from 20*(n - 1) to 25n closest to the point descrubed by x and y
