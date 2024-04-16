import requests  # Pour les requêtes HTTP
import sys  # Pour accéder aux arguments de ligne de commande


def get_employee_tasks(employee_id):
    URL = "https://jsonplaceholder.typicode.com"  # URL de l'API
    try:
        response = requests.get("{}/users/{}/todos".format(URL, employee_id), params={
                                "_expand": "user"})  # Récupération des tâches de l'employé
        response.raise_for_status()  # Vérifie si la requête a réussi
        data = response.json()  # Extraction des données JSON

        employee_name = data[0]["user"]["name"]  # Nom de l'employé
        total_tasks = len(data)  # Nombre total de tâches
        num_completed_tasks = 0  # Nombre de tâches terminées
        completed_tasks = []  # Titres des tâches terminées

        for task in data:  # Parcours des tâches
            if task["completed"]:  # Si la tâche est terminée
                num_completed_tasks += 1  # Incrémentation du compteur de tâches terminées
                # Ajout du titre de la tâche
                completed_tasks.append(task["title"])

        print("Employee {} is done with tasks ({}/{})".format(employee_name,
              num_completed_tasks, total_tasks))  # Affichage du résultat
        for title in completed_tasks:  # Affichage des titres des tâches terminées
            print("\t ", title)
    except requests.exceptions.RequestException as e:  # Gestion des erreurs
        print("An error occurred:", e)  # Affichage de l'erreur
        sys.exit(1)  # Arrêt du programme avec un code d'erreur


if __name__ == "__main__":
    if len(sys.argv) != 2:  # Vérification du nombre d'arguments
        # Message d'erreur si l'ID de l'employé est manquant
        print("Missing employee ID as argument")
        sys.exit(1)  # Arrêt du programme avec un code d'erreur

    employee_id = sys.argv[1]  # Récupération de l'ID de l'employé
    # Appel de la fonction pour récupérer les tâches
    get_employee_tasks(employee_id)
