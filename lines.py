from generator import Artwork
from PIL import ImageDraw
import random
import math


class LinesArtwork(Artwork):
    def generate(self):
        draw = ImageDraw.Draw(self.image)

        for (x, y) in self.get_random_points():
            color = self.get_color_at_point(x, y)

            # draw lines at random angles instead of pixels
            length = random.randint(2, 10)
            angle = random.uniform(0, 3.141)

            coordinate_x = length * math.sin(angle)
            coordinate_y = length * math.cos(angle)

            draw.line(
                [
                    (x - coordinate_x, y - coordinate_y),
                    (x + coordinate_x, y + coordinate_y),
                ],
                fill=color,
            )
