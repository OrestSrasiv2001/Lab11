from DisneylandDisneylandManager.AttractionManagerImpl import AttractionManagerImpl
from Attraction.Child import Child
from Attraction.enums.DangerLevel import DangerLevel
from Attraction.Disneyland import Disneyland
from Attraction.Karting import Karting
from Attraction.RollerCoaster import RollerCoaster


def main():

    attraction_manager = AttractionManagerImpl()

    disneyland = Disneyland(120, 20, DangerLevel.LOW, 2000, 51.3456, 4.5)
    karting = Karting(150.50, 20, DangerLevel.MAXIMUM, 10, "Mazda", "Carbon")
    rollercoaster = RollerCoaster(200, 50, DangerLevel.MIDDLE, 100, 15, "plastic")
    child = Child(100, 3, DangerLevel.HIGH, 10, 65, 120)


    attraction_manager.add_element_to_list(child)
    attraction_manager.add_element_to_list(disneyland)
    attraction_manager.add_element_to_list(karting)
    attraction_manager.add_element_to_list(rollercoaster)


    print(*attraction_manager.sort_attraction_by_price(True))
    print(*attraction_manager.sort_attraction_by_price(False))
    print(*attraction_manager.sort_max_number_of_visitors(True))
    print(*attraction_manager.sort_max_number_of_visitors(False))

    print(*attraction_manager.find_attraction(danger_level= DangerLevel.HIGH))


if __name__ == "__main__":
    main()


