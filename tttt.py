from lednamebadge import SimpleTextAndIcons, LedNameBadge
from array import array

# Create a SimpleTextAndIcons instance
creator = SimpleTextAndIcons()

# Generate bitmaps from text, icons, and an image file
scene_x_bitmap = creator.bitmap("I.T.S_O.V.E.R")
scene_y_bitmap = creator.bitmap("gfx/starfield/starfield_020.png")
scene_c_bitmap = creator.bitmap("gfx/starfield/starfield_040.png")
scene_a_bitmap = creator.bitmap("gfx/starfield/starfield_080.png")
scene_b_bitmap = creator.bitmap("gfx/starfield/starfield_120.png")
scene_d_bitmap = creator.bitmap("gfx/starfield/starfield_160.png")
scene_e_bitmap = creator.bitmap("gfx/starfield/starfield_200.png")

# Prepare lengths and buffer
lengths = (scene_x_bitmap[1], scene_y_bitmap[1], scene_c_bitmap[1])
buf = array('B')

# Create header and add to buffer
header = LedNameBadge.header(lengths, (3,), (0,), (0, 1, 0), (0, 0, 1), 100)
buf.extend(header)

# Add bitmap data to buffer
buf.extend(scene_x_bitmap[0])
buf.extend(scene_y_bitmap[0])
buf.extend(scene_c_bitmap[0])
buf.extend(scene_a_bitmap[0])
buf.extend(scene_b_bitmap[0])
buf.extend(scene_d_bitmap[0])
buf.extend(scene_e_bitmap[0])

# Write buffer to LED name badge
LedNameBadge.write(buf)
