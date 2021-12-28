# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
import shutil
from ParserComtrade import Parser_comtrade

parser_rtds_comtrade = Parser_comtrade(path="1", flag="start_test")
parser_terminal_comtrade = Parser_comtrade(path="2", flag="224 Пуск осциллогр.")
#
# parser_rtds_comtrade.pars_cfg()
# parser_rtds_comtrade.pars_dat()
# t1 = parser_rtds_comtrade.search_start_time()
# parser_terminal_comtrade.pars_cfg()
# parser_terminal_comtrade.pars_dat()
# t2 = parser_terminal_comtrade.search_start_time()
# list_times_before = []
# count_before = 0
# time_for_before = t1
# while time_for_before > 0 and len(list_times_before) < (parser_terminal_comtrade.index_time + 1):
#     list_times_before.append(time_for_before)
#     count = int(883 / 50) * 50
#     time_for_before = time_for_before - count
# print(len(list_times_before))
# list_times_after = []
# count_after = 0
# time_for_after = t1
# print(parser_terminal_comtrade.end_time)
# while len(list_times_after) < (parser_terminal_comtrade.index_end_time - parser_terminal_comtrade.index_time - 1):
#     count = int(883 / 50) * 50
#     time_for_after = time_for_after + count
#     list_times_after.append(time_for_after)
# print(len(list_times_after))
# times = (list_times_before + list_times_after)
# times.sort()
# index_times = list(map(lambda x: x / 50, times))
# name_digital_rtds = parser_rtds_comtrade.name_digital

shutil.copyfile("2.cfg", "3.cfg")
shutil.copyfile("2.dat", "3.dat")
# for name_digital in range(len(name_digital_rtds)):
#     for index in range(len(index_times)):
#         print("hi")
