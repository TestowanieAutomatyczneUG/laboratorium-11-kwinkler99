from unittest import TestCase, main
from src.sample.zad03.friend_ships import FriendShips


class testFriendShips(TestCase):
    def setUp(self):
        self.temp = FriendShips()
        self.temp.ships = {"Kasia": ["Marlena", "Ola", "Basia", "Adam"],
                           "Marlena": ["Kasia"], "Ola": ["Kasia"],
                           "Basia": ["Kasia"], "Adam": ["Kasia"]}

    def test_make_friend(self):
        self.assertEqual(self.temp.makeFriends("Marlena", "Ola"),
                         {"Kasia": ["Marlena", "Ola", "Basia", "Adam"],
                          "Marlena": ["Kasia", "Ola"], "Ola": ["Kasia", "Marlena"],
                          "Basia": ["Kasia"], "Adam": ["Kasia"]})

    def test_raise_make_friend(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 123, "Ola")

    def test_get_friends(self):
        self.assertEqual(self.temp.getFriendsList("Kasia"), ["Marlena", "Ola", "Basia", "Adam"])

    def test_raise_get_friends(self):
        self.assertRaises(Exception, self.temp.getFriendsList, "Marek")

    def test_are_friend_false(self):
        self.assertEqual(self.temp.areFriends("Basia", "Adam"), False)

    def test_are_friend_true(self):
        self.assertEqual(self.temp.areFriends("Basia", "Kasia"), True)
        
    def test_raise_are_friend(self):
        self.assertRaises(Exception, self.temp.areFriends, "Adam", "Maniek")

    def test_add_friend(self):
        self.assertEqual(self.temp.addFriend("Kasia", "Maniek"), "Success")

    def test_add_friend_two(self):
        self.assertEqual(self.temp.addFriend("Maniek", "Piotr"), "Success")

    def tearDown(self):
        self.temp = None
