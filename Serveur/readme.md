#Serveur Lucie
##Echange entre Java et les différents langage
###Java

###Python
Voici le début du code :<br>
<code>socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)</code><br>
Cette ligne permet de créer une socket en mode TCP et non UDP !!!<br><br>
<code>socket.connect(("localhost", "6009"))</code><br>
Cette ligne permet de se connecter au serveur au port 6009<br><br>
<code>socket.send(b"getCoord();")</code><br>
Permet d'envoie un tableau de charactère/String<br><br>
<code>msg = socket.recv(9999999)</code><br>
Permet de recevoir une ligne de charactère/String<br><br>
<code>socket.close()</code><br><br>
Permet de fermer le flux TCP<br>

##Services
{En cours de rédaction...}
##Explication
{En cours...}