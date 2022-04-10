FROM python:3.9.0

COPY . /usr/src/ChemnameNormalizer
WORKDIR /usr/src/ChemnameNormalizer

RUN pip install -r requirements.txt
RUN python setup.py install

ENTRYPOINT ["python", "ChemnameNormalizer"]