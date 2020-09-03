import logging
import sys


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

    logging.debug(f"number_of_levels {num_of_levels}")

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


FORMAT = '%(levelname)s %(module)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

if __name__ == '__main__':

    try:
        logging.info('Task Started')

        if len(sys.argv) == 3:
            logging.info("Output file name: " + str(sys.argv[1]) + " Input file name: " + str(sys.argv[2]))
            input_file_name = str(sys.argv[1])
            output_file_name = str(sys.argv[2])

        with open(input_file_name, encoding='utf-8') as csv_file:
            d_reader = csv.DictReader(csv_file)
            logging.info("Input file loaded")

        logging.info('Task completed successfully')

    except FileNotFoundError as error:
        logging.error(f"{input_file_name} file not found")

    except Exception as error:
        logging.error(error)
