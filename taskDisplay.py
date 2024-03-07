
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

if _name_ == "_main_":
    main()
