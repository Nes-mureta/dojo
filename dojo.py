from models import Office,LivingSpace,Staff, Fellow
import random
import pickle
import os

STATE_FILE='dojo_state.pkl'

class Dojo:
    def __init__(self):
      self.offices = []
      self.living_spaces = []
      self.people = []
    
    def create_room(self, room_type, name):
      room_type = room_type.lower()
      if room_type== 'office':
        self.offices.append(Office(name))
        return f"An office called '{name}' created."
      elif room_type == 'living_space':
        self.living_spaces.append(LivingSpace(name))
        return f"A living space called '{name}' created."
      else:
        return "Invalid room type. Use 'office' or 'living_space'."
      
      
      
    def add_person(self, name, role, wants_living_space='No'):
      output = []
      if role.upper()=='STAFF':
        person= Staff(name)
        output.append(f'Staff {name} has been successfull added.')
      elif role.upper() == 'FELLOW':
        person = Fellow(name, wants_living_space)
        output.append(f'Fellow {name} has been successfully added.')
      else:
        return ["Invalid role. role must be 'FELLOW' or 'STAFF'."]
                
      self.people.append(person)
      
      if self.offices:
        Office=random.choice(self.offices)
        Office.occupants.append(person)
        output.append(f"{person.first_name} has been assigned to office '{Office.name}'.")
      else:
        output.append(f"No offices available for {person.first_name}.")
        
        
      if isinstance(person,Fellow) and person.wants_living_space:
        if self.living_spaces:
          LivingSpace=random.choice(self.living_spaces)
          LivingSpace.occupants.append(person)
          output.append(f"{person.first_name} has been assigned to living space '{LivingSpace.name}'.")
        else:
          output.append(f"No living spaces available for {person.first_name}.")
      return output
    def save_state(self):
      with open(STATE_FILE, 'wb') as f:
        pickle.dump(self, f)
    @staticmethod
    def load_state():
      if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'rb') as f:
          return pickle.load(f)
      else:
        return Dojo()
      
    
