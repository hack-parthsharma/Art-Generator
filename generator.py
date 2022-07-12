from PIL import Image, ImageDraw, ImageFont
from noise import pnoise2  # 2 dimensions
import random
import colorsys  # library to convert between color systems


class Artwork:
    def __init__(
        self, size=500, grain_level=0.1, noise_level=1.5, noise_shift=2.0, debug=False
    ):
        self.image = Image.new("RGBA", (size, size))
        self.palette = (
            # top-left
            self.get_random_color(),
            # top-right
            self.get_random_color(),
            # bottom-left
            self.get_random_color(),
            # bottom-right
            self.get_random_color(),
        )
        self.grain_level = grain_level
        self.noise_base = random.randint(0, 999)
        self.noise_level = noise_level
        self.noise_shift = noise_shift
        self.debug = debug

        self.generate()
        if self.debug:
            self.add_debug()

    def get_random_points(self):
        # instead of going through the canvas from left to right, top to bottom (looping through width and height), we want to get a list of all the possible points and randomly place the pixels
        points = []
        for x in range(self.image.width):
            for y in range(self.image.height):
                points.append((x, y))

        random.shuffle(points)

        return points

    def generate(self):
        for (x, y) in self.get_random_points():
            color = self.get_color_at_point(x, y)
            self.image.putpixel((x, y), color)

    def get_random_grain(self):
        if self.grain_level > 0:
            return random.uniform(-1 * self.grain_level, self.grain_level)
        else:
            return 0

    def make_noise(self, px, py):
        return self.noise_level * pnoise2(
            px * self.noise_shift, py * self.noise_shift, base=self.noise_base
        )

    def get_color_at_point(self, x, y):
        (top_left, top_right, bottom_left, bottom_right) = self.palette

        percentage_x = x / self.image.width
        percentage_y = y / self.image.height

        # add grain (pure randomness)
        grain_x = self.get_random_grain()
        grain_y = self.get_random_grain()

        # add noise/distortion ()
        noise_x = self.make_noise(percentage_x, percentage_y)
        noise_y = self.make_noise(percentage_x, percentage_y)

        # mix top-left and top-right colors into a linear horizontal gradient
        gradient1 = self.mix_color(
            top_left, top_right, percentage_x + grain_x + noise_x
        )
        # mix bottom-left and bottom-right colors into a linear horizontal gradient
        gradient2 = self.mix_color(
            bottom_left, bottom_right, percentage_x + grain_x + noise_x
        )

        # take both gradients and mix into a linear vertical gradient
        gradient = self.mix_color(
            gradient1, gradient2, percentage_y + grain_y + noise_y
        )

        return gradient

    def mix_color(self, color1, color2, mixer):
        (r1, g1, b1, a1) = color1
        (r2, g2, b2, a2) = color2

        # make sure 'mixer' (percentage) is between 0 and 1
        mixer = max(0, min(mixer, 1))

        return (
            self.mix_channel(r1, r2, mixer),
            self.mix_channel(g1, g2, mixer),
            self.mix_channel(b1, b2, mixer),
            self.mix_channel(a1, a2, mixer),
        )

    def mix_channel(self, channel1, channel2, mixer):
        return int(channel1 + (channel2 - channel1) * mixer)

    def get_random_color(self):
        # using HSV instead of RGB to get brighter colors
        h = random.uniform(0, 1)  # hue/color
        s = random.uniform(0.5, 1)  # saturation
        v = random.uniform(0.9, 1)  # value/brightness

        (r, g, b) = colorsys.hsv_to_rgb(h, s, v)

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        return (r, g, b, 255)

    def add_debug(self):
        draw = ImageDraw.Draw(self.image)

        (top_left, top_right, bottom_left, bottom_right) = self.palette
        draw.rectangle([16, 16, 24, 24], fill=top_left)
        draw.rectangle([32, 16, 40, 24], fill=top_right)
        draw.rectangle([48, 16, 56, 24], fill=bottom_left)
        draw.rectangle([64, 16, 72, 24], fill=bottom_right)

        messages = [
            "Generated artwork:",
            f"Grain level: {self.grain_level}",
            f"Noise level: {self.noise_level}",
            f"Noise shift: {self.noise_shift}",
        ]

        font = ImageFont.truetype("ibm-plex-mono.ttf", 16)

        draw.multiline_text(
            (16, 32), "\n".join(messages), font=font, fill=(0, 0, 0, 255)
        )

    def save(self, filepath):
        self.image.save(filepath)
