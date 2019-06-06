class Attraction:

    def __init__(self, price_of_ticket, max_number_of_visitors, danger_level):
        self.price_of_ticket = price_of_ticket
        self.max_number_of_visitors = max_number_of_visitors
        self.danger_level = danger_level

    def __str__(self):
        return "\nPrice_of_ticket:  " + str(self.price_of_ticket) \
               + "\nMax_number_of_visitors: " + str(self.max_number_of_visitors) \
               + "\nDanger_level: " + str(self.danger_level)

    def __del__(self):
        pass
