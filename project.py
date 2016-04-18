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
            for i in range(2, len(row) - 1):
                neighborhood_zips[row[0]].append(row[i])
        else: # if borough is new, add it as key, then add all the associated ZIPs in the row
            neighborhood_zips[row[0]] = [row[2]]
            if len(row) > 3:
                for i in range(3, len(row) - 1):
                    neighborhood_zips[row[0]].append(row[i])
    print 'Neighborhood List Initialized.'

#define subscribers_lists
subscribers_list_1950_1959 = {}
subscribers_list_1960_1969 = {}
subscribers_list_1970_1979 = {}
subscribers_list_1980_plus = {}

#define zip_search method
def  zip_search(decade):
    zipcode = re.search('\d{5}', row['Final Address']) # looks for any 5 digit numbers at the end of the Final Address Column
    if zipcode is not None: #if there is an address given, this converts it from a location to the string
        zipcode = zipcode.group(0)
        decade[zipcode] = decade.get(zipcode, 0) + 1 #adds one to the matching key
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
#compress datasets into larger bins: zips to boroughs, for graph readability
subscribers_by_borough_50s = {}
subscribers_by_borough_60s = {}
subscribers_by_borough_70s = {}
subscribers_by_borough_80s = {}

def borough_count(subscribers_list, decade):
    decade['Out of NYC'] = 0
    for zipcode_key, count in subscribers_list.iteritems():
        for borough, zipcode_list in neighborhood_zips.iteritems():
            if zipcode_key in zipcode_list:
                decade[borough] = decade.get(borough, 0) + subscribers_list[zipcode_key]
            elif zipcode_key not in zipcode_list:
                decade['Out of NYC'] += 1
            else:
                print 'Error!'
    return decade

borough_count(subscribers_list_1980_plus, subscribers_by_borough_80s)
borough_count(subscribers_list_1970_1979, subscribers_by_borough_70s)
borough_count(subscribers_list_1960_1969, subscribers_by_borough_60s)
borough_count(subscribers_list_1950_1959, subscribers_by_borough_50s)
print 'Converted Zipcodes into Boroughs.'

subscribers_by_borough_50s.update((x, y) for x, y in subscribers_by_borough_50s.items())
subscribers_by_borough_60s.update((x, y / 9) for x, y in subscribers_by_borough_60s.items())
subscribers_by_borough_70s.update((x, y / 5) for x, y in subscribers_by_borough_70s.items())
subscribers_by_borough_80s.update((x, y) for x, y in subscribers_by_borough_80s.items())
print 'Determined Mean per Year in Each Borough.'
subscribers_by_borough_80s['Staten Island'] = 0

def diff_in_subs(final_decade, initial_decade):
    diff_in_subscribers = { k:int(final_decade.get(k, 0)) - int(initial_decade.get(k, 0)) for k in set(final_decade) | set(initial_decade)}
    return diff_in_subscribers

diff_in_subscribers_70_60 = diff_in_subs(subscribers_by_borough_70s, subscribers_by_borough_60s)
diff_in_subscribers_80_70 = diff_in_subs(subscribers_by_borough_80s, subscribers_by_borough_70s)
print diff_in_subscribers_70_60
print diff_in_subscribers_80_70

# def create_plot(decade, title):
#     xs = [i +0.1 for i,  _ in enumerate(decade.keys())]
#     plt.bar(xs, decade.values())
#     plt.ylabel('Mean Number of Subscriptions per Year')
#     plt.title('Geographic Location of NY Philharmonic Subscribers in '+ title)
#     plt.xticks([i + 0.5 for i, _ in enumerate(decade.keys())], decade.keys())
#     namepdf = '%s.pdf' % title
#     namepng = '%s.png' % title
#     plt.savefig(namepdf, format = 'pdf')
#     plt.savefig(namepng, format = 'png')
#     plt.show()
#
# create_plot(subscribers_by_borough_80s, '1980')
# create_plot(subscribers_by_borough_70s, 'the 1970s')
# create_plot(subscribers_by_borough_60s, 'the 1960s')
#
# def create_diff_plot(decade, title):
#     xs = [i +0.1 for i,  _ in enumerate(decade.keys())]
#     plt.bar(xs, decade.values())
#     plt.ylabel('Difference in Mean Number of Subscriptions per Year')
#     plt.title('Geographic Location of NY Philharmonic Subscribers in '+ title)
#     plt.xticks([i + 0.5 for i, _ in enumerate(decade.keys())], decade.keys())
#     namepdf = '%s.pdf' % title
#     namepng = '%s.png' % title
#     plt.savefig(namepdf, format = 'pdf')
#     plt.savefig(namepng, format = 'png')
#     plt.show()
#
#
# create_diff_plot(diff_in_subscribers_80_70, '1980 and 1970')
# create_diff_plot(diff_in_subscribers_70_60, '1970 and 1960')

#Create Plots!
import numpy as np
n_groups  = 6
y1 = subscribers_by_borough_60s.values()
y2 = subscribers_by_borough_70s.values()
y3 = subscribers_by_borough_80s.values()

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.3
opacity =1

p1 = plt.bar(index, y1, bar_width, color = 'r', alpha = opacity, label = '60s')
p2 = plt.bar(index + bar_width, y2, bar_width, color = 'b', alpha = opacity, label = '70s')
p3 = plt.bar(index+2*bar_width, y3, bar_width, color = 'g', alpha = opacity, label = '80s')

plt.ylabel('Mean Number of Subscriptions per Year')
plt.title('Geographic Location of NY Philharmonic Subscribers ')
plt.xticks(index + 1.5 * bar_width, ('Staten Island', ' Brooklyn', 'Bronx', 'Out of NYC', 'Manhattan', 'Queens'))
plt.legend()

plt.savefig('Subscriptions by Decade.png')
plt.savefig('Subscriptions by Decade.pdf')
plt.show()

fig, ax = plt.subplots()
p4 =  plt.bar(index, diff_in_subscribers_70_60.values(), bar_width, color = 'b', alpha = opacity, label = '70s - 60s')
p5 = plt.bar(index + bar_width, diff_in_subscribers_80_70.values(), bar_width, color = 'r', alpha = opacity, label = '80s - 70s')

plt.ylabel('Difference in Mean')
plt.title('Difference in Mean Number of Subscriptions per Year')
plt.xticks(index + bar_width, ('Staten Island', ' Brooklyn', 'Bronx', 'Out of NYC', 'Manhattan', 'Queens'))
plt.legend(loc=3)

plt.savefig('Difference by Decade.png')
plt.savefig('Difference by Decade.pdf')
plt.show()

print 'Analysis Complete!'
