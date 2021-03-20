FROM python:3.7-alpine

WORKDIR /writerscript/source

COPY . .

WORKDIR /writerscript

RUN pip install --no-cache-dir writerscript

CMD ["/bin/sh"]