from datetime import datetime
import re
from os import walk
import xmlschema


def find_last_actes(root_directory):
    # Define the pattern to match
    pattern = r"Version (\d{2}\.\d{2}\.\d{4})\.akn"

    # Dictionary to store the newest version of each actes
    last_actes = {}

    now = datetime.now()

    # Walk through the directory structure
    for current_dir, _, files in walk(root_directory):
        for file in files:
            match = re.search(pattern, file)
            if match:
                version_date = datetime.strptime(match.group(1), "%d.%m.%Y")
                if version_date < now :
                    if (current_dir not in last_actes) or (last_actes[current_dir][1] < version_date) :
                        last_actes[current_dir]=(file,version_date)

    return last_actes

if __name__ == "__main__":
    # Usage
    directory = "../Actes/"
    last_actes = find_last_actes(directory)
    xsd_doc = 'akomantoso30.xsd'
    for key in last_actes :
        xsd_doc = 'akomantoso30.xsd'    
        json = xmlschema.to_json(xml_document=f'{key}/{last_actes[key][0]}',schema=xsd_doc,validation='skip')
        with open(f'./json/{last_actes[key][0][:-3]}json', 'w') as file:
            file.write(json)

    #print(len(last_actes))
