import pathlib
import csv
from core.quotation import Quotation


class SaveQuery:
    """
    TODO: __read_file_csv override, because in data_market folder exist
    more than one file.
    """

    def __save_quotation(self, data_row):
        quotation = Quotation.objects.create(
            date=data_row[0],
            open=data_row[1],
            high=data_row[2],
            low=data_row[3],
            close=data_row[4],
            volume=data_row[5],
            dividends=data_row[6],
            stock_splits=data_row[7],
        )
        return quotation

    def __read_file_csv(self):
        csv_file = ""
        folder_path = pathlib.Path("./data_market/")
        for _file in folder_path.iterdir():
            csv_file = _file
        return csv_file

    def saving_quotation(self):
        csv_file = self.__read_file_csv()

        with open(csv_file, "r") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            for row in reader:
                self.__save_quotation(row)
        return True
