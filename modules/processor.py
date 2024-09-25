def convert_to_dict(id, latest_ep, data) -> dict:

    result_dict = {
        'id': id,
        'latest_ep': latest_ep,
        'name': data[0],
        'genre': data[1],
        'status': data[2],
        'score': data[3],
        'review': data[4],
        'publish_year': data[5],
        'duration': data[6],
        'link': data[7]
    }
    return result_dict

def clean_data_for_gold(file_name):

    import pandas as pd

    bronze_data = pd.read_csv('')