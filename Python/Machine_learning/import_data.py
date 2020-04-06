def import_data(input):
    """
        import a csv into a dataframe

        input: csv file
        - set timestamp as index
        - change utc tz to cet tz
        - remove useless columns
        return df
    """
    import pandas as pd

    df = pd.read_csv(input)

    df.timestamp = pd.to_datetime(df.timestamp, utc = True)
    df.set_index('timestamp', inplace=True)
    df = df.tz_convert('Europe/Brussels')
    del df['device_id']
    del df['consolidation']

    return df
