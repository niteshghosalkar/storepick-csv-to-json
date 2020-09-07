executeCommand(){

    OPTION=$1

    case ${OPTION} in

    "init")
        python3.8 -m pip install -r ../requirements.txt
        ;;

    "pylint")
        pylint app
        ;;

    "coverage")
        nosetests --with-coverage --cover-erase --cover-package=app --cover-html
        ;;

    "pydoc")
        python3.8 -m  pydoc -b storepick_menu_convertor
        ;;

    "run")
      python3.8 storepick_menu_convertor.py ../tests/data/data.csv ../nested_menu.json



      }

