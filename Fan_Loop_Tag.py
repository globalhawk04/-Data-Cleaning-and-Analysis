import pandas as pd
import csv


file_main = ['name of main file']
file_tag = ['name of file with tags.csv']

tag = []

#open file with the tags in it
with open('file_tag', 'r') as csvfile:
	datareader = csv.reader(csvfile)
	for row in datareader:
		tag_lst = [row[0],row[1]]
		tag.append(tag_lst)

#open main list
 with open(file, 'r') as csvfile:
 	datareader = csv.reader(csvfile)
 	#looping through main list
	for name in datareader:
		#looping through list of tags
		for tagged in tag:
			#if names match then append tag
			if tagged[0] in row[0]:
				#creating new list
				things.append(tagged[1])
				#then the rest of the stuff you are looking to get specifically name and address


#creating dataframe
df = pd.DataFrame({'tag':tag,'tags':comp_tag,'school':schoolname,
				'school_compare':schoolname1,'keyword':keyword,'position':position,
				'position_compare':position1,'search_vol':search_vol,'url':url,'url_compare':url1})

##Should run sum regression here with purchase price as the dependent variable
#This would be good just to check if the promotion code matters 


#dumpting to csv and creating file 
df.to_csv('comp_tag_url.csv')




