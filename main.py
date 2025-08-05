__doc__ = """

Usage:
  create_room <room_type> <room_name>...
  add_person <person_name> <role> [<wants_living_space>]
  exit
  (-h | --help)

Options:
  -h --help     Show this screen.
"""

from docopt import docopt, DocoptExit
from dojo import Dojo

def main():
    dojo = Dojo.load_state()
    print("Dojo Allocation System. Type '--help' for options")
    
    while True:
        try:
            user_input = input("Dojo >> ").strip()
            if not user_input:
                continue
            if user_input.lower() == 'exit':
                dojo.save_state()
                print("Exiting Dojo...")
                break
            if user_input in ['-h', '--help']:
                print(__doc__)
                continue
                
            # Manually parse commands and array arguments in indexes
            parts = user_input.split()
            command = parts[0].lower()
            
            if command == 'create_room' and len(parts) >= 3:
                room_type = parts[1]
                for name in parts[2:]:
                    print(dojo.create_room(room_type, name))
                dojo.save_state()
            
            elif command == 'add_person' and len(parts) >= 3:
                name = parts[1]
                role = parts[2]
                wants = parts[3] if len(parts) > 3 else 'NO'
                for line in dojo.add_person(name, role, wants):
                    print(line)
                dojo.save_state()
            
            else:
                print("Command not recognized. The available commands are:\ncreate_room <office|living_space> <name>\nadd_person <name> <STAFF|FELLOW> [YES|NO]\nexit")
    
                
        except KeyboardInterrupt:
            print("\n Exiting Dojo...")
            dojo.save_state()
            break


if __name__ == "__main__":
    main()