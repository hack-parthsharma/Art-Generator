import os
from generator import Artwork

print("generating exports...")

os.makedirs("exports", exist_ok=True)

filepath = os.path.join("exports", "export.png")

artwork = Artwork(size=2000)
artwork.save(filepath)
