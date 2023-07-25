from datetime import date
import yfinance as yf


class ExtractDataYFI:
    today = date.today()
    folder_name = './data_market/'

    def __get_data_yfi(self, data_req):
        get_ticket_info = yf.Ticker(data_req.get("symbol"))
        data = get_ticket_info.history(start=data_req.get('start_date'), end=data_req.get('end_date'))
        return data

    def data_file_name_yfi(self, data_req):
        data_yfi = self.__get_data_yfi(data_req)
        data_file_name = f'{str(self.today)}_{data_req.get("symbol")}'
        self.save_file_data_yfi(data_yfi, data_file_name)
        return True

    def save_file_data_yfi(self, df, filename):
        df.to_csv(self.folder_name + f'{filename}.csv')
        return True
