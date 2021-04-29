screen -d -m -S $1 
screen -rd $1 -X -p0 eval "stuff 'java -Xmx1024M -Xms1024M -jar server.jar nogui'^m"
