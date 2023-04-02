# chart-imdb-ratings

Charts a TV show's episodes by IMDB rating.

Downloads the episodes and their ratings from IMDB and then creates an chart image for those ratings.
The image is saved as a PNG file. Written in Python.

I wrote this over a couple of evenings. It comes as is and without warranty!


Example - Chart Game of Thrones Episodes:

Windows:

	chart tt0944947

Mac / Linux:

	./chart tt0944947

Creates:

![Game of Thrones Episode Ratings Chart](game_of_thrones_ratings.png)


# Python References

[SpeedSheet - Python](https://speedsheet.io/s/python)  
[SpeedSheet - Pillow (Python Image Library)](https://speedsheet.io/s/pillow)  
[SpeedSheet - Beautiful Soup](https://speedsheet.io/s/beautiful_soup)


# Run

	chart imdb_show_code

Example (game of thrones):

	chart tt0944947


# Install - Windows

Create the virtual environment:

	python -m venv venv

Start the environment:

	venv\Scripts\activate

Install the libraries:

	pip install -r requirements.txt



# Install - MacOS / Linux

Create the virtual environment:

	python3 -m venv venv

Start the environment:

	. venv/bin/activate

Install the libraries:

	pip install -r requirements.txt


# Inspiration

The inspiration for this app came from [this reddit post](https://www.reddit.com/r/coolguides/comments/11en5ja/the_decline_of_the_simpsons/) where someone charted the decline of the simpsons in a colorful chart.
