# Gestionnaire de Tâches - Mise en Service

Ce projet consiste à créer un gestionnaire de tâches qui permet d'ajouter, de supprimer, de marquer comme terminée et d'afficher des tâches à l'aide d'un fichier JSON pour le stockage des données.

## Installation

1. Clonez ce dépôt sur votre machine locale :
   
   git clone https://github.com/yannyonta/TP_SE_yannyonta_clemencebangali.git
   

2. Naviguez vers le dossier du projet :
   
   cd gestionnaire-de-taches
   

3. Assurez-vous d'avoir Python installé sur votre machine.

## Utilisation

1. Exécutez le script taskDisplay.py pour accéder au programme de gestion des tâches :
   
   python taskDisplay.py
   

2. Suivez les instructions à l'écran pour ajouter, supprimer, marquer comme terminée ou afficher les tâches.

## Fonctionnalités

- *Afficher les Tâches* : Affiche toutes les tâches actuellement enregistrées.
- *Ajouter une Tâche* : Permet à l'utilisateur d'ajouter une nouvelle tâche en spécifiant son ID et son titre.
- *Supprimer une Tâche* : Permet à l'utilisateur de supprimer une tâche en spécifiant son ID.
- *Marquer une Tâche comme Terminée* : Permet à l'utilisateur de marquer une tâche existante comme terminée en spécifiant son ID.

## Étapes à Suivre

1. Assurez-vous d'être sur la branche main avec git checkout main.

2. Créez un nouveau script appelé taskDisplay.py et implémentez les fonctionnalités demandées.

python
import dataTask

def display_tasks(tasks):
    for task_id, task_info in tasks.items():
        print(f"Task ID: {task_id}, Title: {task_info['title']}, Completed: {task_info['completed']}")

def main():
    tasks = {}
    while True:
        print("Que souhaitez-vous faire ?")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Marquer une tâche comme terminée")
        print("5. Quitter")

        choice = input("Entrez le numéro de votre choix : ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task_id = int(input("Entrez l'ID de la tâche : "))
            task_title = input("Entrez le titre de la tâche : ")
            task_completed = False
            tasks[task_id] = {'id': task_id, 'title': task_title, 'completed': task_completed}
            dataTask.save_to_json(tasks, 'tasks.json')
        elif choice == '3':
            task_id = int(input("Entrez l'ID de la tâche à supprimer : "))
            if task_id in tasks:
                del tasks[task_id]
                dataTask.save_to_json(tasks, 'tasks.json')
            else:
                print("La tâche spécifiée n'existe pas.")
        elif choice == '4':
            task_id = int(input("Entrez l'ID de la tâche à marquer comme terminée : "))
            if task_id in tasks:
                tasks[task_id]['completed'] = True
                dataTask.save_to_json(tasks, 'tasks.json')
            else:
                print("La tâche spécifiée n'existe pas.")
        elif choice == '5':
            break
        else:
            print("Choix invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()


3. Faites un commit sur la branche main :


git add taskDisplay.py
git commit -m "Added taskDisplay.py script"


4. Implémentez la fonctionnalité de chargement de la liste de tâches en utilisant la fonction de la partie 3 :

python
def load_tasks():
    tasks = dataTask.load_from_json('tasks.json')
    return tasks


5. Faites un commit sur la branche main :


git add taskDisplay.py
git commit -m "Added load_tasks function"


6. Permettez à l'utilisateur d'ajouter, de supprimer et de marquer une tâche comme terminée en utilisant les fonctions de la partie 2. Assurez-vous que les modifications sont incluses dans taskDisplay.py.

7. Rédigez un README.md pour expliquer comment utiliser votre programme, puis faites un commit et mettez à jour le remote :


git add README.md
git commit -m "Added README.md"
git push origin main
