#Approximation Algorithm
# USA Radio brodcast station select

states_needed=set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])    #brodcast stats list

stations={}    #select brodcast list. using hashtable
stations["kone"]=set(["id", "nv", "ut"])
stations["ktwo"]=set(["wa", "id", "mt"])
stations["kthree"]=set(["or", "nv", "ca"])
stations["kfour"]=set([ "nv", "ut"])
stations["kfive"]=set(["ca", "az"])

final_stations=set()    #final chose stations

while states_needed:
    best_station=None    #select to most area covered brodcast station
    states_coverd=set()    #save covered area
    for station, states in stations.items():    #python for sentence
        covered=states_needed & states    #new grammer(Intersection)
        if len(covered)>len(states_coverd):
            best_station=station
            states_coverd=covered

    states_needed-=states_coverd
    final_stations.add(best_station)
            
print(final_stations)
