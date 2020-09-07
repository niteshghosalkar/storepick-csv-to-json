PYTHON_VERSION=python3.8

executeCommand(){

  OPTION=$1

  case ${OPTION} in

  "init")
  ${PYTHON_VERSION} -m pip install -r requirements.txt
  ;;

  "pylint")
  pylint app
  ;;

  "coverage")
  nosetests --with-coverage --cover-erase --cover-package=app --cover-html
  ;;

  "run")
  ${PYTHON_VERSION} app/storepick_menu_convertor.py tests/data/data.csv nested_menu.json
  ;;

  esac
}