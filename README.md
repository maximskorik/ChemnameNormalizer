# ChemnameNormalizer
**ChemnameNormalizer** is a python package that unifies the names of chemical compounds via PubChem REST API.
It maps different synonyms of a same compound to the same name – trivial or iupac.
It also accepts chemical names with typos and performs fuzzy searching to match those names.
## Installation
Install the required dependencies and the package:
```shell
$ pip install -r requirements.txt
$ python setup.py install
```
## Usage
Use **ChemnameNormalizer** in python:
```python
from ChemnameNormalizer import Normalizer


compounds = ["aden0card", "Adenocard", "BAYT006267", "diflucan", "ibrut1nlb", "PC-32765"]

normalizer = Normalizer(normalization_format="trivial")
norm_compounds = normalized(names=compounds)

>> norm_compounds
["adenosine", "adenosine", "fluconazole", "fluconazole", "ibrutinib", "ibrutinib"]
```
You can run the package in the command line (executed with sample data):
```shell
$ python ChemnameNormalizer \
    --input tests/data/compounds.txt \
    --output output.csv \
    --normalization_format trivial
```
Alternatively, you can use **ChemnameNormalizer** in a Docker container:
```shell
# Build the Docker image
$ docker build -t normalizer .
...
$ docker run -it --rm -v $(pwd):/usr/src/ChemnameNormalizer normalizer \
    -i tests/data/compounds.txt \
    -o output.csv \
    -f trivial
````



