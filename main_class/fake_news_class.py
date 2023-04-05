import pandas as pd

from configs.config_data import TRUE_DATA, FAKE_DATA


class FakeNews:
    def __init__(self):
        self.true = TRUE_DATA
        self.fake = FAKE_DATA
        self.main_data =
        self.run()

    def run(self):
        self.print_data()

    def print_data(self):
        data1 = pd.read_csv(self.true)
        print(data1)
        data2 = pd.read_csv(self.fake)
        print(data2)

