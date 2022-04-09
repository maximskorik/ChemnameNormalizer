FROM python:3.9.0

COPY . /usr/src/ChemicalNameNormalizer
WORKDIR /usr/src/ChemicalNameNormalizer

RUN pip install -r requirements.txt
RUN python setup.py install

ENTRYPOINT ["python", "ChemicalNameNormalizer"]