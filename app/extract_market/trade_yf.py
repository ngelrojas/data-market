from .yahoo_finances.retrieve_yf import RetrieveYF
from .yahoo_finances.extract_data_yfi import ExtractDataYFI
from ..tools.generate_date import get_date_ten_years_ago, get_current_date


def get_quotation_yfi(symbol, start_date, end_date):
    return RetrieveYF(symbol, start_date, end_date).get_quotation_yfi()


_symbol = "PETR4.SA"
get_quotation_yfi(_symbol, get_current_date(), get_date_ten_years_ago())
