# data-inc
The New York Philharmonic (NY Phil) has a rich data set of subscriber information available publicly (http://archives.nyphil.org/index.php/open-data) that
spans from 1883 - Present. A subscription is a pre-purchased set of tickets that typically spans an entire season and usually will guarantee a specific seat
for all performances. As a non-profit organization, it would be extremely beneficial for the  NY Phil to be  able to determine who would be likely to become
a subscriber.

 I plan to create a logistic regression model to determine how likely a given person is to purchase a subscription. My goal is to combine the open data
 subscribers database with information from the Census and American Communities Survey to determine  which attributes (income, location, education, etc.)
 are likely to act as predictors for the NY Phil. In addition, I would like to create a map showing how the addresses of subscribers has changed over time.

 In the course of EDA, I found a couple of interesting things regarding the locations from the 1958-1980 data subset. In the Visualizations folder there are two
 key figures: Subscriptions by Decade, which shows how many subscribers hailed from each of the five boroughs, and Difference by Decade, which shows the
 change in the average number of subscriptions in each of the boroughs as each decade has changed. Of interest is the large outflux from Manhattan in the
 1970s and 80s. (It might be related to the crime rates during the same time period.)

 Currently, I've had to limit the scope of the project due to some data constraints. The Census data is only available digitally from the 2000 and 2010 censuses.
 In addition, the subscribers database lists different information for each time period, ranging from full address to just ZIP codes. This imposes a further restriction
 in comparisons since the Census bureau created ZCTAs (Zip Code Tabulation Areas) for the first time in 2000 and there are differences between the ZCTAs from
 2000 and those from 2010. The ZTCAs roughly map census tracts to ZIP codes.
