import argparse
import json
import logging
import os
import re

from datetime import datetime
from tqdm import tqdm
from typing import TypedDict
from xml.etree import ElementTree as ET

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO)

XMLNS = "{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}"
VERSION_PATTERN = r"Version (\d{2}\.\d{2}\.\d{4})\.akn"

class DocumentMetadata(TypedDict):
    kind: str
    number: str
    fulltitle: str
    shortitle: str
    filename: str

class DocumentData(TypedDict):
    metadata: DocumentMetadata
    rawtext: str

def nstag(tag: str, xmlns: str=XMLNS) -> str:
    """Prepend a tag with an XML namespace string"""
    return f"{xmlns}{tag}"

def unique_tag_text(xml: ET, tag: str) -> None | str:
    """Returns the text contained in the specified tag in the XML tree"""
    tag = xml.find(f""".//{nstag(tag)}""")
    return tag.text if tag is not None else None

def extract_metadata(xml: ET, filename: str) -> None | DocumentMetadata:
    """Extract the metadata from an AKN XML file"""
    kind = unique_tag_text(xml, "docType")
    return None if kind is None else {
        "kind": kind,
        "number": unique_tag_text(xml, "docNumber"),
        "fulltitle": f"""{kind} {unique_tag_text(xml, "docTitle")}""",
        "shortitle": unique_tag_text(xml, "shortTitle"),
        "filename": filename
    }

def string_from_file(filename: str) -> str:
    """Returns the content of a file as a string"""
    with open(filename, "rb") as f:
        return f.read().decode("utf-8")

def extract_rawtext(xml: ET) -> str:
    """Return the concatenated raw text from the elements of an XML tree"""
    return "\n".join(filter(lambda s: s.strip() != "", xml.itertext()))

def get_args():
    parser = argparse.ArgumentParser(
        prog="akn2json",
        description="An AKN XML files to JSON transformer"
    )

    parser.add_argument("--latest", action="store_true", help="only keep the latest version of each act")
    parser.add_argument("INPUT_FOLDER", default="Actes")
    parser.add_argument("OUTPUT_FILE", default="out.json")

    return parser.parse_args()

def extract_date(text: str, pattern: str) -> None | datetime:
    """Extract the date of a given text using `pattern`"""
    match = re.search(pattern, text)
    return None if match is None else datetime.strptime(match.group(1), "%d.%m.%Y")

def is_latest_in_folder(folder: str, file: str, pattern: str) -> bool:
    """Returns true if the specified file is the latest in its subfolder according to the date
    in its name, specified by `pattern`"""
    date = extract_date(file, pattern)
    if date is None:
        return False
    
    for other_file in os.listdir(folder):
        if file == other_file:
            continue

        other_date = extract_date(other_file, pattern)
        if other_date == None:
            continue

        if other_date > date:
            return False
        
    return True

def trim_forest(forest: list, only_latest: bool=False) -> int:
    """Remove empty folders from forest and also keep the latest file using the date in its name if needed.
    Returns the trimmed forest file count.
    """
    c = 0
    for folder in forest:
        if folder[2] == []:
            forest.remove(folder)
            continue

        if only_latest:
            latest = list(filter(lambda f: is_latest_in_folder(folder[0], f, VERSION_PATTERN), folder[2]))
            folder = (*folder[:2], latest)

        c += len(folder[2])

    return c

def main():
    args = get_args()

    input_folder = args.INPUT_FOLDER
    output_file = args.OUTPUT_FILE

    ret = []
    logger.info("Fetching document tree")
    forest = list(os.walk(input_folder))

    n_acts = trim_forest(forest, only_latest=args.latest)
    logger.info(f"Extracting data from non-empty {n_acts} acts")
    for (root, _, files) in tqdm(forest):
        for file in filter(lambda f: f.endswith("akn"), files):
            filename = os.path.join(root, file)
            
            xml = ET.fromstring(string_from_file(filename))
            metadata = extract_metadata(xml, file)

            if metadata is None:
                continue

            ret.append(DocumentData({
                "metadata": metadata,
                "rawtext": extract_rawtext(xml)
            }))

    logger.info(f"Writing {output_file}")
    with open(output_file, "w") as f:
        f.write(json.dumps(ret, indent=2))

if __name__ == "__main__":
    main()
