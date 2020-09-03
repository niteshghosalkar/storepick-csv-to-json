import logging
import sys

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
