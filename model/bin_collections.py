from model.bin_day import BinDay

class BinCollections:

    def __init__(self):
        self.bin_collections = {}

    def add(self, bin_day: BinDay):
        self.bin_collections[bin_day.type] = bin_day.date