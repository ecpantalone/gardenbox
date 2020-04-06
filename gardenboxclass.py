import math as m

class GardenBox:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    # Original functions
    def get_length(self):
        self.length = float(input ("What is the length? "))
    def get_width(self):
        self.width = float(input ("What is the width? "))
    def set_area_original(self):
        self.area = (self.width * self.length)
    def get_perimeter(self):
        self.perimeter = ((self.width * float(2)) + (self.length * float(2)))

   # Testable functions
    def set_length(self, length):
        self.length = length
        return length
    def set_width(self, width):
        self.width = width
        return width
    def set_area(self, length, width):
        self.area = (length * width)
        return self.area

    def crop_calc(self):
        produceChoice = input ("You can have 1. carrots, 2. corn, or 3. beets in your garden, which would you like? choose 1, 2, or 3\n")
        sqlString = "SELECT Vegetable_Name, Planting_Ratio FROM Vegetable_Planting_Ratios WHERE VegetableID = '{}' AND EXISTS(SELECT 1 FROM Vegetable_Planting_Ratios WHERE VegetableID = '{}');".format(produceChoice, produceChoice)

        self.cursor.execute(sqlString)
        result = self.cursor.fetchall()

        planting_ratio = 0
        veggie_name = ""
        for row in result:
            veggie_name = row[0]
            planting_ratio = row[1]

        if planting_ratio > 0 :
            print ("This works!")
        
            produceCalc = m.floor(planting_ratio * self.area)
            print("You can plant " + str(produceCalc) + " " + veggie_name + "(s)")
        else:
            print("invalid choice")
    
        self.cursor.close()




