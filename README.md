# Gestionnaire de Tâches

Ce projet est un gestionnaire de tâches simple implémenté en Python. Il permet d'ajouter, supprimer et marquer des tâches comme terminées.

## Installation

1. Clonez ce dépôt sur votre machine locale :
   
   git clone https://github.com/yannyonta/TP_SE_yannyonta_clemencebangali.git
   

2. Naviguez vers le dossier du projet :
   
   cd gestionnaire-de-taches
   

3. Assurez-vous d'avoir Python installé sur votre machine.

## Utilisation

1. Ouvrez le fichier taskTool.py pour accéder aux fonctionnalités du gestionnaire de tâches.

2. Importez le module taskTool dans votre propre code Python :
   python
   import taskTool
   

3. Utilisez les fonctions fournies pour gérer les tâches :
   - add_task(task_dict, new_task): Ajoute une nouvelle tâche au dictionnaire des tâches.
   - remove_task(task_dict, task_id): Supprime une tâche du dictionnaire des tâches.
   - complete_task(task_dict, task_id): Marque une tâche comme terminée dans le dictionnaire des tâches.

## Exemple d'utilisation

python
tasks = {
    1: {'id': 1, 'title': 'Faire les courses', 'completed': False},
    2: {'id': 2, 'title': 'Répondre aux e-mails', 'completed': False}
}

# Ajouter une nouvelle tâche
new_task = {'id': 3, 'title': 'Appeler le client', 'completed': False}
tasks = taskTool.add_task(tasks, new_task)

# Supprimer une tâche
tasks = taskTool.remove_task(tasks, 2)

# Marquer une tâche comme terminée
tasks = taskTool.complete_task(tasks, 1)

print(tasks)
