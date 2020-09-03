# storepick-csv-to-json

### Overview: ###

* This is simple python task to convert csv file into json
* Task require two parameters to run
* Task read input file name(.csv) and output file name(.json) parameters from command line
* CSV file contains level wise columns and each level is parent of next level
* Task read this CSV file and validate all columns
* After successfully validation task read records row by row and prepare list of dictionary
* Finally task use this list of dictionary to generate json file 

### Tech Stack:  ###

* python 3.8.5

### Development: ###

* Run test_storepick_menu_convertor.py to runt tests, see requirements.txt 
for package requirements


### Unit Testing:  ###

* Nose Testing

### How To Run Task: ###

* input file path : ../test/data/data.csv
* output file path : ../nested_menu.json
* Open Command prompt
* Got to project directory /storepick-csv-to-json/app 
* Run following command :
    >python storepick_menu_convertor.py ../test/data/data.csv ../nested_menu.json
* File will get generate at root level with name /storepick-csv-to-json/nested_menu.json