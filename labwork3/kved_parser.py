"""
This module contains program, which makes operations with JSON files.
"""
import json


def reading_json(json_file):
    """
    This function reads json file and convert it to dictionary

    >>> len(reading_json("kved.json"))
    1
    """
    with open(json_file, encoding="utf-8") as file:
        r_json = json.load(file)
    return r_json


def finding_classcode(json_dict, class_code):
    """
    This function finds the place, where the classcode is,
    and creates a dictionary with whole path to this class code.
    """
    kved_result = dict()
    for sections in json_dict:
        for part in json_dict[sections]:
            for division in part:
                for division_code in division["divisions"]:
                    if division_code["divisionCode"] == class_code[:2]:
                        for group in division_code["groups"]:
                            if group["groupCode"] == class_code[:4]:
                                for classes in group["classes"]:
                                    if classes["classCode"] == class_code:
                                        kved_result["name"] = classes["className"]
                                        kved_result["type"] = "class"
                                        kved_result["parent"] = dict()
                                        kved_result["parent"]["name"] = group["groupName"]
                                        kved_result["parent"]["type"] = "group"
                                        kved_result["parent"]["num_children"] = len(
                                            group["classes"])
                                        kved_result["parent"]["parent"] = dict(
                                        )
                                        kved_result["parent"]["parent"]["name"] = \
                                            division_code["divisionName"]
                                        kved_result["parent"]["parent"]["type"] = "division"
                                        kved_result["parent"]["parent"]["num_children"] = len(
                                            division_code["groups"])
                                        kved_result["parent"]["parent"]["parent"] = dict(
                                        )
                                        kved_result["parent"]["parent"]["parent"]["name"] = \
                                            division["sectionName"]
                                        kved_result["parent"]["parent"]["parent"]["type"] = \
                                            "section"
                                        kved_result["parent"]["parent"]["parent"]["num_children"]\
                                            = len(division["divisions"])
                                        return kved_result
    return None


def convert_dict_to_json(dictionary):
    """
    This function converts dictionary to json format.
    Also this function writes down json file into the file with name
    kved_results.json
    """
    with open("kved_results.json", "w", encoding="utf-8") as file:
        json.dump(dictionary, file, indent=2, ensure_ascii=False)


def parse_kved(class_code):
    """
    This is the main function, which connects the work of all functions.
    """
    convert_dict_to_json(finding_classcode(
        reading_json("kved.json"), class_code))


print(parse_kved("01.70"))
