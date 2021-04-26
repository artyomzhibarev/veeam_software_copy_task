import os
import shutil
from typing import AnyStr
import xml.etree.ElementTree as ET


def xml_parser(xml_file: AnyStr) -> None:
    tree = ET.parse(xml_file)
    config_root = tree.getroot()
    for file in config_root:
        file_name = file.attrib['file_name']
        source_path = os.path.join(file.attrib['source_path'], file_name)
        destination_path = os.path.join(file.attrib['destination_path'], file_name)
        path = os.path.dirname(destination_path)
        if os.path.exists(source_path) and os.path.exists(os.path.dirname(destination_path)):
            shutil.copyfile(source_path, destination_path)



# def copy_file(src_, dst_):
#     shutil.copy(src=src_, dst=dst_)


if __name__ == '__main__':
    print(xml_parser('config.xml'))
    # print(os.path.join('sdf', 'aea'))
