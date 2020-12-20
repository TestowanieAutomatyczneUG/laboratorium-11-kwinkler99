import os


class File:
    def __init__(self, file_path):
        self.file = file_path

    def open(self):
        with open(self.file, 'r') as file_open:
            lines = file_open.readlines()
            return lines

    def edit(self, new_line):
        with open(self.file, 'w') as file_open:
            file_open.write(new_line)

    def delete(self):
        if os.path.isfile(self.file):
            os.remove(self.file)
        else:
            raise Exception(f'{self.file} not found')
