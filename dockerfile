FROM python:3

ADD freemen.py
ADD requirements.txt

RUN pip3 install -r requirements.txt

CMD [ "python", "./freemen.py" ]
