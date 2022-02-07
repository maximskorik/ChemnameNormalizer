# CompoundsNormalizer
CompoundsNormalizer is a python package that unifies the names of chemical compounds via PubChem API.
# Usage
```
from CompoundsNormalizer import CompoundNameNormalizer

compounds = ["Adenosine", "Adenocard", "BG8967"]
normalizer = CompoundsNameNormalizer(compounds)

# type can be "common" for trivial names or "iupac" for IUPAC names
normalizer.normalize(type="common")

# print the results as a table with 1st column being orignal name and 2nd column being normalized name
normalizer.as_pandas()
```
Alternatively you can run the tool in a Docker container:
```
$ docker build -t normalizer .
```
After the image is built you can run the tool with sample inputs as follows:
```
docker run -t normalizer
```
or you can change the input array in the `main.py` file and run the tool in the container with new input as follows:
```
docker run -t -v $(pwd):/usr/src/CompoundsNormalizer normalizer python main.py
