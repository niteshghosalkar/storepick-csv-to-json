"""
This module read CSV file and generate nested json

"""
import logging
import csv
import json
import argparse
from typing import List, Dict

FORMAT = '%(levelname)s %(module)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

parser = argparse.ArgumentParser()
parser.add_argument("inputFileName", help="Input file name with path.", type=str)
parser.add_argument("outputFileName", help="Output file name with path.", type=str)


def validate_column_header(reader: csv.DictReader) -> int:
    """
    :param reader: csv file in dictionary format
    :type reader: csv.DictReader
    :return num_of_levels:
    :rtype int:

    This function used to validate CSV column headers
    """

    headers = reader.fieldnames
    headers.pop(0)

    remainder = (len(headers) % 3)
    if remainder > 0:
        raise Exception('Number of columns are invalid')

    num_of_levels = int((len(headers)) / 3)

    logging.debug("number_of_levels %d", num_of_levels)

    column_list = []
    level_number = num_of_levels
    while level_number > 0:
        column_list.extend([f"Level {str(level_number)} - Name", f"Level {str(level_number)} - ID",
                            f"Level {str(level_number)} - URL"])
        level_number -= 1

    for line in headers:
        if line not in column_list:
            raise Exception(f'column name {line} is invalid')

    return num_of_levels


def generate_level_id_key_for_dict(level_number: int, level_id: int, record: Dict) -> str:
    """

    :param level_number: level number
    :type level_number: int
    :param level_id: level number to get id
    :type level_id: int
    :param record: row of csv file
    :type record: Dict
    :return: key
    :rtype: str

    Generate key for Dict by concatenating level number and id
    """
    return 'L' + str(level_number) + '_' + record['Level ' + str(level_id) + ' - ID']


def prepare_dict_for_level(level_number: int, level_dict: Dict, record: Dict) -> Dict:
    """

    :param level_number: level number
    :type level_number: int
    :param level_dict: dictionary of levelNumber_{id}
    :type level_dict: Dict
    :param record: row of csv file
    :type record: Dict
    :return: dictionary of level
    :rtype: dict
    """
    return dict(label=record['Level ' + str(level_number) + ' - Name'],
                id=record['Level ' + str(level_number) + ' - ID'],
                link=record['Level ' + str(level_number) + ' - URL'],
                children=level_dict.get(
                    generate_level_id_key_for_dict(level_number + 1,
                                                   level_number, record),
                    []))


def get_existing_list_of_levels(level_number: int, level_dict: Dict, record: Dict) -> List:
    """
    :param level_number: number of level exist in csv file
    :type level_number: int
    :param level_dict: dictionary of levelNumber_{id}
    :type level_dict: Dict
    :param record: row of csv file
    :type record: Dict
    :return exist_list:
    :rtype exist_list: List

    This function return existing list of dict having level details
    """

    if generate_level_id_key_for_dict(level_number, level_number - 1, record) in level_dict:
        exist_list = level_dict[
            generate_level_id_key_for_dict(level_number,
                                           level_number - 1, record)]
        exist_list[:] = [d for d in exist_list
                         if d.get('id') != record['Level ' + str(level_number) + ' - ID']]
    else:
        exist_list = []

    return exist_list


def make_json(list_of_dict: List, output_json_file_name: str) -> None:
    """
    :param list_of_dict: list having parent child format dictionaries
    :type list_of_dict: List
    :param output_json_file_name: name of output json file
    :type output_json_file_name: str

    This Function get list of dict and create json file
    """

    logging.info("make_json method called")
    if list_of_dict:
        with open(output_json_file_name, 'w') as outfile:
            json.dump(list_of_dict, outfile, sort_keys=True, indent=2)
            logging.info("Output file created")
    else:
        raise Exception("Either file is empty or no values exit in file")


def process(reader: csv.DictReader, num_of_levels: int) -> List:
    """
    :param reader: csv file in dictionary format
    :type reader: csv.DictReader
    :param num_of_levels: count of levels in csv file
    :type num_of_levels: int
    :return list_of_dict:
    :rtype List:

    This function used to read CSV data and prepare list of dict
    """

    first_level_id_set = set()
    try:
        level_dict = {}
        for record in reader:
            level_number = num_of_levels

            while level_number > 0:
                if record['Level ' + str(level_number) + ' - ID']:
                    if level_number == 1:
                        first_level_id_set.add(
                            generate_level_id_key_for_dict(level_number, level_number, record))
                        level_dict[
                            generate_level_id_key_for_dict(level_number,
                                                           level_number, record)] = [
                            prepare_dict_for_level(level_number, level_dict, record)
                        ]
                    else:
                        exist_list = get_existing_list_of_levels(level_number, level_dict, record)

                        exist_list.append(
                            prepare_dict_for_level(level_number, level_dict, record))

                        level_dict[
                            generate_level_id_key_for_dict(level_number,
                                level_number - 1, record)] = exist_list

                level_number -= 1

        logging.debug(level_dict)

        return [level_dict[x][0] for x in first_level_id_set]

    except Exception as err:
        raise err


if __name__ == '__main__':

    try:
        logging.info('Task Started')

        args = parser.parse_args()

        logging.info("Input file name: " + args.inputFileName +
                     " Output file name: " + args.outputFileName)

        with open(args.inputFileName, encoding='utf-8') as csv_file:
            d_reader = csv.DictReader(csv_file)
            logging.info("Input file loaded")

            number_of_levels = validate_column_header(d_reader)
            ordered_final_list_of_dict = process(d_reader, number_of_levels)
            make_json(ordered_final_list_of_dict, args.outputFileName)

        logging.info('Task completed successfully')

    except FileNotFoundError as error:
        logging.error(" %s file not found ", args.inputFileName)

    except Exception as err:
        logging.exception(err)
