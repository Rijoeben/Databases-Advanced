sudo docker pull mongo
sudo docker pull redis
sudo docker pull rijoeben/scraper
sudo docker pull rijoeben/filter
sudo docker run --name container2 -p 6379:6379 redis 
sudo docker run --name container4 -p 27017:27017 mongo
sudo docker network create mynetwork
sudo docker network connect mynetwork container2
sudo docker network connect mynetwork container4
sudo docker run --name container1 rijoeben/scraper
sudo docker network connect mynetwork container1
sudo docker start container1
sudo docker run --name container3 rijoeben/filter
sudo docker network connect mynetwork container3
sudo docker start container3

sudo docker start container2
sudo docker start container4
sudo docker start container1
sudo docker start container3
