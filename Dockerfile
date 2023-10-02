FROM python:latest
LABEL maintainer="jrauljperez02.dev@gmail.com"

WORKDIR /usr/app/src

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY Data.csv ./

COPY app.py ./

CMD [ "python", "./app.py" ]