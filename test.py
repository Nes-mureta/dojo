import unittest
from dojo import Dojo

class TestDojo(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_create_room_office(self):
        print("\nTesting: create_room (office)")
        result = self.dojo.create_room('office', 'Blue')
        self.assertIn("an office called 'blue' has been successful created.", result.lower())
        self.assertEqual(len(self.dojo.offices), 1)

    def test_create_room_living_space(self):
        print("\nTesting: create_room (living_space)")
        result = self.dojo.create_room('living_space', 'Red')
        self.assertIn("living space called 'Red'", result)
        self.assertEqual(len(self.dojo.living_spaces), 1)

    def test_create_room_invalid(self):
        print("\nTesting: create_room (invalid type)")
        result = self.dojo.create_room('invalid', 'Nope')
        self.assertIn("invalid room type", result.lower())

    def test_add_person_staff(self):
        print("\nTesting: add_person (staff)")
        self.dojo.create_room('office', 'Blue')
        result = self.dojo.add_person('Alice', 'STAFF')
        self.assertTrue(any("Alice" in s for s in result))

    def test_add_person_fellow(self):
        print("\nTesting: add_person (fellow)")
        self.dojo.create_room('office', 'Blue')
        self.dojo.create_room('living_space', 'Red')
        result = self.dojo.add_person('Bob', 'FELLOW', 'YES')
        self.assertTrue(any("Bob" in s for s in result))

    def test_add_person_invalid_role(self):
        print("\nTesting: add_person (invalid role)")
        result = self.dojo.add_person('Charlie', 'JANITOR')
        self.assertTrue(any("invalid role" in s.lower() for s in result))

    def test_add_person_staff_wants_living_space(self):
        print("\nTesting: add_person (staff wants living space)")
        result = self.dojo.add_person('Dana', 'STAFF', 'YES')
        self.assertTrue(any("staff cannot allocated living space" in s.lower() for s in result))

    def test_list_allocations(self):
        print("\nTesting: list_allocations")
        self.dojo.create_room('office', 'Blue')
        self.dojo.add_person('Alice', 'STAFF')
        allocations = self.dojo.list_allocations()
        self.assertTrue(any("Blue" in s for s in allocations))

    def test_list_rooms(self):
        print("\nTesting: list_rooms")
        self.dojo.create_room('office', 'Blue')
        self.dojo.create_room('living_space', 'Red')
        offices = self.dojo.list_rooms('office')
        living_spaces = self.dojo.list_rooms('living_space')
        self.assertEqual(len(offices), 1)
        self.assertEqual(len(living_spaces), 1)

    def test_list_people(self):
        print("\nTesting: list_people")
        self.dojo.add_person('Alice', 'STAFF')
        self.dojo.add_person('Bob', 'FELLOW')
        all_people = self.dojo.list_people()
        staff = self.dojo.list_people('STAFF')
        fellows = self.dojo.list_people('FELLOW')
        self.assertEqual(len(all_people), 2)
        self.assertEqual(len(staff), 1)
        self.assertEqual(len(fellows), 1)

if __name__ == '__main__':
    unittest.main()