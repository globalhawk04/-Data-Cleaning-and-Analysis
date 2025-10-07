import pandas as pd
import csv
from itertools import islice


'''
#the purpose of this code is to grab and tag events related urls to add traffic measure as a % of total traffic

# this means I am going to need the following:

sport_name = ['football', 'softball','baseball','basketball','nsc','run','soccer','swimming']

tag = []

x = ['a','z','gg','as']

y = ['football','softball','basketball']

for loop in sport_name:
#for looping in y:
	if loop not in y:
		#print('yes')
		tag.append('none')
	else:
		#print(loop)
		tag.append(loop)

print(tag)
print(len(tag))



'''

#sport_name = []
sport_name = ['fleet','errorpages','mobility','mis','parking','about','alternative','transit','events','football', 'softball','baseball','basketball','nsc','funrun','soccer','swimming','news']
#sport_name = ['events']
#sport_name = ['news']
tag = []
y = []
page = []
page_view = []
unique = []
avg_time = []
entrance = []
bounce = []
exit = []
all_page_view = []
all_bounce = []
all_avg_time = []
all_unique = []

with open('transport_main.csv', 'r') as csvfile:
	for row in (csv.reader(csvfile)):
		all_page_view.append(int(row[1]))
		all_bounce.append(float(row[5]))
		all_avg_time.append(float(row[3]))
		all_unique.append(float(row[2]))
		for loop in sport_name:
			#print(row[1])
		#for looping in y:
			if loop in row[0].lower():
				#print(row[0])
				#pass
				#print('yes')
				tag.append(loop)
				page_view.append(int(row[1]))
				page.append(row[0])
				unique.append(float(row[2]))
				avg_time.append(float(row[3]))
				entrance.append(row[4])
				bounce.append(float(row[5]))
				exit.append(row[6])

			else:
				pass
				#print(loop)
				'''
				tag.append('none')
				page.append(row[0])
				page_view.append(row[1])
				unique.append(row[2])
				avg_time.append(row[3])
				entrance.append(row[4])
				bounce.append(row[5])
				exit.append(row[6])
'''
sheet = {
		'tag':tag,'page_view':page_view,
		'page':page,'unique':unique,
		'avg_time':avg_time,'entrance':entrance,'bounce':bounce,
		'exit':exit
		}

df = pd.DataFrame(sheet)
#df2 = df.drop_duplicates()
df2 = df.drop_duplicates(subset=['page'], keep='last')

df2.to_csv('remove5.csv')


#print(sheet)
#print(len(sheet))
#df = pd.DataFrame()
#df.to_csv('try.csv') 

#print(page_view)
#print(len(all_page_view))
#print(sum(all_page_view))
#print(sum(page_view))
#print(len(y))
#print(len(tag))
'''
print('urls with')
print(sport_name)

print('event bounce average = ' + str(sum(bounce)/len(bounce)))
print('all bounce average = ' + str(sum(all_bounce)/len(all_bounce)))


print('event page time average = ' + str(sum(avg_time)/len(avg_time)))
print('all page time average = ' + str(sum(all_avg_time)/len(all_avg_time)))


print('event unique average = ' + str(sum(unique)/len(unique)))
print('all unique average = ' + str(sum(all_unique)/len(all_unique)))
'''

#print(sum(page_view)/(sum(all_page_view)))



'''

files = ['All_Schools_All_Keyword']
keywords = ['anthropology', 'atmospheric sciences','biology','chemistry']

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
			if keywords in row[3]:
				keyword.append(row[3])
				position.append(row[4])
				position1.append(row[5])
				search_vol.append(row[6])
				url.append(row[7])
				url1.append(row[8])
				schoolname.append('tamu')
				schoolname1.append(x)
			else: pass


df = pd.DataFrame({'school':schoolname,'school_compare':schoolname1,'keyword':keyword,'position':position,'position_compare':position1,'search_vol':search_vol,'url':url,'url_compare':url1})


df.to_csv('Keyword_Search.csv') 

'''


'''
# the code below splits string based on the first instance of /


get = []
getting = []

with open ('cision_split.csv','r') as csvfile:
	data_i_need = csv.reader(csvfile)
	for row in data_i_need:
		#print(row[1])
		splitting = row[1].split('/',1)
		print(splitting[0])
		get.append(row[0])
		getting.append(splitting[0])


print(len(get))
print(len(getting))


df = pd.DataFrame({'outlet':get, 'url':getting})

df.to_csv('split_urls.csv')


#converting xlsx into csv file 

# Read and store content
# of an excel file
read_file = pd.read_excel ("1.xlsx")

# Write the dataframe object
# into csv file
read_file.to_csv ("1.csv",index = None, header=True)

# read csv file and convet
# into a dataframe object
df = pd.DataFrame(pd.read_csv("Test.csv"))

for sheet in range(1,23):
	print(sheet)
	file = str(sheet)+'.xlsx'
	print(file)
	read_file = pd.read_excel(file)
	read_file.to_csv (str(sheet)+'.csv',index = None, header=True)
	df = pd.DataFrame(pd.read_csv(str(sheet)+'.csv'))


'''

