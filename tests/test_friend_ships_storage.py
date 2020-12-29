import unittest
from unittest.mock import MagicMock
from src.sample.zad03.friend_ships_storage import FriendShipsStorage


class TestFriendShipsStorage(unittest.TestCase):
    def setUp(self):
        self.temp = FriendShipsStorage()

    def test_make_friend(self):
        self.temp.storage = MagicMock()
        self.temp.makeFriends("Kasia", "Marlena")
        self.temp.storage.makeFriends.assert_called_once_with("Kasia", "Marlena")

    def test_raise_make_friend(self):
        self.temp.storage.makeFriends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.makeFriends, 123, "Kasia")

    def test_get_friends_list(self):
        self.temp.storage = MagicMock()
        self.temp.getFriendsList("Kasia")
        self.temp.storage.getFriendsList.assert_called_once_with("Kasia")

    def test_raise_friends_list(self):
        self.temp.storage.getFriendsList = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.getFriendsList, "Someone")

    def test_are_friends(self):
        self.temp.storage = MagicMock()
        self.temp.areFriends("Kasia", "Ola")
        self.temp.storage.areFriends.assert_called_once_with("Kasia", "Ola")

    def test_raise_are_friends_exception(self):
        self.temp.storage.getFriendsList = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.areFriends, "Kasia", "Ewa")

    def test_raise_are_friends_type_error(self):
        self.temp.storage.getFriendsList = MagicMock(side_effect=TypeError)
        self.assertRaises(Exception, self.temp.areFriends, "Kasia", 90)

    def test_add_friend(self):
        self.temp.storage = MagicMock()
        self.temp.addFriend("Kasia", "Ola")
        self.temp.storage.addFriend.assert_called_once_with("Kasia", "Ola")

    def test_raise_add_friend(self):
        self.temp.storage.addFriend = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addFriend, ["Kasia"], "Janek")

    def tearDown(self):
        self.temp = None
