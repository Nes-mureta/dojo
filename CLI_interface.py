"""
Dojo Command Line Interface

Usage:
  create_room <room_type> <room_name>...
  add_person <person_name> <FELLOW|STAFF> [<wants_accommodation>]
  -h | --help

Options:
  -h --help     Show this screen.
"""

from docopt import docopt
from dojo import Dojo

if __name__ == '__main__':
    args = docopt(__doc__)
    dojo = Dojo()

    if args['create_room']:
        room_type = args['<room_type>'].lower()
        room_names = args['<room_name>']
        for name in room_names:
            result = dojo.create_room(room_type, name)
            print(result)

    elif args['add_person']:
        name = args['<person_name>']
        role = args['<FELLOW|STAFF>'].upper()
        accommodation = args['<wants_accommodation>']
        result = dojo.add_person(name, role, accommodation)
        for line in result:
            print(line)
