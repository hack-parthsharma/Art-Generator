from generator import Artwork
from PIL import ImageDraw
import random


class BlocksArtwork(Artwork):
    def generate(self):
        draw = ImageDraw.Draw(self.image)

        for (x, y) in self.get_random_points():
            color = self.get_color_at_point(x, y)

            # draw rectangles with random widths and heights instead of pixels
            width = random.randint(2, 10)
            height = random.randint(2, 10)

            draw.rectangle(
                [(x - width, y - height), (x + width, y + height)], fill=color
            )
