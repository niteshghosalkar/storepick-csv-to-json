activate()
{
    VIRTUAL_ENV_DISABLE_PROMPT=true . .venv/bin/activate;
}

executeCommand(){

    OPTION=$1

    case ${OPTION} in

    "venv")
        if [[ -d .venv ]]; then rm -rf .venv; fi
        python3.8 -m venv .venv --clear
        activate
        python3.6 -m pip install --upgrade pip
        ;;

    "init")
        activate
        python3.8 -m pip install -r ../requirements.txt
        ;;

    "pylint")
        activate
        pylint --rcfile=pylint.rc app
        ;;

    "coverage")
        activate
        nosetests --with-coverage --cover-erase --cover-package=app --cover-html
        ;;

    "pydoc")
        activate
        python3.8 -m  pydoc -b storepick_menu_convertor
        ;;

    "run")
      activate
      python3.8 storepick_menu_convertor.py ../tests/data/data.csv ../nested_menu.json



      }

