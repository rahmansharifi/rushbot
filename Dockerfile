FROM python:latest
RUN mkdir /usr/src/rush/
WORKDIR /usr/src/rush/
COPY . .
RUN pip3 install --user -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["index.py"]