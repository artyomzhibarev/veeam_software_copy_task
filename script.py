import os.path
import shutil
from typing import AnyStr
import xml.etree.ElementTree as ET


def xml_parser(xml_file: AnyStr):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for child in root:
        source_path = child.attrib['source_path']
        destination_path = child.attrib['destination_path']
        file_name = child.attrib['file_name']
        # print(source_path, destination_path, file_name)


def copy_file(src_, dst_, filename):
    shutil.copyfile(src=src_ + filename, dst=dst_ + filename)


if __name__ == '__main__':
    xml_parser('config.xml')
