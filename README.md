### installation
- copy file called cot-env from fenv folder, paste and renamed to .cot-env to
  root folder
- copy file called cot-envdb from fenv folder, paste and renamed to .cot-envdb
  to root folder
 
### build docker
```commandline
  docker-compose build
```

### up docker
```commandline
  docker-compose up -d 
```

### migration db
```commandline
  docker-compose exec api python manage.py makemigrations
  docker-compose exec api python manage.py migrate --noinput 
```

### inside the docker images data base 
```commandline
 - docker-compose exec db psql --username=myuser --dbname=mydatabase 
```

### api to recover data market yfinance
```commandline
 http://127.0.0.1:9001/api/recovery?symbol=META&start_date=1990-01-01&end_date=2023-07-20 
```

### api to read data saved for the code above
```commandline


```

### list volumes docker 
### display a list of volumes
```
 - docker volume ls 
```

### inspect a volume 
```
 - docker volume inspect my-volume-listed 
```

### build a docker using tag 
```
 - docker build -f ./app/Dockerfile -t mytagfordocker:latest ./app
```

### run another images in other port 
### docker is running on port localhost:9002
```
docker run -d \                                     
-p 9002:9001 \
-e "SECRET_KEY=mysecretkey" -e "DEBUG=1" -e "ALLOWED_HOSTS=*" \
api python /usr/src/app/manage.py runserver 0.0.0.0:9001
```

### show docker lgos
```
- docker-compose -f docker-compose.prod.yml logs -f
```
