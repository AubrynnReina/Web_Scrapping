from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from time import sleep


def get_page_html(url):

    option = Options()
    option.add_argument("--headless")  # Run Edge in headless mode
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--allow-insecure-localhost')

    driver = webdriver.Edge(options=option)
    driver.get(url)
    sleep(1) # 1s time allows the webpage to load

    return driver.page_source


def get_movie_items(page):

    domain_name = 'animehay.biz'
    url = f'https://{domain_name}/phim-moi-cap-nhap/trang-{page}.html'

    page_html = get_page_html(url)
    soup = BeautifulSoup(page_html, 'html.parser')
    movie_items = soup.find_all('div', class_='movie-item')

    return movie_items

def extract_data(movie) -> tuple:
    
    url = movie.select('a:nth-child(2)')[0]['href']
    page_html = get_page_html(url)
    soup = BeautifulSoup(page_html, 'html.parser')
    
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
    
    score_and_review = movie_data \
        .find('div', class_='score') \
        .select('div:nth-child(2)')[0].text.split()[:-2:2]
    score = float(score_and_review[0]) if score_and_review[0] != 'NaN' else None
    review = int(score_and_review[1]) if score_and_review[1] != 'NaN' else None

    publish_year_str = movie_data \
        .find('div', class_='update_time') \
        .select('div:nth-child(2)')[0].text.strip()
    publish_year = int(publish_year_str) if publish_year_str != 'NaN' else None
    
    duration = movie_data.find('div', class_='duration') \
                        .select('div:nth-child(2)')[0].text.strip()
    
    return (name, categories, movie_status, score, review, publish_year, duration, url)