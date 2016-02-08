import datetime
import json
import sys

from popolo.models import Person
from popolo_name_resolver.resolve import (
    delete_entities, recreate_entities, ResolvePopoloName
)

from unittest import TestCase


class ResolvePopitNameTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ResolvePopitNameTest, cls).setUpClass()
        # Create some Popolo people:
        cls.john_q = Person.objects.create(
            name='John Quentin Smith',
        )
        Person.objects.create(
            name='John Smith',
        )
        # And create lots of EntityName objects for looking them up.
        recreate_entities(verbose=False)

    @classmethod
    def tearDownClass(cls):
        delete_entities()
        Person.objects.all().delete()

    def test_aaa(self):
        self.assertTrue(True) # dummy pass, to prevent annoying stacktrace of SQL DDL if first test fails

    def test_resolve(self):

        resolver = ResolvePopoloName(
                date = datetime.date(month=11, year=2010, day=1) )

        popolo_person = resolver.get_person('J Q Smith')
        self.assertEqual(self.john_q, popolo_person)