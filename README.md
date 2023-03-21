# gaatha-server

# Steps to run the project:

- Clone the repository to your local machine

- Create a **.env** file with the necessary environment variables. Check `?err` attributes in **docker-compose.yml** and **gaatha/settings.py**

- Run Project
`docker-compose up`

- To create super user:
`docker-compose exec server ./manage.py createsuperuser`

- To go to admin page go to http://localhost:8020/admin/

- To generate schema file enter following command:
`docker-compose exec server ./manage.py generate_schema --out schema.graphql`
