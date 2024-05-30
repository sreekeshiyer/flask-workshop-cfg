FROM python:3.9.7-slim-buster

#Set the working directory to /todo-app
WORKDIR /todo-app
#Copy the Code from the source to the images' code  directory
COPY . .

#Install dependencies
RUN pip install -r requirements.txt

#env variables 
## make sure your credentials.json file is available on the directory when you're building this
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

#Expose the port
EXPOSE 5000

#Start the dev server
CMD ["flask", "run"]
