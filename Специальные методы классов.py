class House:
    def __init__(set):
        set.numberOfFloors = 0

    def setNewNumberOfFloors(set, floors):
        set.numberOfFloors = floors
        print("Number of floors:", int(set.numberOfFloors))


my_house = House()
my_house.setNewNumberOfFloors(2)
my_house.setNewNumberOfFloors(6)