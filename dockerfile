FROM python:latest

COPY . /usr/src/CompoundsNormalizer
WORKDIR /usr/src/CompoundsNormalizer

RUN pip install -r requirements.txt
RUN python setup.py install

ENTRYPOINT ["python", "main.py"]