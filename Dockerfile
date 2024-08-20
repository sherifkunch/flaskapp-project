FROM python:3.9-alpine

COPY . /root/ 

WORKDIR /root/

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["web.py"]
