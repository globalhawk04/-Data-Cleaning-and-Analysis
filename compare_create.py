import pandas as pd
import csv

#https://stackoverflow.com/questions/14657241/how-do-i-get-a-list-of-all-the-duplicate-items-using-pandas-in-python


#ok, so i started this by pulling organic key words by indiviual school dropping dublicates then combining eveverthing into 
#one list and pulling duplicates out of that list to create one main list of words that are common among the group
#now i can actually pull the data differently and get this list a different way.  i think the main concern will be muliple returns
# on the a&m side but for some reason i think that the way the data is being returned it may cancel it out.
#either way i think i have the majority of that stuff figured out.
# what i need to do now is create a tagging method for land grant sec texas schools along with desktop mobile and ads
# this is the only way i will be able to create one main list to compare everything.  i need this list because ultimately
# what i am looking for is a hierachry of words:

# 1.  words associated across all of the schools and platforms
# 2.  words associate across all schools by platform
# 3,  words that assoicate with schools across region and platforms
# 4.  words that associate with schools by platform
# 5.  words that associate between a school and a&m

# this allows me to target:
# 1.  individual schools vs a&m
# 2. region vs a&m
# 3.  all schools vs a&m (or this biggest grouping possible)

# the moon shot goal being words that cut across mobile and desktop 

# data used:  SEM Rush Keyword gap tool.  This tool allows me to compare a&m to other schools organic and paid key
# words across mobile and desktop

# this is very important because by knowing what keywords cut across domains and who we are cometiing with allows
# for better descsions in terms of creating an economic strategy for digital advertisment moving forward


files = ['baylordd','ricedd','shsudd','smudd','tamudd','tcudd','txstdd','uhdd','utexasdd']

keyword = []
position = []
search_vol = []
url = []
dupp = []
double = []
schoolname = []
for x in files:
#opens the file name and reads
	with open(x+'.csv', 'r') as csvfile:
		datareader = csv.reader(csvfile)
		for row in datareader:
			keyword.append(row[1])
			position.append(row[2])
			search_vol.append(row[4])
			url.append(row[7])
			schoolname.append(x)


df = pd.DataFrame({'school':schoolname,'keyword':keyword,'position':position,'search_vol':search_vol,'url':url})


df.to_csv('Combined_List_of_All_Organic_Keyword_data.csv') 

df3 = pd.concat(g for _, g in df.groupby("keyword") if len(g) > 1)
# it would be really really smart to get a better understanding of this one liner above
#df3.to_csv('texas_org_comp.csv')
