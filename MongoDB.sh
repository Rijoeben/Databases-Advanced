if [ ! -f /usr/bin/mongod ]; then<br>
  sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10<br>
  echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list<br>
  sudo apt-get -y update
  sudo apt-get install -y mongodb-org<br>
else
  echo "mongo db already installed.  Skipping..."
fi