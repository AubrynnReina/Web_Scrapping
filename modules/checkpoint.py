def get_checkpoint_data(movie) -> tuple[int, str]:

    movie_id = int(movie['id'][9:])
    movie_latest_ep = movie.find('div', class_='episode-latest').text
    
    return (movie_id, movie_latest_ep)


def save_checkpoint(checkpoint_set):

    import pickle
    CHECKPOINT_PATH = './data/checkpoint.pkl'

    with open(CHECKPOINT_PATH, 'wb') as f:
        pickle.dump(checkpoint_set, f)


def load_checkpoint() -> set[int, str]:
    
    import pickle
    CHECKPOINT_PATH = './data/checkpoint.pkl'

    with open(CHECKPOINT_PATH, 'rb') as f:
        data = pickle.load(f)

    return data