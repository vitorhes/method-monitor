from datetime import datetime
import calendar
from typing import Tuple
def __get_month_range(month: int) -> Tuple[str, str]:
    # Get the current year and calculate the start and end dates for the given month
    current_year = datetime.now().year
    num_days_in_month = calendar.monthrange(current_year, month)[1]
    start_date = datetime(current_year, month, 1).isoformat()
    end_date = datetime(current_year, month, num_days_in_month).isoformat()
    return start_date, end_date
x,y = __get_month_range(3)
print(x,y)