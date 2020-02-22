FROM python:latest

ADD freemen.py /root/
ADD requirements.txt /root/
ADD .env /root/

RUN pip3 install -r /root/requirements.txt

CMD [ "python", "./freemen.py" ]
