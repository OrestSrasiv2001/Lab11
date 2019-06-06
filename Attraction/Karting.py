from Attraction.Attraction import Attraction


class Karting(Attraction):
    def __init__(self, price_of_ticket, max_number_of_visitors, danger_level,number_of_cars, name,  type_of_covering):
        super().__init__(price_of_ticket, max_number_of_visitors,danger_level)
        self.number_of_cars = number_of_cars
        self.name = name
        self.type_of_covering = type_of_covering

    def __str__(self):
        return super().__str__() \
               + "\nNumber_of_cars:" + str(self.number_of_cars) \
               + "\nName: " + str(self.name) \
               + "\nType_of_covering: " + self.type_of_covering

    def __del__(self):
        pass