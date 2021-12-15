FROM python:2.7
MAINTAINER Brindavani Pathuri "bp16479n@pace.edu" and Krishna  "vt72814n@pace.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
