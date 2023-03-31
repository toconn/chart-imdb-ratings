from dataclasses import dataclass
from dataclasses import field
from collections import namedtuple

Offset = namedtuple("Offset", ["col", "row"])
Point = namedtuple("Point", ["x", "y"])
Size = namedtuple("Size", ["width", "height"])

@dataclass
class Show:
    code: str
    name: str = ""
    seasons: int = 0
    ratings: list = field(default_factory = lambda: [])

    def episodes(self):
        return max([len(episodes) for episodes in self.ratings])
    
    def season_average(self, season):
        ratings = self.ratings[season]
        average = sum(ratings) / len(ratings)
        return f'{average:.1f}'

class Grid:

    def __init__(self, grid_size: Size, cell_size: Size):

        self.grid_size = grid_size
        self.cell_size = cell_size

        #self.rating_offset = Offset(2, 4)
        #self.episode_offset = Offset(2, 3)
        #self.season_offset = Offset(1, 4)

        self.rating_offset = Offset(1, 1)
        self.episode_offset = Offset(1, 0)
        self.season_offset = Offset(0, 1)

    def image_size(self):

        # grid + label (1) + margin (2)

        return Size (
            (self.grid_size.width + 3) * (self.cell_size.width + 1),
            (self.grid_size.height + 1) * (self.cell_size.height + 1)
        )
        
    def location(self, col, row):

        return Point (
            col * (self.cell_size.width + 1),
            row * (self.cell_size.height + 1)
        )

    def offset_location(self, col, row, offset):
        return self.location(col + offset.col, row + offset.row)

    def episode(self, episode):
        return self.offset_location(episode, 0, self.episode_offset)

    def rating(self, season, episode):
        return self.offset_location(episode, season, self.rating_offset)

    def season(self, season):
        return self.offset_location(0, season, self.season_offset)
    
    def season_average(self, season):
        return self.rating(season, self.grid_size.width + 1)

    def title(self):
        return self.location(1, 1)
