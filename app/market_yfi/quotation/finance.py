from datetime import date

import yfinance as yf


class Finance:
    today = date.today()
    folder_name = "./data_market/"

    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    def get_quotation_yfi(self):
        get_ticket_info = yf.Ticker(self.symbol)
        data = get_ticket_info.history(start=self.start_date, end=self.end_date)
        self._put_info_file_name(data)
        return data

    def _put_info_file_name(self, data):
        data_file_name = (
            f"{str(self.today)}_{self.start_date}_{self.end_date}_{self.symbol}"
        )
        self._save_file_data(data, data_file_name)
        return True

    def _save_file_data(self, df, filename):
        df.to_csv(self.folder_name + f"{filename}.csv")
        return True
