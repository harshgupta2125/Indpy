import argparse
import sys
from . import __version__
from . import validators

def main():
    # 1. Setup the parser
    parser = argparse.ArgumentParser(
        description="indpy: The Professional Indian Data Validator Tool 🇮🇳"
    )

    # 2. Add the --version argument
    parser.add_argument(
        '-v', '--version', 
        action='version', 
        version=f'indpy {__version__}'
    )

    # 3. Add arguments to actually DO things (optional but useful)
    # Example usage: indpy pan ABCDE1234F
    parser.add_argument('type', nargs='?', help="Type of validation (pan, gstin, mobile)")
    parser.add_argument('value', nargs='?', help="The value to validate")

    # 4. Read the arguments
    args = parser.parse_args()

    # If user typed nothing, show help
    if not args.type:
        parser.print_help()
        sys.exit(0)

    # Logic for actual validation
    result = False
    doc_type = args.type.lower()
    val = args.value

    if not val:
        print("❌ Error: You must provide a value to check.")
        sys.exit(1)

    if doc_type == 'pan':
        result = validators.is_pan(val)
    elif doc_type == 'gstin':
        result = validators.is_gstin(val)
    elif doc_type == 'mobile':
        result = validators.is_mobile(val)
    else:
        print(f"❌ Unknown type: '{doc_type}'. Try 'pan', 'gstin', or 'mobile'.")
        sys.exit(1)

    # Final Output
    if result:
        print(f"✅ Valid {doc_type.upper()}")
    else:
        print(f"❌ Invalid {doc_type.upper()}")
        sys.exit(1)