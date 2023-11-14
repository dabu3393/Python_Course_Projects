from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
movie_titles = [movie.getText() for movie in movies]
movie_names = movie_titles[::-1]

with open('movies.txt', mode='w') as file:
    for name in movie_names:
        file.write(f'{name}\n')

