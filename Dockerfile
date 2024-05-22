
# pull the python3.11 image
FROM python:3.11
 
# set the working directory in the container
WORKDIR /src

# Copy the requirements.yml file into the container
COPY requirements.yml .

# Install necessary tools
RUN pip install pyyaml

# Add a script to convert requirements.yml to requirements.txt
RUN python -c "
import yaml
with open('requirements.yml', 'r') as yml_file:
    data = yaml.safe_load(yml_file)
with open('requirements.txt', 'w') as txt_file:
    for dependency in data['dependencies']:
        if isinstance(dependency, dict) and 'pip' in dependency:
            for package in dependency['pip']:
                txt_file.write(package + '\n')
"

COPY requirements.txt ./requirements.txt

# install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# copy the current directory contents into the container at /usr/src/app
COPY src/ .

# command to run on container start
CMD [ "python", "./app.py"]
