def save_to_json(data, filename):

    import json
    
    with open(f'./data/json/{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


def save_to_csv(data, filename):

    import pandas as pd

    data_df = pd.DataFrame(data=data)
    data_df = data_df.explode('genre')
    data_df.to_csv(f'./data/csv/{filename}.csv', index=False)

    return data_df


def save_to_parquet(data_df, filename):

    data_df.to_csv(f'./data/parquet/{filename}.parquet', index=False)


def save_data(data):

    from datetime import datetime

    filename = datetime.today().strftime('%Y_%m_%d')

    save_to_json(data, filename)
    data_df = save_to_csv(data, filename)
    save_to_parquet(data_df, filename)