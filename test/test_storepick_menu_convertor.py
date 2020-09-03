import nose
import os, glob
from os import path
from nose.tools import raises
from app.storepick_menu_convertor import *

if __name__ == '__main__':
    nose.main(exit=False)


def test_process():
    with open("data/data.csv", encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        headers = csv_reader.fieldnames
        headers.pop(0)

        num_of_levels = int((len(headers)) / 3)


def test_process_empty_file():
    with open("data/test_data_empty_file.csv", encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        headers = csv_reader.fieldnames
        headers.pop(0)

        num_of_levels = int((len(headers)) / 3)


def test_validate_column_header():
    with open("data/data.csv", encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)


@raises(Exception)
def test_validate_column_header_invalid_no_columns():
    with open("data/test_data_invalid_no_of_columns.csv", encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)


@raises(Exception)
def test_validate_column_header_invalid_column_name():
    with open("data/test_data_invalid_column_name.csv", encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)


def test_make_json():
    with open("data/data.csv", encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        headers = csv_reader.fieldnames
        headers.pop(0)

        num_of_levels = int((len(headers)) / 3)


@raises(Exception)
def test_make_json_empty_list():
    make_json([], "../test_nested_data.json")


def teardown_module():
    for filename in glob.glob("../test_nested_data.json"):
        os.remove(filename)
