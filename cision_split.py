#starting the proecss of breaking the media data into a one sheet.  this sheet is going to have
#media name, city, and state to start with.  
#at some point I will have to break this up into newspaper, tv, radio, and digital but that is not he first step.
# the first step is breaking out the city name from the ones where they are combine in one cell


import pandas as pd
import csv


media_name = []
media_city = []

remove = '–'
remove_1 = ' - '
remove_2 = '--'
remove_3 = '——'
remove_4 = ' —— '
with open('All_Media.csv') as csvfile:
	for row in csv.reader(csvfile):
		if remove in row[1]:
			#print(row[1])
			splitting = row[1].split(remove)
			#print(splitting[0])
			media_name.append(splitting[0])
			media_city.append(splitting[1])

		elif remove_1 in row[1]:
			#print(row[1])
			splitting = row[1].split(remove_1)
			#print(splitting[1])
			media_name.append(splitting[0])
			media_city.append(splitting[1])

		elif remove_2 in row[1]:
			#print(row[1])
			splitting = row[1].split(remove_2)
			#print(splitting[1])
			media_name.append(splitting[0])
			media_city.append(splitting[1])

		elif remove_3 in row[1]:
			#print(row[1])
			splitting = row[1].split(remove_3)
			#print(splitting[1])
			media_name.append(splitting[0])
			media_city.append(splitting[1])
			
		elif remove_4 in row[1]:
			#print(row[1])
			splitting = row[1].split(remove_4)
			print(splitting[1])
			media_name.append(splitting[0])
			media_city.append(splitting[1])



		else:
			media_name.append(row[1])
			media_city.append(row[2])



print(len(media_name))
print(len(media_city))

#df = pd.DataFrame({'media_name':media_name,'media_city':media_city})
#df.to_csv('cision_media_first_split.csv')
