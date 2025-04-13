# Planetobot 🤖🌍

Un petit bot Discord développé en Python avec `discord.py`.

## Fonctionnalités
- Commande `!ping` pour tester la réactivité du bot
- Configuration simple avec un fichier `.env`

## Lancement

1. Installe les dépendances :
```bash
pip install -r requirements.txt
```

2. Crée un fichier `.env` avec ton token Discord :
```
DISCORD_TOKEN=ton_token_ici
```

3. Lance le bot :
```bash
python main.py
```

## Déploiement sur Render
- Ajoute `DISCORD_TOKEN` comme variable d’environnement.
- Utilise `python main.py` comme Start Command.
