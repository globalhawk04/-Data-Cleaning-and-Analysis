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

'''
files = ['baylor-m','rice-m','shsu-m','smu-m','sfa-m','tcu-m','txst-m','uh-m',
		'ut-m','ttu-m','baylor-d','rice-d','shsu-d','smu-d','sfa-d','tcu-d',
		'txst-d','uh-d','ut-d','ttu-d',
		'ufl-m','uga-m','uky-m','utk-m','vander-m','ark-d','au-d','lsu-d','mizzo-d','msstat-d',
		'olemiss-d','sc-d','ua-d','ufl-d','uga-d','uky-d','utk-d','vander-d',
		'arz-m','cal-m','clem-m','col-m','corn-m','ia-m','ill-m','kstate-m','msu-m',
		'okstate-m','org-m','osu-m','psu-m','unl-m','usu-m','vt-m','wisc-m','wvu-m',
		'arz-d','cal-d','clem-d','col-d','corn-d','ia-d','ill-d','kstate-d','msu-d',
		'okstate-d','org-d','osu-d','psu-d','unl-d','usu-d','vt-d','wisc-d','wvu-d']
'''
		
#files = ['ark-m','au-m','lsu-m','mizzo-m','msstat-m','olemiss-m','sc-m','ua-m','ufl-m','uga-m','uky-m','utk-m','vander-m','ark-d','au-d','lsu-d','mizzo-d','msstat-d','olemiss-d','sc-d','ua-d','ufl-d','uga-d','uky-d','utk-d','vander-d']
#files = ['arz-m','cal-m','clem-m','col-m','corn-m','ia-m','ill-m','kstate-m','msu-m','okstate-m','org-m','osu-m','psu-m','unl-m','usu-m','vt-m','wisc-m','wvu-m','arz-d','cal-d','clem-d','col-d','corn-d','ia-d','ill-d','kstate-d','msu-d','okstate-d','org-d','osu-d','psu-d','unl-d','usu-d','vt-d','wisc-d','wvu-d']
#files = ['Land_Grant_Schools_All_Keyword','SEC_Schools_All_Keyword','Texas_Schools_All_Keyword']



files = ['All_Schools_All_Keyword']


keyword = []
position = []
position1 = []
search_vol = []
url = []
url1 = []
schoolname = []
schoolname1 = []
for x in files:
#opens the file name and reads
	with open(x+'.csv', 'r') as csvfile:
		datareader = csv.reader(csvfile)
		for row in datareader:
			#if 'anthropology' or 'science' or 'atmospheric sciences' or 'biology' or 'chemistry' or 'communications' or 'journalism' or 'economics' or 'english' or 'geograhpy' or 'geology' or 'geophysics' or 'global languages' or 'cultures' or 'history' or 'mathematics' or 'oceanography' or 'philosophy' or 'humanities' or 'physics' or 'astronomy' or 'brain sciences' or 'sociology' or 'statistics' in row[3]:
			if 'anthropology' in row[3]:
				keyword.append(row[3])
				position.append(row[4])
				position1.append(row[5])
				search_vol.append(row[6])
				url.append(row[7])
				url1.append(row[8])
				schoolname.append('tamu')
				schoolname1.append(x)
			if 'journalism' in row[3]:
				keyword.append(row[3])
				position.append(row[4])
				position1.append(row[5])
				search_vol.append(row[6])
				url.append(row[7])
				url1.append(row[8])
				schoolname.append('tamu')
				schoolname1.append(x)
			if 'atmospheric sciences' in row[3]:
				keyword.append(row[3])
				position.append(row[4])
				position1.append(row[5])
				search_vol.append(row[6])
				url.append(row[7])
				url1.append(row[8])
				schoolname.append('tamu')
				schoolname1.append(x)
			if 'biology' in row[3]:
				keyword.append(row[3])
				position.append(row[4])
				position1.append(row[5])
				search_vol.append(row[6])
				url.append(row[7])
				url1.append(row[8])
				schoolname.append('tamu')
				schoolname1.append(x)
			if 'communications' in row[3]:
				keyword.append(row[3])
				position.append(row[4])
				position1.append(row[5])
				search_vol.append(row[6])
				url.append(row[7])
				url1.append(row[8])
				schoolname.append('tamu')
				schoolname1.append(x)
			if 'global languages' in row[3]:
				keyword.append(row[3])
				position.append(row[4])
				position1.append(row[5])
				search_vol.append(row[6])
				url.append(row[7])
				url1.append(row[8])
				schoolname.append('tamu')
				schoolname1.append(x)


df = pd.DataFrame({'school':schoolname,'school_compare':schoolname1,'keyword':keyword,'position':position,'position_compare':position1,'search_vol':search_vol,'url':url,'url_compare':url1})
#df.to_csv('comeon.csv')

#keywords = ['anthropology', 'atmospheric sciences','biology','chemistry']

df3 = pd.concat(g for _, g in df.groupby("keyword") if len(g) > 6)
# it would be really really smart to get a better understanding of this one liner above
df3.to_csv('key_compare.csv')

# consider a list
#list1 = ['anthropology', 'priyank']

# check the pandas name column
# contain the given list if strings
#print(data[data['keyword'].isin(list1)])

#x.to_csv('comeon.csv')

# consider a list
#list2 = ['anthropology']

# check the pandas subjects column
# contain the given list if strings
#x  = data[~numpy.isin(data['keyword'], list2)]


