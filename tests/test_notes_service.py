import unittest
from src.sample.zad02.notes_service import NotesService
from src.sample.zad02.note import Note
from unittest.mock import *


class TestNote(unittest.TestCase):
    def test_add(self):
        note = Note(5.0, "Kasia")
        test_object = NotesService()
        test_object.add = MagicMock(return_value=note)
        self.assertEqual(test_object.add(note), note)

    def test_clear(self):
        test_object = NotesService()
        test_object.clear = MagicMock(return_value=[])
        self.assertEqual(test_object.clear(), [])

    def test_get_all_notes_off(self):
        test_object = NotesService()
        test_object.averageOf = MagicMock(return_value=3.75)
        self.assertEqual(test_object.averageOf("Marlena"), 3.75)

    def test_get_all_notes_off_error(self):
        test_object = NotesService()
        test_object.averageOf = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, test_object.averageOf, "Marlena")