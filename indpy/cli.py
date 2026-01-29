"""Command-line interface for indpy - Indian Data Utilities."""

import argparse
import os
import sys

from . import __version__
from . import generators
from . import validators

if __name__ == "__main__" and __package__ is None:
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, parent_dir)
    __package__ = "indpy"


def main():
    """Main CLI entry point for indpy validation and generation commands."""
    parser = argparse.ArgumentParser(description="indpy - Indian Data Utilities CLI")

    parser.add_argument(
        "-v", "--version", action="version", version=f"indpy v{__version__}"
    )

    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'check' command
    check_parser = subparsers.add_parser("check", help="Validate a document")
    check_parser.add_argument(
        "type",
        choices=[
            "pan",
            "gstin",
            "mobile",
            "ifsc",
            "vehicle",
            "aadhaar",
            "voterid",
            "passport",
            "cin",
            "pincode",
        ],
        help="Document type",
    )
    check_parser.add_argument("value", help="Value to validate")

    # 'gen' command
    gen_parser = subparsers.add_parser("gen", help="Generate fake data")
    gen_parser.add_argument(
        "type",
        choices=[
            "pan",
            "mobile",
            "vehicle",
            "aadhaar",
            "voterid",
            "passport",
            "cin",
            "pincode",
        ],
        help="Data type to generate",
    )
    args = parser.parse_args()

    # Logic for CHECK
    if args.command == "check":
        func_map = {
            "pan": validators.is_pan,
            "gstin": validators.is_gstin,
            "mobile": validators.is_mobile,
            "ifsc": validators.is_ifsc,
            "vehicle": validators.is_vehicle,
            "aadhaar": validators.is_aadhaar,
            "voterid": validators.is_voterid,
            "passport": validators.is_passport,
            "cin": validators.is_cin,
            "pincode": validators.is_pincode,
        }

        is_valid = func_map[args.type](args.value)
        icon = "✅" if is_valid else "❌"
        print(f"{icon} {args.type.upper()} Validation Result: {is_valid}")

    # Logic for GEN
    elif args.command == "gen":
        gen_map = {
            "pan": generators.Generate.pan,
            "mobile": generators.Generate.mobile,
            "vehicle": generators.Generate.vehicle,
            "aadhaar": generators.Generate.aadhaar,
            "voterid": generators.Generate.voterid,
            "passport": generators.Generate.passport,
            "cin": generators.Generate.cin,
            "pincode": generators.Generate.pincode,
        }
        print(gen_map[args.type]())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
