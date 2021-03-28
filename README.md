## Om de scraper uit te voeren moet u volgende stappen doen.

### stap 1 installeer docker met behulp van de volgende commando's
sudo apt update
sudo apt upgrade
sudo apt install docker.io
sudo systemctl enable --now docker

### stap 2 clone de volgende github repository op de machine
git clone https://github.com/Rijoeben/Databases-Advanced.git

### stap 3 Ga in de github directory en voer volgende commando uit
./projectScript.sh

#### Tijdens het uitvoeren van dit script kan het zijn dat de terminal vast loopt druk dan op ctrl + c om de terminal verder te laten gaan.

### stap 4 Check met het volgende commando of alle containers gestart zijn. U zou 4 container moeten zien. Indien de containers niet allemaal gestart zijn kijk naar welke container niet gestart is en doe dan het volgende commando met x de nummer van de niet gestarte container 1, 2, 3 of 4.

sudo docker ps

sudo docker start container(x) 

## stap 5 als u wilt kunnen volgen of alles goed verloopt installer dan ook nog mongodb compass en connect met de localhost database.

www.mongodb.com/try/download/compass

