import csv
import re
#from matplotlib import pyplot as plt
nyc_zips = []
# Open and load neighborhoods information
with open('NYNeighborhoods.csv', 'rb') as csvfile:
    zip_list = csv.reader(csvfile) # add as list to prevent None keys, due to multiple ZIPs
    zip_list.next() # skip header
    for row in zip_list:
        for i in range(2, len(row)):
            nyc_zips.append(row[i])
    print 'Zip Codes Loaded.'
    nyc_zips.sort()
    print 'Zip Codes Sorted.'


nyc_zip_dict = {k: [] for k in nyc_zips} # create dictionary with NYC Zips as keys; cannot use .fromkeys because it appends the same list to every key
# Open and search for tracts belonging to each zipcode
with open('nhgis0001_csv/zcta_tract_rel_10.txt', 'rb') as csvfile:
    zcta_relations = csv.reader(csvfile) # load into temporary var
    zcta_relations.next() # skip header
    for row in zcta_relations:
        if row[0] in nyc_zip_dict: # if zip (zcta5 code) matches a key, append the tract code
            nyc_zip_dict[row[0]].append(row[3])
    print 'Tracts have been assigned to ZIP codes.'

# Open and write a new csv containing the equivalencies
with open('nyc_zip_tract_relations.csv', 'wb'): pass # clears file so it doesn't get need to be deleted
with open('nyc_zip_tract_relations.csv', 'wb') as writer:
    zctatract = csv.writer(writer) # add as list to prevent None values
    for key, value in nyc_zip_dict.iteritems():
        zctatract.writerow([key,value])

print 'Zip-Tract Relations now saved!'    
