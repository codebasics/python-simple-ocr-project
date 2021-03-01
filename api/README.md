# Setting up the API

### With Docker
1. Install Docker CE. ([Setup instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/))

2. Install docker-compose. ([Setup instructions](https://docs.docker.com/compose/install/))

3. Clone the project. (`https://github.com/beladiyadarshan/python-simple-ocr-project.git`)

4. Copy docker-compose.yml.example and save it as docker-compose.yml.

5. Build docker image
```
    docker build .
```

### Without Docker
1. Install Python ([Setup instructions](https://wiki.python.org/moin/BeginnersGuide))

2. Install tesseract ([Setup instructions](https://github.com/tesseract-ocr/tesseract#installing-tesseract))

3. Install Python packages
```
pip3 install -r requirements.txt
```

# Running the API

### With Docker
```
docker-compose up
```

### Without Docker
```
python3 app.py
```
