#!/usr/bin/env python3
import json
import csv
import sys

def serialize_to_jsonfile(raw_data, filename):
    """This function takes data from python object and creates a json file"""
    with open (filename, "w", encoding="utf-8") as jsfl:
        json.dump(raw_data, jsfl, indent=3)

def deserialize_from_jsonfile(filename):
    """Loads the data from a jsnon file into a dictionary."""
    with open(filename) as jsnfile:
        dict_data = json.load(jsnfile)
    return dict_data

def dict_from_csv(csv_path, rowname):
    """This function converts a CSV file with <;> or <,> delimiters into JSON file."""
    dict_csvdata = {}
    with open(csv_path, mode="r", encoding="utf-8") as csv_file:
        # Identify the delimiter from csv file
        csv_delimiter = csv.Sniffer().sniff(csv_file.read(), delimiters=";,")
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file, dialect=csv_delimiter)
        for row in csv_reader:
            key = row[rowname]
            dict_csvdata[key] = row
    return dict_csvdata


if __name__ == "__main__":
    json_generator = sys.argv
    csv_file = json_generator[1]
    row_unique_key = json_generator[2]
    alpha = dict_from_csv(csv_file, rowname=row_unique_key)
    serialize_to_jsonfile(alpha, "{}.json".format(csv_file.replace(".csv", "")))

