import csv
import pytest
import os
from ChemicalNameNormalizer.utils import read_input, write_output

here = os.path.abspath(os.path.dirname(__file__))
testdata_dir = os.path.join(here, 'data')


@pytest.fixture(params=['compounds.txt'])
def filename_input(request):
    return os.path.join(testdata_dir, request.param)


def test_read_input(filename_input):
    input_data = read_input(filename_input)

    assert type(input_data) == list
    assert len(input_data) == 50


def test_write_output(tmp_path):
    original_data = ['test', 'test2', 'test3']
    normalized_data = ['test_norm', 'test2_norm', 'test3_norm']

    out_path = os.path.join(tmp_path, 'output.csv')
    write_output(out_path, original_data, normalized_data)

    with open(out_path) as f:
        reader = csv.reader(f)
        data = list(reader)

    actual_original = [i[0] for i in data]
    actual_normalized = [i[1] for i in data]

    assert original_data == actual_original
    assert normalized_data == actual_normalized