# looping through csv files to create one giant file
# this is a little different because the first five rows contain: 
	#Email Name
	#Date/Time sent
	#Email Subject
	#Sender Name
	#Sender Email

#then there are the header rows.  I want to create a column for email name, subject , and date/time sent to use as tags
#this lets me figure out what emails are doing what


#I am going to start with one csv to figure out the loops and tagging.  Then I will create one big loop for all 22 files
#grabs the header info from the first few lines of each .csv
'''
email_name = []
date_and_time = []
email_subj = []

#appends each time and acts as a tag
email_name_1= []
date_and_time_1 = []
email_subj_1= []

#data that I want
media_contact = []
media_outlet = []
email_address = []
list_name = []
status = []
links_clicked = []
Bounced = []

with open('9.csv', 'r') as csvfile:
	# dropping this line below becasue the line below it calls it directly so there is no need for a data reader variable
	#datareader = csv.reader(csvfile)
	# this is really cool.  Using islice from itertools I am starting the look at row 0 and ending at row five.
	# this lets me take the header information on the first 4 lines to be used as a tag for the rest of the information
	for row in islice(csv.reader(csvfile),0,5):
		#print(row[0])
		if "Email Name" in row:
			email_name.append(row[1])
		if "Date/Time sent" in row:
			date_and_time.append(row[1])
		if "Email Subject" in row:
			email_subj.append(row[1])
	#using islice and starting where data begins
	for row in islice(csv.reader(csvfile),6,None):
		email_name_1.append(email_name[0])
		date_and_time_1.append(date_and_time[0])
		email_subj_1.append(email_subj[0])
		media_contact.append(row[0])
		media_outlet.append(row[1])
		email_address.append(row[2])
		list_name.append(row[3])
		status.append(row[4])
		links_clicked.append(row[5])
		Bounced.append(row[6])

df = pd.DataFrame({'email_subj':email_subj_1,'email_name':email_name_1,'date_and_time':date_and_time_1,'media_contact':media_contact,'media_outlet':media_outlet,'email_address':email_address,'list_name':list_name,
					'status':status,'links_clicked':links_clicked,'Bounced':Bounced})
df.to_csv('try.csv') 
#print(email_subj,email_name,date_and_time)





#the code above solves the problem of tagging each of the data points with the header information.  Now I need to loop through all 22 .csv to create one list
#first I need to recreate the code above but it is going to be nested in a loop that loops through each file

email_name = []
date_and_time = []
email_subj = []

#appends each time and acts as a tag
email_name_1= []
date_and_time_1 = []
email_subj_1= []

#data that I want
media_contact = []
media_outlet = []
email_address = []
list_name = []
status = []
links_clicked = []
Bounced = []

file_name = []

for files in range(1,23):
	file_name.append(str(files)+'.csv')

for got_it in file_name:
	with open(got_it, 'r') as csvfile:
		# dropping this line below becasue the line below it calls it directly so there is no need for a data reader variable
		#datareader = csv.reader(csvfile)
		# this is really cool.  Using islice from itertools I am starting the look at row 0 and ending at row five.
		# this lets me take the header information on the first 4 lines to be used as a tag for the rest of the information
		for row in islice(csv.reader(csvfile),0,5):
			#print(row[0])
			if "Email Name" in row:
				email_name = (row[1])
			if "Date/Time sent" in row:
				date_and_time = (row[1])
			if "Email Subject" in row:
				email_subj = (row[1])
		#using islice and starting where data begins
		for row in islice(csv.reader(csvfile),6,None):
			email_name_1.append(email_name)
			date_and_time_1.append(date_and_time)
			email_subj_1.append(email_subj)
			media_contact.append(row[0])
			media_outlet.append(row[1])
			email_address.append(row[2])
			list_name.append(row[3])
			status.append(row[4])
			links_clicked.append(row[5])
			Bounced.append(row[6])

df = pd.DataFrame({'email_subj':email_subj_1,'email_name':email_name_1,'date_and_time':date_and_time_1,'media_contact':media_contact,'media_outlet':media_outlet,'email_address':email_address,'list_name':list_name,
					'status':status,'links_clicked':links_clicked,'Bounced':Bounced})
df.to_csv('try_all.csv') 
#print(email_subj,email_name,date_and_time)


#print(file_name)


'''
