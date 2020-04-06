from gardenboxclass import GardenBox
import sqlite3
import math

conn = sqlite3.connect('garden_box.sqlite')
cursor = conn.cursor()
gb = GardenBox(conn)

def test_length():
    assert gb.set_length(3) == 3

def test_area():
    assert gb.set_area(2, 2) == 4


# from gardenboxclass import GardenBox
# import unittests

# class MyTest(unittest.TestCase):
#     def test(self):
#         get_length()
#         get_width()
#         self.assertEqual(set_area(), 4)