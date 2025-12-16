from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

# Calculate the difference between a start time and an end time.
def calc_time_diff_hr(start_time:datetime, end_time:datetime):
    time_diff = end_time - start_time
    return time_diff

print(calc_time_diff_hr(datetime(1995, 10, 27, 9, 9, 45), datetime.now()))


