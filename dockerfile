FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

# Add required packages
RUN apk update && apk add curl

# Add our code to DockerContainer Folder
ADD . /app/webapp/

# Set Working Directory
WORKDIR /app/webapp/

#upgrade PIP
RUN pip3 install --upgrade pip

# install FastAPI requirement
RUN pip3 install fastapi "uvicorn[standard]"


EXPOSE 80
CMD ["uvicorn","main:app","--host","0.0.0.0", "--port","80"]