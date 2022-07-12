from generator import Artwork
from circles import CirclesArtwork
from PIL import Image

artwork1 = Artwork()
artwork2 = CirclesArtwork()

new_artwork = Image.blend(artwork1.image, artwork2.image, 0.5)

new_artwork.save("blend.png")
