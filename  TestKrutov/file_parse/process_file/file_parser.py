import os
from file_parse.process_file.xml_read import read_xml_file
from file_parse.process_file.json_read import read_json_file


class FileParser:

    def __init__(self, file_path: str, supported_file_types: list):
        self.file_paths = []
        self.file_index = 0
        self.supported_file_types = supported_file_types
        if os.path.isfile(file_path):
            self.add_supported_file(file_path)
        else:
            self.walk_and_add_files(file_path)
        self.current_file = self.file_paths[self.file_index] if self.file_index < len(self.file_paths) else None

    def add_supported_file(self, file_path):
        file_type = os.path.splitext(file_path)[-1].lower()
        if file_type in self.supported_file_types:
            self.file_paths.append(file_path)

    def walk_and_add_files(self, directory):
        for root, dirs, files in os.walk(directory, topdown=True):
            for name in files:
                self.add_supported_file(os.path.join(root, name))

    def increment_index(self) -> None:
        if self.file_index < len(self.file_paths) - 1:
            self.file_index += 1
            self.current_file = self.file_paths[self.file_index]
        else:
            self.current_file = None

    async def read_file(self):
        if not self.current_file:
            return ""
        file_type = os.path.splitext(self.current_file)[-1].lower()
        if file_type in ['.xml']:
            return await read_xml_file(self.current_file)
        elif file_type in ['.json']:
            return await read_json_file(self.current_file)
        else:
            return "Unsupported file type"

