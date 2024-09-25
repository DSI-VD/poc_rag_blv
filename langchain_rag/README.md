# RAG avec Llamaindex

## Extraction des requêtes

À partir des fichiers logs, on peut obtenir des exemples de recherche avec la commande suivante:

```bash
grep -o -P '(?<=query\=).*?(?=&)' all.log | python -c "import sys, urllib.parse; print(urllib.parse.unquote(sys.stdin.read()))" > queries.txt
```

`all.log` correspond à la concaténation de 27 jours (2024-06-19 à 2024-07-18) de fichiers logs d'accès à l'application de la BLV.

## Base vectorielle

Il faut compter environ 15s par split de document en moyenne pour générer les _embeddings_