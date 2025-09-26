# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
from functions.write_file import write_file


def main():
    working_dir = "calculator"
    print(write_file(working_dir, 'pkh/lorem.txt', "bkawjbfawjklbmargp"))

main()