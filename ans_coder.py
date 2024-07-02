import numpy as np
import math


class AnsCoder:

    def __init__(self, image):
        self.image = image
        self.alphabet = [i for i in range(256)]
        self.r = 18
        self.n = 18
        self.initial_state = pow(2, self.r)
        self.current_state = self.initial_state

    def reset_state(self):
        self.current_state = self.initial_state

    def open(self):
        values = []
        with open(self.image, "r") as file:
            for line in file:
                value = int(line.strip())
                values.append(value)
        return values

    def probability(self, s_values):
        occurrences = {value: s_values.count(value) for value in self.alphabet}
        occurrences_list = list(occurrences.values())
        px_num = len(s_values)
        probabilities_list = [(occurrences_list[i] / px_num) for i in range(len(occurrences_list))]
        return probabilities_list

    def determine_f_and_CDF(self, probabilities_list):
        two_power_n = pow(2, self.n)
        f = [math.floor(probabilities_list[s] * two_power_n) for s in range(len(probabilities_list))]  # po zmianie z ceil na floor działa na uniform.pgm
        CDF = np.insert(np.cumsum(f), 0, 0)
        return f, CDF

    def encode(self, s, f, CDF, stream):
        fs = f[s]
        CDFs = CDF[s]
        x_new = int((math.floor(self.current_state / fs) << self.n) + (self.current_state % fs) + CDFs)

        while x_new > (pow(2, (self.r + 1)) - 1):
            buffer = (self.current_state & 1)  # 1 lub 0 na ostatnim bicie
            buffer = "{:01b}".format(buffer)  # zmiana buffer na string
            stream = stream + buffer  # konkantenacja do stream
            self.current_state >>= 1  # wysunięcie tego ostatniego bitu co już trafił do stream
            x_new = int((math.floor(self.current_state / fs) << self.n) + (self.current_state % fs) + CDFs)  # liczymy x_new dla x z wysuniętym bitem

        return x_new, stream
