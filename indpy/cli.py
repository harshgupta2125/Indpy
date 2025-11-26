import sys
import os

# If we are running this file directly, add the parent folder to the system path
if __name__ == "__main__" and __package__ is None:
    # Get the path to the folder ABOVE 'indpy'
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, parent_dir)
    __package__ = "indpy"


import argparse
from . import __version__
from . import validators
from . import generators

def main():
    parser = argparse.ArgumentParser(description="indpy - Indian Data Utilities CLI")
    
    parser.add_argument('-v', '--version', action='version', version=f'indpy v{__version__}')
    
    # Subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # 'check' command
    check_parser = subparsers.add_parser('check', help='Validate a document')
    check_parser.add_argument('type', choices=['pan', 'gstin', 'mobile', 'ifsc', 'vehicle'], help='Document type')
    check_parser.add_argument('value', help='Value to validate')

    # 'gen' command
    gen_parser = subparsers.add_parser('gen', help='Generate fake data')
    gen_parser.add_argument('type', choices=['pan', 'mobile', 'vehicle'], help='Data type to generate')

    args = parser.parse_args()

    # Logic for CHECK
    if args.command == 'check':
        func_map = {
            'pan': validators.is_pan,
            'gstin': validators.is_gstin,
            'mobile': validators.is_mobile,
            'ifsc': validators.is_ifsc,
            'vehicle': validators.is_vehicle
        }
        
        is_valid = func_map[args.type](args.value)
        icon = "✅" if is_valid else "❌"
        print(f"{icon} {args.type.upper()} Validation Result: {is_valid}")

    # Logic for GEN
    elif args.command == 'gen':
        if args.type == 'pan':
            print(generators.Generate.pan())
        elif args.type == 'mobile':
            print(generators.Generate.mobile())
        elif args.type == 'vehicle':
            print(generators.Generate.vehicle())
            
    else:
        parser.print_help()

if __name__ == "__main__":
    main()