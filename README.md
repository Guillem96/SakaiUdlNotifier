# SakaiUdlNotifier
Sistema de notificacions d'anuncis del campus virtual de la UdL.
Mitjançant web scraping obté els missatges més recents del campus virtual de la Udl i mostra una notificació.

## Instal·lació

```
$ pip install -r requirements.txt
$ chmod +x notifier.sh
$ chmod +x notifier.py
```

## Configuració

Modificar el fitxer config.json

```
{
    "path" : "<path_de_la_carpeta_que_conte_script>",
    "username": "<usuari_campus_virtual>",
    "password": "<contrassenya_campus>"
}
```

## Execució
```
./notifier.sh
```

## Exemple execució programada al crontab
En procés...

## Autor 
Guillem Orellana Trullols