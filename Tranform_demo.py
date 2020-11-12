import sys, logging, re
from datetime import datetime

regex = '[^@]+@[^@]+\.[^@]+'


def validate(splited):
    try:
        datetime.strptime(splited[7], '%d/%m/%Y')
        if ('GB' == splited[9] and re.search(regex, splited[18])):
            return True
        else:
            return False
    except Exception as e:
        logging.error("Error while validating", e)
        return False


if __name__ == "__main__":
    try:
        logging.basicConfig(filename='logs.log', format='%(levelname)s:%(asctime)s: %(message)s', encoding='utf-8',
                            filemode='w',
                            level=logging.DEBUG)
        # logging.basicConfig(filename='logs.log', encoding='utf-8', filemode='w', level=logging.DEBUG)
        source = sys.argv[1]
        dest = sys.argv[2]
        logging.debug("abcd")
        logging.debug("source %s destination %s", source, dest)
        sourceFile = open(source, 'r')
        readline = sourceFile.readlines()
        c = 1
        with open(dest, 'w') as success_file:
            with open(str(source).replace('.csv', '_error.csv'), 'w') as fail_file:
                for line in readline:
                    if c == 1:
                        success_file.write(line)
                        fail_file.write(line)
                        c = 2
                        continue
                    if validate(line.split(",")):
                        success_file.write(line)
                    else:
                        fail_file.write(line)
        fail_file.close()
        success_file.close()
    except Exception as e:
        logging.error("Error ", e)
        pass
