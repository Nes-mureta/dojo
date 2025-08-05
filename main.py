"""
Usage:
  main.py create_room <room_type> <room_name>...
  main.py add_person <person_name> <role> [<wants_living_space>]

Options:
  -h --help     Show this screen.
"""

from docopt import docopt
from dojo import Dojo

if __name__ == "__main__":
    args = docopt(__doc__)
    dojo = Dojo.load_state()

    if args['create_room']:
        room_type = args['<room_type>']
        for name in args['<room_name>']:
            print(dojo.create_room(room_type, name))
            dojo.save_state()

    elif args['add_person']:
        name = args['<person_name>']
        role = args['<role>']
        wants = args['<wants_living_space>'] or 'No'
        for line in dojo.add_person(name, role, wants):
            print(line)
        dojo.save_state()
