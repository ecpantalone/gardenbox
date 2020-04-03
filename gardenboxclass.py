import math as m

class GardenBox:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def set_length(self):
        self.length = float(input ("What is the length? "))

    def set_width(self):
        self.width = float(input ("What is the width? "))

    def get_perimeter(self):
        self.perimeter = ((self.width * 2) + (self.length * 2))
        
    def get_area(self):
        self.area = (self.width * self.length)
    
    def crop_calc(self):
        produceChoice = input ("You can have 1. carrots, 2. corn, or 3. beets in your garden, which would you like? choose 1, 2, or 3\n")
        sqlString = "SELECT EXISTS(SELECT 1 FROM Vegetable_Planting_Ratios WHERE VegetableID = '{}')".format(produceChoice)
    
        self.cursor.execute(sqlString)
        result = self.cursor.fetchone()
        for row in result:
            exists = row
        
        if exists == True :
            self.cursor.execute("SELECT Vegetable_Name, Planting_Ratio FROM Vegetable_Planting_Ratios WHERE VegetableID = '{}';".format(produceChoice))

            
            records = self.cursor.fetchall()
            for row in records:
                veggie_name = row[0]
                ratio = float(row[1])
            

            produceCalc = m.floor(ratio * self.area)
            print("You can plant " + str(produceCalc) + " " + veggie_name + "(s)")
        else:
            print("invalid choice")
    
        self.cursor.close()




