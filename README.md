# task 1
The file webscraping.py contains python code for scraping a web page for name,organisationname and projectname with template similar to
https://summerofcode.withgoogle.com/archive/2019/projects/

## Instructions 
clone the repository to your local drive. Inside the assignment directory 
open terminal and run webscrapping.py using following command =>

```
$python webscrapping.py 'url' filename.csv
example
$ python webscraping.py 'https://summerofcode.withgoogle.com/archive/2019/projects/' projects.csv 
```
place the URL of the page to be scraped in place of url. And place the name that you want your scraped csv file to have in place of filename

After running this command a new csv file will be created in the current directory. This file contains the data of selected students in required format.

### Task 2
For this task include the students.json file in assignment directory. Then for getting the required output run the file csv_json_comp.py
with passing csv file and json file as command line arguements.

```
$python csv_json_comp.py ./filename.csv ./filename.json

$python csv_json_comp.py ./projects.csv ./students.json
```
On running this python script first it will display all the unofficial names and then data with common names between the two files.

## Authors

* **Shorya Kumar** 

