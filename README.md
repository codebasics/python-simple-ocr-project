# python-simple-ocr-project
A simple OCR Project using python with frontend in VueJS



# Overview
Repository for Medical-OCR.

# Folder Structure
1. **api** : backend for performing ocr
    
    1.1. **extaractor** : performing format specific field extractions on text 

    1.2. **image_utils** : extracting text from  every images of pdf

    1.3. **parser** : parsing pdf pages into images for image processing use

    1.4. **uploads** : just temperory folder for storing pdf files for temperory 

2. **frontend**: frontend for request response

    -having only one component for uploading pdf file and getting response from docker and printing it on the screen.

# Setup Instructions For Local Environment

1. Install git bash or any other git client where you can run git & unix commands.

2. Install Docker CE. ([Setup instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/))

3. Install docker-compose. ([Setup instructions](https://docs.docker.com/compose/install/))

4. Clone the project. (`https://github.com/beladiyadarshan/python-simple-ocr-project.git`)

5. Copy docker-compose.yml.example and save it as docker-compose.yml.

6. For Running Backend api
```
    cd api(change your directory to api)
    docker-compose up --build
```
7.For Running frontend
```
    cd ../frontend(change your directory to frontend)
    npm install (install all required node packages)
    npm run dev (for running the frontend)
```
    