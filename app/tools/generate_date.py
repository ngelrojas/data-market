from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_date_ten_years_ago():
    return datetime.now() - relativedelta(years=10)
