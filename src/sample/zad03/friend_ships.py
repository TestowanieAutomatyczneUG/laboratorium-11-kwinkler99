class FriendShips:
    def __init__(self):
        self.ships = {}

    def makeFriends(self, person1, person2):
        if type(person1) == str and type(person2) == str:
            self.addFriend(person1, person2)
            self.addFriend(person2, person1)
            return self.ships
        else:
            raise TypeError

    def getFriendsList(self, person):
        if type(person) == str and person in self.ships.keys():
            return self.ships[person]
        else:
            raise Exception("Wrong person")

    def areFriends(self, person1, person2):
        if type(person1) == str and type(person2) == str:
            if person2 in self.ships.keys() and person1 in self.ships.keys():
                if person2 in self.ships[person1]:
                    return True
                else:
                    return False
            else:
                raise Exception("At least one person does not exist")
        else:
            raise TypeError

    def addFriend(self, person, friend):
        if type(person) == str and type(friend) == str:
            if person in self.ships.keys():
                self.ships[person].append(friend)
                return "Success"
            else:
                self.ships[person] = [friend]
                return "Success"
        else:
            raise TypeError


