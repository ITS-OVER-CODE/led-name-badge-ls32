from lednamebadge import SimpleTextAndIcons, LedNameBadge
from array import array

# Create a SimpleTextAndIcons instance
creator = SimpleTextAndIcons()

# Generate bitmaps from the starfield images
starfield_020_bitmap = creator.bitmap("gfx/starfield/starfield_020.png")
starfield_040_bitmap = creator.bitmap("gfx/starfield/starfield_040.png")
starfield_080_bitmap = creator.bitmap("gfx/starfield/starfield_080.png")
starfield_120_bitmap = creator.bitmap("gfx/starfield/starfield_120.png")
starfield_160_bitmap = creator.bitmap("gfx/starfield/starfield_160.png")
starfield_200_bitmap = creator.bitmap("gfx/starfield/starfield_200.png")

# Prepare lengths and buffer
lengths = (
    starfield_020_bitmap[1], 
    starfield_040_bitmap[1], 
    starfield_080_bitmap[1], 
    starfield_120_bitmap[1], 
    starfield_160_bitmap[1], 
    starfield_200_bitmap[1]
)
buf = array('B')

# Create header and add to buffer
# Setting mode to 4 and timing parameters to change scene 5 times per second (20 centiseconds per scene)
# Ensure no transition effects and steady display
header = LedNameBadge.header(lengths, (0,), (0,), (20, 20, 20, 20, 20, 20), (0, 0, 0, 0, 0, 0), 20)
buf.extend(header)

# Add bitmap data to buffer
buf.extend(starfield_020_bitmap[0])
buf.extend(starfield_040_bitmap[0])
buf.extend(starfield_080_bitmap[0])
buf.extend(starfield_120_bitmap[0])
buf.extend(starfield_160_bitmap[0])
buf.extend(starfield_200_bitmap[0])

# Write buffer to LED name badge
LedNameBadge.write(buf)
