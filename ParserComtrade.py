import numpy
import matplotlib.pyplot as plt


class Parser_comtrade():
    def __init__(self, path="2", flag="Пуск осциллогр.", time_d=20000 / 24):
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
        self.times = list(range(0, 5521667, 683))
        self.matrix_analog = numpy.zeros((1, 1))
        self.matrix_digital = numpy.zeros((1, 1))

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
            # self.matrix_analog = numpy.zeros((len(data), self.__numbers_analog + 1))
            # for t in range(len(data)):
            #     self.matrix_analog[t, 0] = int(data[t].split(",")[1])
            #     for number_analog in range(self.__numbers_analog):
            #         a = self.__data_A[self.__name_analog[number_analog]]
            #         b = self.__data_B[self.__name_analog[number_analog]]
            #         x = int(data[t].split(",")[2 + number_analog])
            #         value = a * x + b
            #         self.matrix_analog[t, number_analog + 1] = value
            self.matrix_digital = numpy.zeros((len(data), self.__numbers_digital + 1))
            for t in range(len(data)):
                self.matrix_digital[t, 0] = int(data[t].split(",")[1])
                for number_digital in range(self.__numbers_digital):
                    self.matrix_digital[t, number_digital + 1] = int(
                        data[t].split(",")[2 + self.__numbers_analog + number_digital])
        fp.close()

    def plotFig(self, data):
        colors = ["-y", "-g", "-r"]
        fig = plt.figure()
        fig.set_size_inches(30, 15)
        plt.plot(list(range(0, 3000000, 50)), data)
        plt.grid()
        plt.show()

    def search_start_time(self):
        index = self.__name_digital.index(self.__flag) + 1
        data_flag = list(self.matrix_digital[:,index])
        index_time = data_flag.index(1)
        print("Time = ", self.matrix_digital[index_time,0])