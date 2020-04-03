import bs4
from sys import argv
from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup 

#storing the url passed as command line arguement
my_url = argv[1]

#making connection with the webpage and reading it
uClient = uReq(my_url) 
page_html = uClient.read() 
uClient.close() 

#parsing our html page with beautiful soup
page_soup =soup(page_html,"html.parser")

#selecting all the div tags which contain the information needed to be scrapped
containers = page_soup.findAll("div",{"class":"md-padding archive-project-card__header archive-project-card__header--mod-0"})
containers1=page_soup.findAll("div",{"class":"md-padding archive-project-card__header archive-project-card__header--mod-1"})
containers2=page_soup.findAll("div",{"class":"md-padding archive-project-card__header archive-project-card__header--mod-2"})
containers3=page_soup.findAll("div",{"class":"md-padding archive-project-card__header archive-project-card__header--mod-3"})

filename = argv[2]
f = open(filename, "w",encoding="utf-8")

headers= "name, organisation, project\n"

f.write(headers)

for container in containers:
	name = container.h4.a.text
	divs=container.findAll('div')
	project=divs[0].text
	organisation=divs[1].text
	print(name)
	print(project)
	print(organisation)

	f.write(name.replace(",","|") + "," + organisation.replace(",","|")  + "," + project.replace(",","|") + "\n")

for container in containers1:
	name = container.h4.a.text
	divs=container.findAll('div')
	project=divs[0].text
	organisation=divs[1].text
	print(name)
	print(project)
	print(organisation)

	f.write(name.replace(",","|") + "," + organisation.replace(",","|")  + "," + project.replace(",","|") + "\n")

for container in containers2:
	name = container.h4.a.text
	divs=container.findAll('div')
	project=divs[0].text
	organisation=divs[1].text
	print(name)
	print(project)
	print(organisation)

	f.write(name.replace(",","|") + "," + organisation.replace(",","|")  + "," + project.replace(",","|") + "\n")
for container in containers3:
	name = container.h4.a.text
	divs=container.findAll('div')
	project=divs[0].text
	organisation=divs[1].text
	print(name)
	print(project)
	print(organisation)

	f.write(name.replace(",","|") + "," + organisation.replace(",","|")  + "," + project.replace(",","|") + "\n")

print("\n" + argv[2] + " has been created\n")

f.close()
