from generator import Artwork
from PIL import ImageDraw
import random


class CirclesArtwork(Artwork):
    def generate(self):
        draw = ImageDraw.Draw(self.image)

        for (x, y) in self.get_random_points():
            color = self.get_color_at_point(x, y)

            # draw circles with random radius instead of pixels
            radius = random.randint(2, 10)

            draw.ellipse(
                [(x - radius, y - radius), (x + radius, y + radius)], fill=color
            )
