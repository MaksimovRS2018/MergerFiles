class Parser_comtrade():
    def __init__(self, path="1", flag="start_test", time_d=20000 / 24):
        self.__path_cfg = path + ".cfg"
        self.__path_dat = path + ".dat"
        self.__data_A = {}
        self.__data_B = {}
        self.__name_analog = []
        self.__name_digital = []
        self.__data_analog = {}
        self.__data_analog = {}
        self.__flag = flag
        self.__time_d = time_d
        self.__numbers_analog = 0
        self.__numbers_digital = 0

    def pars_cfg(self):
        with open(self.__path_cfg, 'r') as fp:
            data = fp.readlines()
            self.__numbers_analog = int(data[1].split(",")[1].split("A")[0])
            self.__numbers_digital = int(data[1].split(",")[2].split("D")[0])
            for number_analog in range(self.__numbers_analog):
                self.__name_analog.append(data[2 + number_analog].split(",")[1])
                self.__data_A[data[2 + number_analog].split(",")[1]] = float(data[2 + number_analog].split(",")[5])
                self.__data_B[data[2 + number_analog].split(",")[1]] = float(data[2 + number_analog].split(",")[6])
            for number_digital in range(self.__numbers_analog, self.__numbers_analog + self.__numbers_digital):
                self.__name_digital.append(data[2 + number_digital].split(",")[1])
        # print(self.__data_A)
        # print(self.__data_B)
        # print(self.__name_analog)
        # print(self.__name_digital)
        fp.close()

    def pars_dat(self):
        with open(self.__path_dat, 'r') as fp:
            data = fp.readlines()
            # print(len(data))
            self.__data_analog = dict.fromkeys(self.__name_analog, [])
            for t in range(len(data)):
                for number_analog in range(self.__numbers_analog):
                    a = self.__data_A[self.__name_analog[number_analog]]
                    b = self.__data_B[self.__name_analog[number_analog]]
                    x = int(data[t].split(",")[2+number_analog])
                    value = a*x-b
                    actual_list = self.__data_analog[self.__name_analog[number_analog]]
                    actual_list.append(value)
                    self.__data_analog[self.__name_analog[number_analog]] = actual_list
        print(self.__data_analog["IBURA1"][0:100])
        fp.close()
