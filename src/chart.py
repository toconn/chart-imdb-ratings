from data import Grid, Size
from image import to_boxed_text, to_boxed_rating, to_text
from PIL import Image

CELL_SIZE = Size(32, 22)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def _add_episode_labels(show, grid, image):

	for i in range(show.episodes()):
		cell = to_boxed_text(str(i + 1), WHITE, BLACK)
		point = grid.episode(i)
		image.paste(cell, point)

def _add_episode_ratings(show, grid, image):

	for season, ratings in enumerate(show.ratings):
		for number, rating in enumerate(ratings):
			cell = to_boxed_rating(rating)
			point = grid.rating(season, number)
			image.paste(cell, point)

def _add_season_labels(show, grid, image):

	for i in range(show.seasons):
		cell = to_boxed_text(str(i + 1), WHITE, BLACK)
		point = grid.season(i)
		image.paste(cell, point)

def _add_season_ratings(show, grid, image):

	for season, ratings in enumerate(show.ratings):
		average = show.season_average(season)
		cell = to_boxed_rating(average)
		point = grid.season_average(season)
		image.paste(cell, point)

def _add_title(show, grid, image):
	title = to_text(show.name, BLACK, WHITE)
	image.paste(title, grid.title())	

def _new_grid(show):
	grid_size = Size(show.episodes(), show.seasons)
	return Grid(grid_size, CELL_SIZE)

def create_chart(show):

	grid = _new_grid(show)
	size = grid.image_size()
	image = Image.new('RGBA', size)

	# add_title(show, grid, image)
	_add_episode_labels(show, grid, image)
	_add_season_labels(show, grid, image)
	_add_episode_ratings(show, grid, image)
	_add_season_ratings(show, grid, image)

	return image

