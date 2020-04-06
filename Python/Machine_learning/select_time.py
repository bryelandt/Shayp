
def select_fridays(df):
    """
        Select the fridays in a time serie

        input: time serie as dataframe
            index = timestamp
        -add column with dayofweek
        -select the fridays
        return dataframe
    """
    import pandas as pd
    import numpy as np
    import datetime

    s = df.index.to_series()
    df['dayofweek'] = s.dt.dayofweek

    fridays = df.loc[df['dayofweek'] == 4]
    del fridays['dayofweek']

    return fridays

def select_hour(df):
    """
        lol
    """

    time = pd.Timestamp(events[i].index[0])
    time = pd.to_datetime(time)
    events_time[i,0] = time.dayofweek
    events_time[i,1] = time.hour





    
