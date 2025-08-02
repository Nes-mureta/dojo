

'''
DOJO Application CLI Interface

usage:
create_room <room_type> <room_name>
add_person <person_name> <role> [<wants_living_space>]
'''

from docopt import docopt
from dojo import Dojo

if __name__ == '__main__':
  args= docopt(__doc__)
  dojo = Dojo()
  
  if args['create_room']:
    for name in args['<room_name>']:
      print(dojo.create_room(args['<room_type>'], name))
      
  elif args['add_person']:
    name=args['<person_name>']
    role=args['<role>']
    wants_living_space=args['<wants_living_space>']or 'No'
    for line in dojo.add_person(name, role, wants_living_space):
      print(line)
      
  else:
    print("Invalid input. Use 'create_room' or 'add_person'.")