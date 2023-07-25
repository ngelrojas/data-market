from rest_framework import status
from rest_framework.response import Response


class DateRequired:
    def dates_required(self, start_date, end_date):
        if not start_date or not end_date:
            raise ValueError("start_date and end_date are required")
