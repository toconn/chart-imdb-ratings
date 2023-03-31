from PIL import Image
from PIL.Image import merge
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype

from data import Point, Size


FONT = truetype('Calibri', 16)

BLACK = (0, 0, 0)
DARK_GREEN = (37, 120, 67)
GREEN = (114, 172, 106)
YELLOW = (251, 222, 104)
ORANGE = (237, 121, 61)
RED = (197, 39, 62)
WHITE = (255, 255, 255)

CELL_SIZE = Size(32, 22)
TITLE_SIZE = Size(160, 22)


def center(outer: Size, inner: Size) -> Point:
    x = (outer.width - inner.width) // 2
    y = (outer.height - inner.height) // 2
    return Point(x, y)

def get_colors(rating):
    ''' Returns foreground, backgroud for the given rating.
    '''
	
    if rating < 6:
        return WHITE, RED
    
    if rating < 7:
        return BLACK, ORANGE
    
    if rating < 8:
        return BLACK, YELLOW
    
    if rating < 8.5:
        return BLACK, GREEN
    
    return WHITE, DARK_GREEN

def to_boxed_text(text, foreground, background):

    image = Image.new('RGBA', CELL_SIZE, background)
    
    draw = Draw(image)

    text_size = Size(*draw.textsize(str(text), font = FONT))
    position = center(CELL_SIZE, text_size)

    draw.text(position, str(text), foreground, font = FONT)  

    return image

def to_boxed_rating(rating):

    foreground, background = get_colors(float(rating)) 
    return to_boxed_text(rating, foreground, background)

def to_text(text, foreground, background):

    image = Image.new('RGBA', TITLE_SIZE, background)
    
    draw = Draw(image)
    draw.text((2, 4), str(text), foreground, font = FONT)  

    return image