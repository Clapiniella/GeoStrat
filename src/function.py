from pymongo import MongoClient

def diHola():
    return ' Clara'

def connectCollection(database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll

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