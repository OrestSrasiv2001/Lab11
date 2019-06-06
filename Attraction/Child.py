from Attraction.Attraction import Attraction


class Child(Attraction):
    def __init__(self, price_of_ticket, max_number_of_visitors, danger_level,age, weight, height):
        super().__init__(price_of_ticket, max_number_of_visitors,danger_level)
        self.age = age
        self.weight = weight
        self.height = height

    def __str__(self):
        return super().__str__()\
               + "\nAge:" + str(self.age)\
               + "\nWeight: " + str(self.weight)\
               + "\nHeight: " + str(self.height)

    def __del__(self):
        pass