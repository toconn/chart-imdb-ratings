#!/usr/bin/env python3

from sys import exit
from data import Show
from shared import *
from imdb import retrieve_imdb_info
from chart import create_chart


HELP = f'''Usage: {LIGHT_YELLOW}main {VAR}movie_code{RESET_COLOR}

       {VAR}movie_code{RESET_COLOR}  The IMBD code for the movie (eg tt0944947).
'''


# UI ───────────────────────────────────────────────────── #

def show_show_ratings(show):
	
	ratings_length = show.episodes() * 4 - 1

	print(show.name + ":")
	print()
	print("  Seasons:", show.seasons)
	print()

	for season, ratings in enumerate(show.ratings, 1):
		season_ratings = ' '.join([str(rating) for rating in ratings])
		season_ratings = season_ratings.ljust(ratings_length)
		print (f"  S {season:>02}   {season_ratings}   {show.season_average(season - 1)}")

	print()

def show_show_summary(show):
	print(f'{show.name:30} : {show.seasons:2}')

def show_help():
	print(HELP)


# Main ─────────────────────────────────────────────────── #

def get_settings():
	return Show(argument(0))

def main(show):
	retrieve_imdb_info(show)
	# show_show_ratings(show)
	# show_show_summary(show)
	chart = create_chart(show)
	chart.save(show.name + " - Ratings.png")


if __name__ == "__main__":

    nl()

    if no_arguments():
        show_help()
        exit()

    main(get_settings())

