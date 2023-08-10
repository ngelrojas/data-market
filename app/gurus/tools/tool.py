import json
from os import path


def get_data_mock(stock_file):
    try:
        _file_path = f"gurus/mocks/{stock_file}"
        real_path = path.realpath(_file_path)
        with open(real_path, "r") as data_file:
            data = json.load(data_file)
        return data
    except Exception as e:
        return {"error": e}