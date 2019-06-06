from Attraction.Attraction import Attraction


class Disneyland(Attraction):
    def __init__(self, price_of_ticket, max_number_of_visitors, danger_level, area, location, number_attractions):
        super().__init__(price_of_ticket, max_number_of_visitors, danger_level)
        self.area = area
        self.location= location
        self.number_attractions = number_attractions

    def __str__(self):
        return super().__str__() \
               + "\nArea:" + str(self.area) \
               + "\nLocation: " + str(self.location) \
               + "\nNumber_attractions: " + str(self.number_attractions)

    def __del__(self):
        pass