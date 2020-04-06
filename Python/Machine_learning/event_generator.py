def event_generator(df,x):
    """
        Divide a time serie into a list of events

        event: uninterrupted consumption
        input: time serie dataframe, x (see line 9)
        output: list of events (dataframes)
        start of an event: pulse
        end of an event: when the x steps of time doesn't have pulse
    """
    import numpy as np
    import pandas as pd

    events_list = []

    event_start = None
    event_end = None

    i = 0
    while i >= 0:
        # check if an event starts
        if (df.values[i] > 0) & (event_start is None):
            event_start = df.index[i]
        # check if it is the end of the event
        elif (event_start is not None):
            if np.sum(df.values[i+1:i+x]) == 0:
                if df.values[i] == 0:
                    event_end = df.index[(i-1)]
                else:
                    event_end = df.index[i]

                if isFridayNight(event_start) is True:
                    # select all event in the data
                    event_time = (event_start <= df.index) & (df.index <= event_end)
                    event = pd.DataFrame(index=df.index[event_time],data=df.values[event_time])
                    # store the event in a list
                    events_list.append(event)
                # reset the event
                event_start = None
                event_end = None
        # loop iteration
        if i <= (len(df)-2):
            i += 1
        else:
            break # end of data

    return events_list

def isFridayNight(time):
    """
        Check if the event occurs on Friday night
    """

    if (time.dayofweek == 4) & (1 <= time.hour) & (time.hour <= 4):
        answer = True
    else:
        answer = False

    return answer
