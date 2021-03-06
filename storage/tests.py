"""
Test cases for `actions` of the `storage` app
"""

from django.test import TestCase

from storage import models
from storage import actions


class ActionsTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Authors
        herman_melville = models.Author.objects.create(
            first_name='Herman',
            last_name='Melville',
            email='herman@melville.writer'
        )
        mary_shelley = models.Author.objects.create(
            first_name='Mary',
            last_name='Shelley',
            email='mary@shelley.writer'
        )
        howard_lovecraft = models.Author.objects.create(
            first_name='Howard',
            last_name='Lovecraft',
            email='howard@lovecraft.writer'
        )
        # Books
        models.Book.objects.create(
            author=herman_melville,
            title='Moby-Dick; or, The Whale'
        )
        models.Book.objects.create(
            author=mary_shelley,
            title='Frankenstein: or, The Modern Prometheus'
        )
        models.Book.objects.create(
            author=howard_lovecraft,
            title='The Call of Cthulhu'
        )
        models.Book.objects.create(
            author=howard_lovecraft,
            title='The Shadow Over Innsmouth'
        )

    def test_all_authors(self):
        all_authors = [
            'Herman Melville',
            'Mary Shelley',
            'Howard Lovecraft'
        ]
        self.assertListEqual(actions.all_authors(), all_authors)

    def test_all_books(self):
        all_books = [
            'Moby-Dick; or, The Whale',
            'Frankenstein: or, The Modern Prometheus',
            'The Call of Cthulhu',
            'The Shadow Over Innsmouth'
        ]
        self.assertListEqual(actions.all_books(), all_books)

    def test_books_by_authors(self):
        books_by_authors = {
            'Herman Melville': [
                'Moby-Dick; or, The Whale'
            ],
            'Mary Shelley': [
                'Frankenstein: or, The Modern Prometheus'
            ],
            'Howard Lovecraft': [
                'The Call of Cthulhu',
                'The Shadow Over Innsmouth'
            ]
        }
        self.assertDictEqual(actions.books_by_authors(), books_by_authors)

    def test__db_table_exists(self):
        self.assertTrue(actions._db_table_exists(models.Author))
        self.assertTrue(actions._db_table_exists(models.Book))
