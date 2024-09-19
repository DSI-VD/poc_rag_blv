# RAG avec Llamaindex

## Extraction des requêtes

À partir des fichiers logs, on peut obtenir des exemples de recherche avec la commande suivante:

```bash
grep -o -P '(?<=query\=).*?(?=&)' all.log | python -c "import sys, urllib.parse; print(urllib.parse.unquote(sys.stdin.read()))" > requests.txt
```