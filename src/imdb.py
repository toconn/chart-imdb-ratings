import requests
from bs4 import BeautifulSoup
from colorama import Fore
from shared import is_windows
from shared import PrintOnLine


def retrieve_imdb_info(show):

    print(".", end = '\r')

    name, seasons = _retrieve_show_name_seasons(_get_seasons_url(show.code))
    show.name = name
    show.seasons = seasons

    line = PrintOnLine()
    line.print(f"{Fore.LIGHTGREEN_EX}{name}{Fore.RESET} : {Fore.LIGHTYELLOW_EX}{seasons} Seasons{Fore.RESET} : ")

    for season in range(1, show.seasons + 1):
        line.print(".")
        ratings = _retrieve_episode_ratings(_get_season_url(show.code, season))
        if len(ratings) > 0:
            show.ratings.append(ratings)

    line.print(" Done")
    print("\n")

def _extract_name(soup):
    title_element = soup.find('h3').find('a')
    return title_element.contents[0].strip()

def _extract_season_count(soup):

    season_dropdown = soup.find('select', id='bySeason')
    if not season_dropdown:
        return 0

    return len(season_dropdown.find_all('option'))

def _get_main_url(show):
    return f"https://www.imdb.com/title/{show}/"

def _get_season_url(show, season):
    return f"https://www.imdb.com/title/{show}/episodes?season={season}"

def _get_seasons_url(show):
    return f"https://www.imdb.com/title/{show}/episodes"

def _retrieve(url):

    # print("Retrieve:", url)

    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def _retrieve_episode_ratings(url):

    soup = _retrieve(url)

    episode_containers = soup.find_all('div', class_='info')
    ratings = []

    for container in episode_containers:
        # episode_number = container.find('meta', itemprop='episodeNumber')['content']
        rating_element = container.find('span', class_='ipl-rating-star__rating')
        rating = float(rating_element.text) if rating_element else None
        if rating:
            # ratingns.append((episode_number, rating))
            ratings.append(rating)

    return ratings

def _retrieve_number_of_seasons(url):

    soup = _retrieve(url)

    season_dropdown = soup.find('select', id='bySeason')
    
    if not season_dropdown:
        return 0

    seasons = len(season_dropdown.find_all('option'))
    return seasons

def _retrieve_show_name(url):

    soup = _retrieve(url)

    title_element = soup.find('h1')
    show_name = title_element.contents[0].strip()
    
    return show_name

def _retrieve_show_name_seasons(url):

    soup = _retrieve(url)
    return _extract_name(soup), _extract_season_count(soup)
