# storepick-menu-creator

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

* Development has been done under python 3.8.5
* Used pylint for bug and quality check
* Used DocString, Typing Module and Type Hint for documentation
* Used argParser for command-line options, arguments and sub-command
* requirements.txt file created for packages requirements

## How To Check code quality ###

* Run following command to clone repo bundle
    >git clone storepick-menu-creator.bundle
* Got to project directory /storepick-menu-creator
* Run following command in command prompt :
    >pylint app
OR
* Run run.sh file with following command
    >source run.sh && executeCommand init
    >source run.sh && executeCommand pylint

### How To Run Unit Testing:  ###

* Nose Testing framework has been used for unit testing
* Run following command to clone repo bundle
    >git clone storepick-menu-creator.bundle
* Script test_storepick_menu_convertor.py to runt tests
* Got to project directory /storepick-menu-creator
* Run following command in command prompt :
    >nosetests --with-coverage --cover-erase --cover-package=app --cover-html
* Will get output with coverage
* Got to project directory /storepick-menu-creator/cover
* Open index.html file in browser to see output
OR
* Run run.sh file with following command
    >source run.sh && executeCommand init
    >source run.sh && executeCommand coverage

### How To Run Task: ###

* Run following command to clone repo bundle
    >git clone storepick-menu-creator.bundle
* Got to project directory /storepick-menu-creator/app
* Run following command in command prompt :
    >python storepick_menu_convertor.py ../tests/data/data.csv ../nested_menu.json
* File will get generate at root level with name /storepick-menu-creator/nested_menu.json
OR
* Run run.sh file with following command
    >source run.sh && executeCommand run

### How to run PyDoc to get module documentation ###

* Got to project directory /storepick-menu-creator/app
* Run following command in command prompt :
   >python -m  pydoc -b storepick_menu_convertor
   Server ready at http://localhost:64954/
   Server commands: [b]rowser, [q]uit
* Browser will open with all modules details
* To stop server type q in same command prompt
OR
* Run run.sh file with following command
    >source run.sh && executeCommand pydoc


