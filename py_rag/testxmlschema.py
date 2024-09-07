import xmlschema
import json
from pprint import pprint
xsd_doc = 'akomantoso30.xsd'
xml_doc_sample ='us_Act_2011-11-29.xml'
xml_doc = '/var/opt/dev/poc_rag_blv/Actes/ad18f7d3-9638-4020-a817-a4f936d47c68/Version 22.02.2022.akn'
akomantoso30 = xmlschema.XMLSchema11(source=xsd_doc,validation='skip')


if akomantoso30.is_valid(xml_doc_sample) :
    print(f'{xml_doc_sample} is valid')
    d = akomantoso30.to_dict(xml_doc_sample)
    #pprint(d)
    print(json.dumps(d, indent=2))
else : 
    print(f'{xml_doc_sample} isn\'t valid')

if akomantoso30.is_valid(xml_doc) :
    print(f'{xml_doc} is valid')
    d = akomantoso30.to_dict(xml_doc)
    #pprint(d)
    print(json.dumps(d, indent=2))
else : 
    print(f'{xml_doc} isn\'t valid')
    print(xmlschema.to_json(xml_document=xml_doc,schema=xsd_doc,validation='lax'))
    #print(akomantoso30.to_json(xml_doc,validation='skip'))
