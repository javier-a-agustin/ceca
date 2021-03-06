# Project structure  
- **django/ folder:** contain the django code. This includes the API view (drf), management command and fixture to load initial data.  
- **frontend/ folder:** contains the frontend react files.  
- **env_variables/ folder:** enviroment variables that the containers will use (and apps).
- **dockerfiles/ folder:** contains the Dockerfiles for the Django and React containers. This files are used when the container is created.  
- **mysql/ folder:** volume for the mysql database. It's not added to git.

# Start project  
In the main directory run:  
- `docker-compose up -d --build`  
Once the containers are created run:   
- `docker exec ceca_django_1 python manage.py migrate`  
then  
- `docker exec ceca_django_1 python manage.py write_car_rows`  

### Explanation
The migrate command will apply the migrations to the database.  
The write_car_rows command is a custom management command that will call the loaddata command with the car_fixture.json fixture. This command will load the initial rows for the Car model.  
See the django\api\management\commands\write_car_rows.py file.  

# up.sh command  
By using the ./up.sh shell command within the root directory the containers will start, and migrations and initial data will be added.  
This command won't work until the mysql database is created.  

# List of car plates from car_fixture.json  
- 123abc  
- 123def  
- 123ghi  
- 456abc  
- 456def