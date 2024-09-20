import requests
from bs4 import BeautifulSoup

def get_movie_items(page):

    domain_name = 'animehay.biz'
    url = f'https://{domain_name}/phim-moi-cap-nhap/trang-{page}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept-Encoding': '*',
        'Connection': 'keep-alive'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return ()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    movie_items = soup.find_all('div', class_='movie-item')

    return movie_items

def extract_data(movie) -> tuple:
    
    link = movie.select('a:nth-child(2)')[0]['href']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept-Encoding': '*',
        'Connection': 'keep-alive'
    }
    response = requests.get(link, headers=headers)
    
    if response.status_code != 200:
        return ()

    soup = BeautifulSoup(response.content, 'html.parser')
    
    movie_data = soup.find('div', class_='last')

    if movie_data is None:
        return ()
    
    name = soup.find('h1', class_='heading_movie').text.strip()

    raw_categories = movie_data.find('div', class_='list_cate') \
                            .text.split('\n')[4:-1:2]
    categories = [category.strip() for category in raw_categories]

    movie_status = movie_data.find('div', class_='status') \
                    .select('div:nth-child(2)')[0] \
                    .text.strip()
    
    score_and_review = movie_data.find('div', class_='score') \
                                 .select('div:nth-child(2)')[0].text.split()[:-2:2]
    score = float(score_and_review[0]) if score_and_review[0] != 'NaN' else None
    review = int(score_and_review[1]) if score_and_review[1] != 'NaN' else None

    publish_year_str = movie_data.find('div', class_='update_time') \
                                 .select('div:nth-child(2)')[0].text.strip()
    publish_year = int(publish_year_str) if publish_year_str != 'NaN' else None
    
    duration = movie_data.find('div', class_='duration') \
                        .select('div:nth-child(2)')[0].text.strip()
    
    return (name, categories, movie_status, score, review, publish_year, duration, link)