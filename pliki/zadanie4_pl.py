import os
import glob
from pathlib import Path

path = 'C:\\Users\\kurs\\workspace'


def check_dir(path):
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            if name.endswith('.py'):
                print(os.path.join(path, name))
        if os.path.isdir(name):
            check_dir(os.path.join(path, name))


check_dir(os.getcwd())


def check_dir2(path):
    for root, dirs, files, in os.walk(path):
        for filename in files:
            if filename.endswith('.py'):
                print(os.path.join(root, filename))


check_dir2(os.getcwd())


def check_dir3(path):
    for filename in (glob.glob('**/*.py', recursive=True)):
        print(os.path.join(path, filename))


check_dir3(os.getcwd())


def check_dir4(path):
    def searching_all_files(directory):
        dirpath = Path(directory)

        file_list = []
        for x in dirpath.iterdir():
            if x.is_file():
                if x.suffix == '.py':
                    file_list.append(x)
                elif x.is_dir():
                    file_list.extend(searching_all_files(x))
        return file_list

    lines_sum = 0
    for x in searching_all_files(path):
        with open(x) as f:
            lines_no = len(f.readlines())
            lines_sum += lines_no
            print(f'{x}\t {lines_no}')
    print(f'\nSuma:\t\t\t{lines_sum}')


check_dir4(os.getcwd())
