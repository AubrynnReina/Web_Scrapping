def convert_to_dict(id, data) -> dict:

    result_dict = {
        'id': id,
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


def append_data(id, data, data_dict):
    
    for i in range(len(data[1])):

        for j, key in enumerate(data_dict):

            if j == 0:  
                data_dict[key].append(id)
            
            elif j == 2:
                data_dict[key].append(data[j - 1][i])
                
            else:
                data_dict[key].append(data[j - 1])

    return data_dict