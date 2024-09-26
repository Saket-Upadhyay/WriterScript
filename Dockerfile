FROM python:3-alpine

WORKDIR /writerscript/source

COPY . .

WORKDIR /writerscript/source/WriterScript

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir setuptools

RUN python setup.py install

WORKDIR /tmp

ENTRYPOINT ["wscript"]

CMD ["--help"]
