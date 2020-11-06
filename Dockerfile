FROM python:3.8

ADD . .

RUN pip install --upgrade pip

RUN pip install numpy scipy

CMD ["python", "-m", "unittest", "discover", "-s","/Tests"]