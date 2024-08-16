def save_to_json(data, filename):

    import json
    
    with open(f'./data/json/{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


def save_to_csv(data, filename):

    import pandas as pd
    from datetime import datetime

    filename = datetime.today().strftime('%Y_%m_%d')
    data_df = pd.DataFrame(data=data)
    data_df = data_df.explode('genre')
    data_df.to_csv(f'./data/csv/{filename}.csv', index=False)

    return data_df


def save_to_parquet(data_df, filename):

    import pyarrow as pa
    import pyarrow.parquet as pq

    data_table = pa.Table.from_pandas(data_df)
    pq.write_table(data_table, f'./data/parquet/{filename}.parquet')

    # Try this one Chanh. Don't need to import pyarrow
    import pandas as pd
    data_df.to_parquet(f"./data/parquet/{filename}.parquet")

def save_data(data):

    from datetime import datetime

    filename = datetime.today().strftime('%Y_%m_%d')

    save_to_json(data, filename)
    data_df = save_to_csv(data, filename)
    save_to_parquet(data_df, filename)