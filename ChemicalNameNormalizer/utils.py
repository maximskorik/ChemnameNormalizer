import csv
from typing import List, Union
import os


def write_output(file_path, original_data, normalized_data):
    with open(file_path, 'a') as f:
        for pair in zip(original_data, normalized_data):
            f.write(pair[0] + "," + pair[1] + "\n")


def read_input(file_path) -> Union[List, NotImplementedError]:
    _, file_extension = os.path.splitext(file_path)
    if file_extension == ".txt":
        return read_txt(file_path)
    elif file_extension == ".csv":
        return read_csv(file_path)
    else:
        raise NotImplementedError("File extension not supported. Supported extensions: txt, csv")


def read_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def read_txt(file_path):
    with open(file_path) as f:
        data = f.readlines()
        data = [data.rstrip('\n') for data in data]
    return data
