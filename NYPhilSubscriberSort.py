import csv
import re
from matplotlib import pyplot as plt
neighborhood_zips = {}
# Open and load neighborhoods information
with open('NYNeighborhoods.csv', 'rb') as csvfile:
    neighborhood_list = csv.reader(csvfile) # add as list to prevent None keys, due to multiple ZIPs
    neighborhood_list.next() # skip header
    for row in neighborhood_list:
        if row[0] in neighborhood_zips: # if borough is in the dict, add new ZIPs
            for i in range(2, len(row)): # REMOVED len(row) - 1, seemed to be chopping off the last zip in each set in CensusMap.py
                neighborhood_zips[row[0]].append(row[i])
        else: # if borough is new, add it as key, then add all the associated ZIPs in the row
            neighborhood_zips[row[0]] = [row[2]]
            if len(row) > 3:
                for i in range(3, len(row) - 1):
                    neighborhood_zips[row[0]].append(row[i])
    print 'Neighborhood List Initialized.'

#Call in neighborhoods and zip relations
neighborhoods = {}
with open('nyc_neighborhood_zip_relations.csv', 'rb') as csvfile:
    neighborhood_zip_relation = csv.reader(csvfile)
    neighborhoods = dict(neighborhood_zip_relation)

#call in borough and neighborhood relations
boroughs = {}
with open('nyc_borough_neighborhood_relations.csv', 'rb') as csvfile:
    borough_neighborhood_relation = csv.reader(csvfile)
    boroughs = dict(borough_neighborhood_relation)

#define subscribers_lists dictionaries
subscribers_list_1950_1959 = {}
subscribers_list_1960_1969 = {}
subscribers_list_1970_1979 = {}
subscribers_list_1980_plus = {}

#define zip_search method
def  zip_search(decade):
    zipcode = re.search('\d{5}', row['Final Address']) # looks for any 5 digit numbers at the end of the Final Address Column
    if zipcode is not None: #if there is an address given, this converts it from a location to the string
        zipcode = zipcode.group(0)
        for neighborhood, zips in neighborhoods.iteritems():
            if zipcode in zips:
                decade[neighborhood] = decade.get(neighborhood, 0) + 1 #adds one to the matching key
        return decade

#import subscribers' zipcodes from the dataset
with open('NewYorkPhilharmonicSubscribersDataset/NewYorkPhilharmonic_Subscribers_1953-1980.csv', 'rb') as csvfile:
    raw_subscribers_list = csv.DictReader(csvfile)
    for row in raw_subscribers_list:
        #segment data by decade and then count by zipcode
        if int(row['Year']) >=1950 and int(row['Year']) <= 1959:
            zip_search(subscribers_list_1950_1959)
        elif int(row['Year']) >= 1960 and int(row['Year']) <= 1969:
            zip_search(subscribers_list_1960_1969)
        elif int(row['Year']) >=  1970 and int(row['Year']) <= 1979:
            zip_search(subscribers_list_1970_1979)
        elif int(row['Year']) >= 1980:
            zip_search(subscribers_list_1980_plus)
        else:
            print 'Error!'
print 'Sorted by Decade.'


neighborhood_by_borough_50s = {k: {} for k in boroughs.keys()}
neighborhood_by_borough_60s = {k: {} for k in boroughs.keys()}
neighborhood_by_borough_70s = {k: {} for k in boroughs.keys()}
neighborhood_by_borough_80s = {k: {} for k in boroughs.keys()}

def borough_count(subscribers_list, decade):
    for neighborhood_key, count in subscribers_list.iteritems():
        for borough, neighborhood in boroughs.iteritems():
            if neighborhood_key in neighborhood:
                decade[borough][neighborhood_key] = count
            return decade

borough_count(subscribers_list_1980_plus, neighborhood_by_borough_80s)
borough_count(subscribers_list_1970_1979, neighborhood_by_borough_70s)
borough_count(subscribers_list_1960_1969, neighborhood_by_borough_60s)
borough_count(subscribers_list_1950_1959, neighborhood_by_borough_50s)
print 'Converted Zipcodes into Boroughs.'
#
# print neighborhood_by_borough_50s
# print neighborhood_by_borough_60s
# print neighborhood_by_borough_70s
# print neighborhood_by_borough_80s


neighborhood_by_borough_50s.update((x,y) for x, y in neighborhood_by_borough_50s.items())
neighborhood_by_borough_60s.update((x, y / 9) for x, y in neighborhood_by_borough_60s.items())
neighborhood_by_borough_70s.update((x, y / 5) for x, y in neighborhood_by_borough_70s.items())
neighborhood_by_borough_80s.update((x, y) for x, y in neighborhood_by_borough_80s.items())
print 'Determined Mean per Year in Each Borough.'
#
#
# def diff_in_subs(final_decade, initial_decade):
#     diff_in_subscribers = { k:int(final_decade.get(k, 0)) - int(initial_decade.get(k, 0)) for k in set(final_decade) | set(initial_decade)}
#     return diff_in_subscribers
#
# diff_in_subscribers_70_60 = diff_in_subs(neighborhood_by_borough_70s, neighborhood_by_borough_60s)
# diff_in_subscribers_80_70 = diff_in_subs(neighborhood_by_borough_80s, neighborhood_by_borough_70s)
# print diff_in_subscribers_70_60
# print diff_in_subscribers_80_70
