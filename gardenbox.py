from gardenboxclass import GardenBox
import sqlite3
import math

conn = sqlite3.connect('garden_box.sqlite')
cursor = conn.cursor()
gb = GardenBox(conn)

print ("hello welcome to gardenbox!")

# get length
gb.get_length()

# get width
gb.get_width()

# do math to make area
gb.set_area()

# tell the user the list of plants
# ask user which plants they'd like to add
## do crop calculation
gb.crop_calc()


conn.commit() # similar to .ExecuteNonQuery() ?
conn.close()