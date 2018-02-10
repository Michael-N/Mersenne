import pp
'''
import urllib
import json
'''
#code to run

import math
#Computation to Run
def mers_list(range_open,range_close):
    def is_prime(numArg):
        num = int(numArg)
        x = int(math.ceil(math.sqrt(num)) + 1)

        for numToChk in range(2,x ):
            print("[Test %s]  Iterating %s modulo %s "%(str(numToChk),str(num),str(numToChk)))
            if num % numToChk == 0:
                return False
        return True

    primes = []
    test_list = range(range_open, range_close)
    test_odds = [item for item in test_list if item % 2 ==1]

    for item in test_odds:
        #print("IN LOOP")
        if is_prime(item) == True:
            primes.append(item)
    #print(str(len(primes)) + " primes found!")
    return primes
def range_dist(r_open, r_close, n_dist):
    pre_range = []
    pre_range.extend(range(r_open,r_close))

    length = len(pre_range)
    each_length = int(length/n_dist)
    final_length = int(each_length+(length%n_dist))

    #for debugging
    """
    print("size of range=")
    print(str(length))

    print("length of each dist except final")
    print(str(each_length))

    print("length of final")
    print(str(final_length))
    """
    #creates distributions lists withing list_of_dists
    list_of_dists = []
    for i  in range(1,n_dist+1):
        list_of_dists.append([])

    #calculates all distributions to lists except final
    initial = r_open
    for i in range(0,n_dist-1):
        for x in range(initial, initial+each_length):
            if x == initial:
                list_of_dists[i].extend([x])
            elif x == (initial+each_length-1):
                list_of_dists[i].extend([x+1])
        initial += each_length

    #calculates final distribution of range / n_dist + remainder
    for x in range(initial, initial+final_length):
        if x == initial:
            list_of_dists[n_dist-1].extend([x])
        elif x == (initial+final_length-1):
            list_of_dists[n_dist-1].extend([x+1])
    return list_of_dists
#settings:
settingsUrl = ""

#fetch settings
'''
print("[Fetching settings from %s]"%settingsUrl)
settingsJson = urllib.request.urlopen(settingsUrl)
settingsText = settingsJson.read()
settingsData = json.loads(settingsText)
print("[Loaded settings from %s]"%settingsUrl)
'''
#Create the connections:
ppservers=("192.168.1.84:35000", "192.168.1.73:35000")
job_server = pp.Server(ppservers=ppservers, secret='abc123')#settingsData.secret
print("[Created Distributrion Server]")

#Submit the Jobs
allPartitions = []
splitRanges = range_dist(1,200000,len(ppservers))
for j in range(0,len(ppservers)):
    allPartitions.append(job_server.submit(mers_list,args=(splitRanges[j][0],splitRanges[j][1]),modules=("math","datetime")))
print("[Created Partitions and sent the tasks for Computation]")

#Get and print the data


print('[Waiting...]')
for i in range(0,len(allPartitions)):
    getData = allPartitions[i]
    dataPartition = getData()
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("[Data]:%s" % str(dataPartition))
