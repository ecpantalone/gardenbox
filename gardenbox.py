from gardenboxclass import GardenBox
import sqlite3
import math

conn = sqlite3.connect('garden_box.sqlite')
cursor = conn.cursor()
gb = GardenBox(conn)

print ("hello welcome to gardenbox!")


user_length = float(input("What is the length? "))
gb.set_length(user_length)
# gb.length now populated

# # get length
# gb.get_length()

user_width = float(input("What is the width? "))
gb.set_width(user_width)
#gb.width now populated 

# # get width
# gb.get_width()

gb.set_area(gb.length, gb.width)

# do math to make area
# gb.set_area()

# tell the user the list of plants
# ask user which plants they'd like to add
## do crop calculation
gb.crop_calc()


conn.commit() # similar to .ExecuteNonQuery() ?
conn.close()