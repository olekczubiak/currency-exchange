FROM python:3

ENV PYTHONUNBUFFERED 1

# Backend Service
WORKDIR /app/backend
ADD /BackendServer/. /app/backend/
COPY /BackendServer/requirements.txt /app/backend/requirements.txt
RUN pip install -r requirements.txt
COPY /BackendServer/. /app/backend/


# Scrapping Service 
# WORKDIR /app/scrapping
# ADD /WebScappingServer/. /app/scrapping/
# COPY /WebScappingServer/requirements.txt /app/scrapping/requirements.txt
# RUN pip install -r requirements.txt
# COPY /WebScappingServer/. /app/scrapping/