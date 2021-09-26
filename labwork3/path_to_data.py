"""
This module contains program, which helps you to check json information file.
"""
import json
import webbrowser
import sys


def reading_json(json_file):
    """
    This function reads json file and convert it to dictionary

    >>> len(reading_json("frienfs_list_Obama.json"))
    6
    """
    with open(json_file, encoding="utf-8") as file:
        r_json = json.load(file)
    return r_json


def path_to_data(read_file, result=""):
    """
    This function is capable for making a path to the information,
    user wants to check.
    It works on the base of recursion.
    """
    if isinstance(read_file, dict):
        print("Your item is a dictionary!")
        print("Would you like to see list of keys?\n")
        print("""Enter "yes" or "no" \n""")
        if input() == "yes":
            print("\n", read_file.keys(), "\n")
        print("Please, enter a key\n")
        key = input()
        print()
    else:
        print("Your item is a list!")
        print("Please, enter an index\n")
        key = int(input())
        print()
    try:
        if isinstance(read_file[key], (dict, list)):
            result = path_to_data(read_file[key])
        else:
            result = read_file[key]
            try:
                if result.startswith("http"):
                    webbrowser.open(result, new=2, autoraise=True)
            except AttributeError:
                result = read_file[key]
    except (KeyError, IndexError):
        print("Unknown key or index!")
        sys.exit()
    return result


def acsess_to_data(json_file):
    """
    This is the main function, it connects to functions below
    and returns a result
    """
    return path_to_data(reading_json(json_file))
