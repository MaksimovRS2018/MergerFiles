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
from functools import reduce

parser_rtds_comtrade = Parser_comtrade(path="1", flag="start_test", A=False, D=True)
parser_terminal_comtrade = Parser_comtrade(path="2", flag="224 Пуск осциллогр.", A=True, D=True)

parser_rtds_comtrade.pars_cfg()
parser_rtds_comtrade.pars_dat()
t1 = parser_rtds_comtrade.search_start_time()
parser_terminal_comtrade.pars_cfg()
parser_terminal_comtrade.pars_dat()
t2 = parser_terminal_comtrade.search_start_time()
list_times_before = []
count_before = 0
time_for_before = t1
while time_for_before > 0 and len(list_times_before) < (parser_terminal_comtrade.index_time + 1):
    list_times_before.append(time_for_before)
    count = int(883 / 50) * 50
    time_for_before = time_for_before - count
print(len(list_times_before))
list_times_after = []
count_after = 0
time_for_after = t1
print(parser_terminal_comtrade.end_time)
while len(list_times_after) < (parser_terminal_comtrade.index_end_time - parser_terminal_comtrade.index_time - 1):
    count = int(883 / 50) * 50
    time_for_after = time_for_after + count
    list_times_after.append(time_for_after)
print(len(list_times_after))
times = (list_times_before + list_times_after)
times.sort()


# index_times = list(map(lambda x: (int(x / 50)), times))


def filter_max(x):
    if x < 60000:
        return True
    return False


def list_to_str(list_data):
    string = ""
    for i in range(len(list_data)):
        string = string + ", " + str(int(list_data[i]))
    return string

index_times = list(filter(filter_max, list(map(lambda x: (int(x / 50)), times))))
print(max(index_times))
shutil.copyfile("2.cfg", "3.cfg")
shutil.copyfile("2.dat", "3.dat")
name_digital_rtds = parser_rtds_comtrade.name_digital
with open("3.cfg", 'w') as fp:
    number_str = 2 + parser_terminal_comtrade.numbers_signal
    data_cfg_terminal = parser_terminal_comtrade.data_cfg
    for new_index_digital in range(len(name_digital_rtds)):
        new_str = str(len(parser_terminal_comtrade.name_digital) + new_index_digital + 1) + "," + name_digital_rtds[
            new_index_digital] + ",0\n"
        data_cfg_terminal.insert(number_str + new_index_digital, new_str)
    new_number_digital = len(parser_terminal_comtrade.name_digital) + len(parser_rtds_comtrade.name_digital)
    list_1 = data_cfg_terminal[1].split(",")
    data_cfg_terminal[1] = str(len(parser_terminal_comtrade.name_analog) + new_number_digital) + "," + str(
        len(parser_terminal_comtrade.name_analog)) + "A," + str(new_number_digital) + "D\n"
    for i in range(len(data_cfg_terminal)):
        fp.write(data_cfg_terminal[i])

with open("3.dat", 'w') as fp:
    data_dat_terminal = parser_terminal_comtrade.data_dat
    # a = parser_terminal_comtrade.matrix_digital
    # matrix_digital_rtds = parser_rtds_comtrade.matrix_digital
    for index in range(len(index_times)):
        list_data_digital = list(parser_rtds_comtrade.matrix_digital[index_times[index], 2:])
        # str_data_digital = reduce(lambda x, y: str(x) + ", " + str(int(y)), list_data_digital)
        str_data_digital = list_to_str(list_data_digital)
        fp.write(data_dat_terminal[index].split("\n")[0] + ", " + str_data_digital + "\n")
# def list_to_str(list_data):
#     string=""
#     for i in range(len(list_data)):
#         string = string + ", "+ str(int(list_data[i]))#
#     return string
# a= [1,2,3]
# print(list_to_str(a))
# str_data_digital = reduce(lambda x, y: str((x)) + ", " + str((int(y))), a)
# print(str_data_digital)
