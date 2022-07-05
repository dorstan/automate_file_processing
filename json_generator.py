#!/usr/bin/env python3
import json
import csv
import sys, os

def dict_from_csv(csv_path, rowname):
    """This function converts a CSV file with <;> or <,> delimiters into JSON file."""
    dict_csvdata = {}
    with open(csv_path, mode="r", encoding="utf-8") as csv_file:
        # Identify the delimiter from csv file
        csv_delimiter = csv.Sniffer().sniff(csv_file.read(), delimiters=";,")
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file, dialect=csv_delimiter)
        # Use the unique rowname for keys
        for row in csv_reader:
            key = row[rowname]
            dict_csvdata[key] = row
    return dict_csvdata


def deserialize_from_jsonfile(filename):
    """Loads the data from a jsnon file into a dictionary."""
    with open(filename) as jsnfile:
        dict_data = json.load(jsnfile)
    return dict_data


def serialize_to_jsonfile(raw_data, filename):
    """This function takes data from python object and creates a json file"""
    with open (filename, "w", encoding="utf-8") as jsfl:
        json.dump(raw_data, jsfl, indent=3)


def json_to_csv(json_file):
    """This function creates a CSV file from Json file"""
    # Call deserialize_from_jsonfile to create a dictionary
    dict_data = deserialize_from_jsonfile(json_file)
    # Open a file with the same name and csv extension 
    with open("{}.csv".format(json_file.replace(".json", "")), "w") as cf:
        csv_writer = csv.DictWriter(cf, dict_data.keys())
        csv_writer.writeheader()
        csv_writer.writerow(dict_data)


if __name__ == "__main__":
    # Call argv for imput (filename[1] and uique_row[2] to be used as key)
    json_generator = sys.argv
    command_generator = json_generator[1]
    if command_generator == "json":
        file_name = input("Please type the file path ")
        if not os.path.isfile(file_name):
            print("Please provide a valid path")
            file_name =input("Please type the file path ")
        row_unique_key = input("Please type the uique row as key ")
        
        alpha = dict_from_csv(file_name, rowname=row_unique_key)
        # Save the file with the same name and json extension
        serialize_to_jsonfile(alpha, "{}.json".format(file_name.replace(".csv", "")))
    elif command_generator == "csv":
        file_name = input("Please type the file path ")
        if not os.path.isfile(file_name):
            print("Please provide a valid path")
            file_name =input("Please type the file path ")
        json_to_csv(file_name)
