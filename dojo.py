from models import Office, LivingSpace, Staff, Fellow
import random
import pickle
import os

STATE_FILE = 'dojo_state.pkl'

class Dojo:
    def __init__(self):
        self.offices = []
        self.living_spaces = []
        self.people = []
    
    def create_room(self, room_type, name):
        room_type = room_type.lower()
        if room_type == 'office':
            self.offices.append(Office(name))
            return f"An office called '{name}'has been successful created."
        elif room_type == 'living_space':
            self.living_spaces.append(LivingSpace(name))
            return f"A living space called '{name}'has been successful  created."
        return "Invalid room type. Use 'office' or 'living_space'."
    
    def add_person(self, name, role, wants_living_space='NO'):
        output = []
        role = role.upper()
        wants = wants_living_space.upper()
        
        if role not in ['STAFF', 'FELLOW']:
            return ["Invalid role. Must be STAFF or FELLOW"]
        
        if role == 'STAFF' and wants == 'YES':
            return ["Staff cannot allocated living space"]
        
        person = Staff(name) if role == 'STAFF' else Fellow(name, wants)
        self.people.append(person)
        output.append(f"A{role} {name} added successfully")
        
        # Assign office
        if self.offices:
            office = random.choice(self.offices)
            if len(office.occupants) < office.capacity:
                office.occupants.append(person)
                output.append(f"Assigned to office: {office.name}")
            else:
                output.append("No office space available")
        else:
            output.append("No offices exists")
        
        # Assign living space if person is a Fellow
        if role == 'FELLOW' and wants == 'YES':
            if self.living_spaces:
                living = random.choice(self.living_spaces)
                if len(living.occupants) < living.capacity:
                    living.occupants.append(person)
                    output.append(f"Assigned to living space: {living.name}")
                else:
                    output.append("No living space available")
            else:
                output.append("No living spaces exists")
        
        return output
    
    def save_state(self):
        with open(STATE_FILE, 'wb') as f:
            pickle.dump(self, f)
    
    @staticmethod
    def load_state():
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, 'rb') as f:
                return pickle.load(f)
        return Dojo()