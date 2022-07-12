import os
from generator import Artwork
from circles import CirclesArtwork
from blocks import BlocksArtwork
from lines import LinesArtwork

print("generating sample images...")

os.makedirs("sample", exist_ok=True)

for i in range(1, 6):
    filepath = os.path.join("sample", f"gradient-{i}.png")
    artwork = Artwork()
    artwork.save(filepath)

for c in range(1, 6):
    filepath = os.path.join("sample", f"circles-{c}.png")
    artwork = CirclesArtwork()
    artwork.save(filepath)

for b in range(1, 6):
    filepath = os.path.join("sample", f"blocks-{b}.png")
    artwork = BlocksArtwork()
    artwork.save(filepath)

for l in range(1, 6):
    filepath = os.path.join("sample", f"lines-{l}.png")
    artwork = LinesArtwork(debug=True)
    artwork.save(filepath)
