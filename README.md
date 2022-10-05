# data_lookup_api_1


#for first time only run: 
    docker network create db

#run this commands to start:
#1 you need start postgress container by:
    docker-compose up
#2 build the app and start it
    
    docker build -t lookup_data_api .
    
    docker run -d -p 5001:5001 --name lookup_data_api --restart=always lookup_data_api:latest

