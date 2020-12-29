from src.sample.zad03.friend_ships import FriendShips


class FriendShipsStorage:
    def __init__(self):
        self.storage = FriendShips()

    def makeFriends(self, person1, person2):
        return self.storage.makeFriends(person1, person2)

    def getFriendsList(self, person):
        return self.storage.getFriendsList(person)

    def areFriends(self, person1, person2):
        return self.storage.areFriends(person1, person2)

    def addFriend(self, person, friend):
        return self.storage.addFriend(person, friend)
