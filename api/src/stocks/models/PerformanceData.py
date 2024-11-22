from pydantic import BaseModel


class PerformanceData(BaseModel):
    five_days: float
    one_month: float
    three_months: float
    year_to_date: float
    one_year: float
