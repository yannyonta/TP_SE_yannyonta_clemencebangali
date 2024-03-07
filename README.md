# Stockage des Tâches

Ce projet permet de stocker et de manipuler des tâches à l'aide de fichiers JSON sur l'ordinateur.

## Installation

1. Clonez ce dépôt sur votre machine locale :
   
   git clone https://github.com/yannyonta/TP_SE_yannyonta_clemencebangali.git
   

2. Naviguez vers le dossier du projet :
   
   cd gestionnaire-de-taches
   

3. Assurez-vous d'avoir Python installé sur votre machine.

## Utilisation

1. Ouvrez le fichier dataTask.py pour accéder aux fonctions de stockage des tâches.

2. Importez le module dataTask dans votre propre code Python :
   python
   import dataTask
   

3. Utilisez les fonctions fournies pour gérer le stockage des tâches :
   - save_to_json(data, filename): Enregistre un dictionnaire de tâches dans un fichier JSON.
   - load_from_json(filename): Charge un fichier JSON contenant des tâches et retourne le dictionnaire correspondant.
   - delete_database(filename): Supprime le fichier de base de données JSON.

## Exemple d'utilisation

python
tasks = {
    1: {'id': 1, 'title': 'Faire les courses', 'completed': False},
    2: {'id': 2, 'title': 'Répondre aux e-mails', 'completed': False}
}

# Enregistrer les tâches dans un fichier JSON
dataTask.save_to_json(tasks, 'tasks.json')

# Charger les tâches depuis le fichier JSON
loaded_tasks = dataTask.load_from_json('tasks.json')

print(loaded_tasks)
