import os
import shutil
import xml.etree.ElementTree as ET

CONFIG = 'config.xml'


class XmlDeserializer:
    def __init__(self, config):
        self.config = config

    @property
    def deserializer(self):
        tree = ET.parse(self.config)
        config_root = tree.getroot()
        for file in config_root:
            file_name = file.attrib['file_name']
            src_path = os.path.join(file.attrib['source_path'], file_name)
            dst_path = os.path.join(file.attrib['destination_path'], file_name)
            yield File(file_name, src_path, dst_path)


class File:
    def __init__(self, file_name, src_path, dst_path) -> None:
        self.file_name = file_name
        if not os.path.isabs(src_path):
            src_path = os.path.abspath(src_path)
        if not os.path.isabs(dst_path):
            dst_path = os.path.abspath(dst_path)
        self.dst_path = dst_path
        self.src_path = src_path


class FileProvider:
    @staticmethod
    def path_validator(file: File) -> bool:
        return os.path.exists(file.src_path) and os.path.exists(os.path.dirname(file.dst_path))

    @staticmethod
    def file_copier(file: File) -> None:
        shutil.copyfile(file.src_path, file.dst_path)


def main(xml_file):
    xml_des = XmlDeserializer(xml_file)
    parser = xml_des.deserializer

    for file in parser:
        if FileProvider.path_validator(file):
            FileProvider.file_copier(file)


if __name__ == "__main__":
    main(CONFIG)
