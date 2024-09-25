def save_to_json(data, stage, filename):

    import json
    
    with open(f'./data/{stage}/json/{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


def save_to_csv(data, stage, filename):

    import pandas as pd

    data_df = pd.DataFrame(data=data)
    data_df = data_df.explode('genre')
    data_df.to_csv(f'./data/{stage}/csv/{filename}.csv', index=False, encoding='utf-8')

    return data_df


def save_to_parquet(data_df, stage, filename):

    data_df.to_parquet(f'./data/{stage}/parquet/{filename}.parquet', index=False)

def save_data(data, stage):

    from datetime import datetime

    filename = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

    save_to_json(data, stage, filename)
    data_df = save_to_csv(data, stage, filename)
    save_to_parquet(data_df, stage, filename)