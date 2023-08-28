from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_date_ten_years_ago():
    return datetime.now().date() - relativedelta(years=10)


def get_current_date():
    return datetime.now().date()
