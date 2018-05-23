from datetime import datetime
from time import time

def calculate_time_ago(timestamp):
    delta = time() - timestamp
    days, hours, minutes = delta//86400, delta//3600, delta//60
    d = datetime.fromtimestamp(timestamp)

    if days:
        time_str = d.strftime("%B %d at %H.%M")
    elif hours:
        time_str = "{0} hours ago".format(int(hours))
    elif minutes:
        time_str = "{0} minutes ago".format(int(minutes))
    else:
        time_str = "Just {0} seconds ago".format(int(delta))

    return time_str
