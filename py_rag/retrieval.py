from datetime import datetime
import re
from os import walk
# import xmlschema
import xml.etree.ElementTree as ET
import base64


def node_to_text(value):
    if ((value != None) and (value.text !=None)):
        return value.text
    return ''

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

def extract_chunks(acte_file):
    with open(acte_file, 'r') as acte_xml:
        ns = {'ns0' : 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0'}
        tree = ET.parse(acte_xml)
        root = tree.getroot()
    
    docType = node_to_text(root.find('./ns0:act//ns0:preface/ns0:p/ns0:docType',ns))
    docNumber = node_to_text(root.find('./ns0:act//ns0:preface/ns0:p/ns0:docNumber',ns))
    docTitle = node_to_text(root.find('./ns0:act//ns0:preface/ns0:p/ns0:docTitle',ns))
    shortTitle = node_to_text(root.find('./ns0:act//ns0:preface/ns0:p/ns0:shortTitle',ns))
    paragraphs = root.findall('./ns0:act/ns0:body//ns0:content//ns0:p',ns)
    b64_name = base64.b64encode(f'{docNumber}-{docType}-{shortTitle}'.encode('utf-8')).decode('utf-8')
    filename = f'./out/{b64_name}.txt' 
    with open(filename, 'w') as chunks_file:
        chunks_file.write('{')
        if (docType != None):
            chunks_file.write(f'"docType":"{docType}",')
        if (docNumber != None):
            chunks_file.write(f'"docNumber":"{docNumber}",')
        if (docTitle != None):
            chunks_file.write(f'"docTitle":"{docTitle}",')
        if (shortTitle != None):
            chunks_file.write(f'"shortTitle":"{shortTitle.strip('()')}",')
        chunks_file.write('}\n')
        for paragraph in paragraphs:
            text = paragraph.text
            if (text != None):
                chunks_file.write(f'{text}\n')
    print(f'####>\n\t{acte_file}\n\t{filename}')




if __name__ == "__main__":
    # Usage
    directory = "../Actes/"
    last_actes = find_last_actes(directory)
    # test = '../Actes/00b0a620-8e5d-4bdb-be9d-72720fd00ff6/Version 01.01.2011.akn'
    # test = '../Actes/e938e89d-0adc-49e4-8d44-cca669bd6c98/Version 01.02.2021.akn'
    # extract_chunks(test) 

    for key in last_actes :
        file = f'{key}/{last_actes[key][0]}'
        extract_chunks(file)
    


    """
    xsd_doc = 'akomantoso30.xsd'
    for key in last_actes :
        xsd_doc = 'akomantoso30.xsd'    
        json = xmlschema.to_json(xml_document=f'{key}/{last_actes[key][0]}',schema=xsd_doc,validation='skip')
        with open(f'./json/{last_actes[key][0][:-3]}json', 'w') as file:
            file.write(json)

    #print(len(last_actes))
    """
