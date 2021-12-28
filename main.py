# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

from ParserComtrade import Parser_comtrade

parser = Parser_comtrade(path="2")
# print(list(range(0,300000,50)))
parser.pars_cfg()
parser.pars_dat()
parser.search_start_time()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
