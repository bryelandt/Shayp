import numpy as np
import datetime as dt
import pandas as pd
import time as t

def events2array(events):
    events_array = np.zeros((len(events),15)) # 15 is the maximum event size
    events_time = np.zeros((len(events),2))
    for i in range(len(events)-1):
        # time = pd.Timestamp(events[i].index[0])
        # time = pd.to_datetime(time)
        # events_time[i,0] = time.dayofweek
        # events_time[i,1] = time.hour

        for j in np.arange(len(events[i].values.T[0])):
            events_array[i,j] = events[i].values.T[0][j]

    # events_array = np.c_[events_array,events_time]

    return events_array
