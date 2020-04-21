from pymongo import MongoClient
import folium
from haversine import haversine
import googlemaps
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
import requests, json 
import time
import pandas as pd

def diHola(nombre):
    return 'Hola' + ' ' + nombre

client = MongoClient()
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

def geoquery(geoindex,distance,col):
    points= col.find(
        {"location": 
         {"$near": 
          {"$geometry":
           geoindex,
           "$maxDistance":distance
            }
        }
    })
    return list(points)

def mapping(coords,name,ic_type,ic_color,mapito):
    return folium.Marker(coords,
                        radius=1,popup=name,
                        icon=folium.Icon(icon=ic_type,color=ic_color), 
                       ).add_to(mapito)

def createDF(query):
    ind=[]
    name=[]
    category=[]
    descrip=[]
    lat=[]
    long=[]
    year=[]
    money_raised=[]
    for cia in range(len(query)):
        for office in range(len(query[cia].get('offices',0))):
            ind.append(query[cia].get('_id',0))
            name.append(query[cia].get('name',0))
            category.append(query[cia].get('category_code',0))
            descrip.append(query[cia].get('description',0))
            lat.append(query[cia].get('offices',0)[office].get('latitude'))
            long.append(query[cia].get('offices',0)[office].get('longitude'))
            year.append(query[cia].get('founded_year',0))
            money_raised.append(query[cia].get('total_money_raised',0))
    dic={"Id":ind,
         "name":name, 
         "category":category,
         "description":descrip,
         "lat":lat,
         "long":long,
         "year":year,
         "money_raised":money_raised}
    new_DF=pd.DataFrame(dic)
    return new_DF

def getcoord(query,lat,long):
    for que in query: 
        lat.append(que['location']['coordinates'][1])
        long.append(que['location']['coordinates'][0])
    return len(lat),len(long)   

def harver(elem,zipi):
    comparator=[]
    for a in zipi:
        comparator.append(haversine(elem,a))
    return min(comparator)

def nearbyAPI(location, radius, keyword):
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'keyword': keyword,
            'key': os.getenv("API_KEY")
        }
        res = requests.get(url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
        return places 

def search_places_by_input(query=''):
    # Search for a list of places in a city using places API from google.
    apiKey = os.getenv("API_KEY")
    endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    places = []
    params = {
        'query': input("Query: "),
        'key': apiKey
    }
    res = requests.get(endpoint_url, params = params)
    results = json.loads(res.content)
    print(results)
    places.extend(results['results'])
    time.sleep(2)
    while "next_page_token" in results:
        # Get the results from the 2nd and 3th page of the search in the API, with a total of 60 results.
        params['pagetoken'] = results['next_page_token'],
        res = requests.get(endpoint_url, params = params)
        results = json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
    return places

def createApiDf(query):
    name=[]
    long=[]
    lat=[]
    for location in query:
        for starbucks in location:
            name.append(starbucks['name'])
            long.append(starbucks['geometry']['location']['lng'])
            lat.append(starbucks['geometry']['location']['lat'])
    dic2={"name":name,"long":long,"lat":lat}
    lil_DF=pd.DataFrame(dic2)
    return lil_DF 

def getApiLoc(off):
    longitude = off['long']
    latitude = off['lat']
    loc=({
        'type':'Point',
        'coordinates':[longitude,latitude]
    })
    return loc