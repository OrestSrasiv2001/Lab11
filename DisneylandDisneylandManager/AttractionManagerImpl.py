class AttractionManagerImpl:
    attraction_list = []

    def __init__(self):
        pass

    def add_element_to_list(self, attraction):
        self.attraction_list.append(attraction)

    def sort_attraction_by_price(self, reverse):
        return sorted(self.attraction_list, key=lambda attraction: attraction.price_of_ticket, reverse=reverse)

    def sort_max_number_of_visitors(self, reverse):
        return sorted(self.attraction_list, key=lambda attraction: attraction.max_number_of_visitors, reverse=reverse)

    def find_attraction(self, danger_level):
        return list(filter(lambda attraction: attraction.danger_level == danger_level, self.attraction_list))

    def show_elements_inl_list(self):
        for elements in self.attraction_list:
            print(elements)

    def __del__(self):
        pass