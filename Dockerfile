FROM python:latest
RUN mkdir /usr/src/rush/
WORKDIR /usr/src/rush/
RUN apt-get update -
RUN apt-get install apt-utils -y
RUN apt update -y
RUN apt install -y tor
RUN service tor start
COPY . .
RUN pip3 install --user -r requirements.txt
RUN export PATH="/root/.local/bin"
ENTRYPOINT ["python3"]
CMD ["index.py"]