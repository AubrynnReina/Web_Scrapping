def save_to_json(data, filename):

    import json
    
    with open(f'./data/json/{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


def convert_to_dataframe(data):
    import pandas as pd

    data_df = pd.DataFrame(data=data)

    return data_df

def save_to_csv(data_df, filename):

    data_df = data_df.explode('genre')
    data_df.to_csv(f'./data/csv/{filename}.csv', index=False)


def save_to_parquet(data_df, filename):

    # import pyarrow as pa
    # import pyarrow.parquet as pq

    # data_table = pa.Table.from_pandas(data_df)
    # pq.write_table(data_table, f'./data/parquet/{filename}.parquet')

    # Try this one Chanh. Don't need to import pyarrow
    data_df.to_parquet(f"./data/parquet/{filename}.parquet", index=False)

def save_data(data):

    from datetime import datetime

    filename = datetime.today().strftime('%Y_%m_%d')

    data_df = convert_to_dataframe(data=data)
    save_to_json(data, filename)
    save_to_csv(data_df=data_df, filename=filename)
    save_to_parquet(data_df=data_df, filename=filename)