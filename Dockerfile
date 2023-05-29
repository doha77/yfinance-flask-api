FROM python:3.9-slim-buster

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
curl

# copy every content from the local file to the image
COPY . .

ENV FLASK_APP=src/main/app.py

# configure the container to run in an executed manner
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]