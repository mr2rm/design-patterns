import sys

from create_order import CreateOrder
from update_order import UpdateOrder
from ship_order import ShipOrder
from no_command import NoCommand


# TODO: violates O in SOLID
def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return {cls.name: cls for cls in commands}


def print_usage(commands):
    print('Usage: python -m after <command> [arguments]')
    print('Commands:')
    for command in commands.values():
        print(f'    {command.description}')


def parse_command(commands, args):
    command = commands.get(args[0], NoCommand)
    return command(args)


commands = get_commands()
if len(sys.argv) < 2:
    print_usage(commands)
    exit()

# Find and execute the command
command = parse_command(commands, sys.argv[1:])
command.execute()
