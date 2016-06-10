<<<<<<< HEAD
import csv
import re
from matplotlib import pyplot as plt
neighborhood_zips = {}
# Open and load neighborhoods information
with open('NYNeighborhoods.csv', 'rb') as csvfile:
    neighborhood_list = csv.reader(csvfile) # add as list to prevent None keys, due to multiple ZIPs
    neighborhood_list.next() # skip header
    for row in neighborhood_list:
        if row[1] in neighborhood_zips: # if neighborhood is in the dict, add new ZIPs
            for i in range(2, len(row)): # REMOVED len(row) - 1, seemed to be chopping off the last zip in each set in CensusMap.py
                neighborhood_zips[row[1]].append(row[i])
        else: # if borough is new, add it as key, then add all the associated ZIPs in the row
            neighborhood_zips[row[1]] = [row[2]]
            if len(row) > 3:
                for i in range(3, len(row) - 1):
                    neighborhood_zips[row[1]].append(row[i])
    print 'Neighborhood List Initialized.'

borough_neighborhoods = {}
# Open and load neighborhoods information
with open('NYNeighborhoods.csv', 'rb') as csvfile:
    neighborhood_list = csv.reader(csvfile) # add as list to prevent None keys, due to multiple ZIPs
    neighborhood_list.next() # skip header
    for row in neighborhood_list:
        if row[0] in borough_neighborhoods: # if borough is in the dict, add new ZIPs
            borough_neighborhoods[row[0]].append(row[1])
        else: # if borough is new, add it as key, then add all the associated ZIPs in the row
            borough_neighborhoods[row[0]] = [row[1]]
    print 'Borough List Initialized.'

# Open and write a new csv containing the equivalencies
with open('nyc_neighborhood_zip_relations.csv', 'wb'): pass # clears file so it doesn't get need to be deleted
with open('nyc_neighborhood_zip_relations.csv', 'wb') as writer:
    neighborhood_zip_list = csv.writer(writer) # add as list to prevent None values
    for key, value in neighborhood_zips.iteritems():
        neighborhood_zip_list.writerow([key,value])

print 'Neighborhood-Zip Relations now saved!'


# Open and write a new csv containing the equivalencies
with open('nyc_borough_neighborhood_relations.csv', 'wb'): pass # clears file so it doesn't get need to be deleted
with open('nyc_borough_neighborhood_relations.csv', 'wb') as writer:
    borough_neighborhood_list = csv.writer(writer) # add as list to prevent None values
    for key, value in borough_neighborhoods.iteritems():
        borough_neighborhood_list.writerow([key,value])

print 'Neighborhood-Zip Relations now saved!'
=======
import csv
import re
from matplotlib import pyplot as plt
neighborhood_zips = {}
# Open and load neighborhoods information
with open('NYNeighborhoods.csv', 'rb') as csvfile:
    neighborhood_list = csv.reader(csvfile) # add as list to prevent None keys, due to multiple ZIPs
    neighborhood_list.next() # skip header
    for row in neighborhood_list:
        if row[1] in neighborhood_zips: # if neighborhood is in the dict, add new ZIPs
            for i in range(2, len(row)): # REMOVED len(row) - 1, seemed to be chopping off the last zip in each set in CensusMap.py
                neighborhood_zips[row[1]].append(row[i])
        else: # if borough is new, add it as key, then add all the associated ZIPs in the row
            neighborhood_zips[row[1]] = [row[2]]
            if len(row) > 3:
                for i in range(3, len(row) - 1):
                    neighborhood_zips[row[1]].append(row[i])
    print 'Neighborhood List Initialized.'

borough_neighborhoods = {}
# Open and load neighborhoods information
with open('NYNeighborhoods.csv', 'rb') as csvfile:
    neighborhood_list = csv.reader(csvfile) # add as list to prevent None keys, due to multiple ZIPs
    neighborhood_list.next() # skip header
    for row in neighborhood_list:
        if row[0] in borough_neighborhoods: # if borough is in the dict, add new ZIPs
            borough_neighborhoods[row[0]].append(row[1])
        else: # if borough is new, add it as key, then add all the associated ZIPs in the row
            borough_neighborhoods[row[0]] = [row[1]]
    print 'Borough List Initialized.'

# Open and write a new csv containing the equivalencies
with open('nyc_neighborhood_zip_relations.csv', 'wb'): pass # clears file so it doesn't get need to be deleted
with open('nyc_neighborhood_zip_relations.csv', 'wb') as writer:
    neighborhood_zip_list = csv.writer(writer) # add as list to prevent None values
    for key, value in neighborhood_zips.iteritems():
        neighborhood_zip_list.writerow([key,value])

print 'Neighborhood-Zip Relations now saved!'


# Open and write a new csv containing the equivalencies
with open('nyc_borough_neighborhood_relations.csv', 'wb'): pass # clears file so it doesn't get need to be deleted
with open('nyc_borough_neighborhood_relations.csv', 'wb') as writer:
    borough_neighborhood_list = csv.writer(writer) # add as list to prevent None values
    for key, value in borough_neighborhoods.iteritems():
        borough_neighborhood_list.writerow([key,value])

print 'Neighborhood-Zip Relations now saved!'
>>>>>>> 921ead7ebe3a2bb2cf257abdb6137c2373ae5474
