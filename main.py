__doc__ = """

Usage:
  create_room <room_type> <room_name>...
  add_person <person_name> <role> [<wants_living_space>]
  list_allocations <room_type> <room_name>
  list_rooms <room_type>
  list_people <role> 
  exit
  (-h | --help)

Options:
  -h --help     Show this screen.
"""

from docopt import docopt, DocoptExit
from tabulate import tabulate
from dojo import Dojo

def main():
    dojo = Dojo.load_state()
    print("Dojo Allocation System. Type '--help' for options or 'exit' to quit.")
    
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
                
            
            elif command =='list_allocations':
                if len(parts) ==3:
                    room_type = parts[1]
                    room_name = parts[2]
                    allocations = dojo.list_allocations(room_type, room_name)
                    if allocations:
                        print(f"Allocations for {room_type} '{room_name}':")
                        table_data = [[i + 1, alloc] for i, alloc in enumerate(allocations)]
                        print(tabulate(table_data, headers=["#", "Allocations"], tablefmt="fancy_grid"))    
                    else:
                        print(f"No allocations found for {room_type} '{room_name}'.")
                elif len(parts) == 2:
                    room_type = parts[1]
                    allocations = dojo.list_allocations(room_type)
                    if allocations:
                        print(f"Allocations for {room_type}:")
                        table_data = [[i + 1, alloc] for i, alloc in enumerate(allocations)]
                        print(tabulate(table_data, headers=["#", "Allocations"], tablefmt="fancy_grid"))
                    else:
                        print(f"No allocations found for {room_type}.")
                elif len(parts)==1:
                    all_allocations = dojo.list_allocations()
                    if all_allocations:
                        print("All Allocations:")
                        table_data = [[i + 1, alloc] for i, alloc in enumerate(all_allocations)]
                        print(tabulate(table_data, headers=["#", "Allocations"], tablefmt="fancy_grid")) 
                    else:
                        print("No allocations found.")
                            
                            
            elif command == 'list_rooms':
                if len(parts) == 2:
                    room_type = parts[1]
                    rooms = dojo.list_rooms(room_type)
                    if rooms:
                       print(f"\n{room_type.capitalize()} Rooms:")
                       table_data = [[i + 1, room] for i, room in enumerate(rooms)]
                       print(tabulate(table_data, headers=["#", "Room Name"], tablefmt="fancy_grid"))
                    else:
                        print(f"No {room_type} rooms found.")
                else:
                    all_rooms = dojo.list_rooms()
                    if all_rooms:
                           print("\nAll Rooms:")
                           table_data = [[i + 1, room] for i, room in enumerate(all_rooms)]
                           print(tabulate(table_data, headers=["#", "Room Name"], tablefmt="fancy_grid"))
                    else:
                        print("No rooms found.")
                        
            elif command == 'list_people':
                if len(parts) == 2:
                    role = parts[1]
                    people = dojo.list_people(role)
                    if people:
                        print(f"\n{role.capitalize()}s:")
                        table_data = [[i + 1, person] for i, person in enumerate(people)]
                        print(tabulate(table_data, headers=["#", "Name"], tablefmt="fancy_grid"))
                        
                    else:
                        print(f"No {role} found.")
                else:
                    all_people = dojo.list_people()
                    if all_people:
                        print("\nAll People:")
                        table_data = [[i + 1, person] for i, person in enumerate(all_people)]
                        print(tabulate(table_data, headers=["#", "Name"], tablefmt="fancy_grid"))
                    else:
                        print("No people found.")
                
                
            
            else:
                print("Command not recognized. The available commands are:\ncreate_room <office|living_space> <name>\nadd_person <name> <STAFF|FELLOW> [YES|NO]\nexit")
    
                
        except KeyboardInterrupt:
            print("\n Exiting Dojo...")
            dojo.save_state()
            break


if __name__ == "__main__":
    main()