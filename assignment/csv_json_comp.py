import pandas as pd
import json
import csv
from sys import argv

#reading the csv file
reader=csv.reader(open(argv[1],encoding="utf-8"))
ws=pd.read_csv(argv[1])

#function for filtering names with all alphabets in lower case
def f1(word):
  if word.islower():
    return True

#function for filtering names with special characters in it or containing exactly one word
def f2(word):
  t=word
  word.strip(" ")
  aw=word.isalpha()
  if aw:
    return False
  t.strip()
  if " " in t:
    return False
  return True


#list for storing invalid names
invalid_names =[]

#dictionary for storing valid names with their organisationname and projectname
db={}

#filling invalid names list from name column
for word in ws.name:
  if f1(word) or f2(word):
    invalid_names.append(word)
 


#creating the dictionary db while traversing the data row wise
for row in reader:
  if f1(row[0]) or f2(row[0]):
    pass
  else:
    db[row[0].lower()]={'organisation':row[1],'project':row[2]}
    

#printing invalid names
print("LIST OF INVALID NAMES\n")
for i in invalid_names:
	print(i)

print()

#Loading json data 
with open(argv[2],'r') as f:
  data = json.load(f)


print("The common names in csv and json files is/are\n")
#iterating through data from json file and is the same name exists in scraped data we are printing the required data
c=0
for i in data:
  if db.get(i['n'].lower())==None:
    continue
  else:
    q=db.get(i['n'].lower())
    print(i['n']+", "+i['i']+", "+i['d']+", "+q['organisation'].replace("|",",")+", "+q['project'].replace("|",","))
    c+=1

if c==0:
  print("None")