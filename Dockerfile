
# pull the python3.11 image
FROM python:3.11
 
# set the working directory in the container
WORKDIR /src

COPY requirements.txt ./requirements.txt

# install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# copy the current directory contents into the container at /usr/src/app
COPY src/ .

# command to run on container start
CMD [ "python", "./app.py"]
