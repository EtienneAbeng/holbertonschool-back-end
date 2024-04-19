import requests  # Pour les requêtes HTTP
import sys  # Pour accéder aux arguments de ligne de commande


def get_employee_tasks(employee_id):
    """
    Fonction pour récupérer et afficher les tâches d'un employé.

    Args:
        employee_id (int): L'ID de l'employé dont on veut récupérer les tâches.
    """
    URL = "https://jsonplaceholder.typicode.com"  # URL de l'API
    try:
        response = requests.get(
            "{}/users/{}/todos".format(URL, employee_id),
            params={"_expand": "user"}
        )
        response.raise_for_status()  # Vérifie si la requête a réussi
        data = response.json()  # Extraction des données JSON

        EMPLOYEE_NAME = data[0]["user"]["name"]  # Nom de l'employé
        TOTAL_NUMBER_OF_TASKS = len(data)  # Nombre total de tâches
        NUMBER_OF_DONE_TASKS = 0  # Nombre de tâches terminées
        TASK_TITLE = []  # Titres des tâches terminées

        for task in data:  # Parcours des tâches
            if task["completed"]:
                NUMBER_OF_DONE_TASKS += 1  # Incrémente compteur
                # Ajout du titre de la tâche
                TASK_TITLE.append(task["title"])

        print(f"Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for title in TASK_TITLE:  # Affichage titres tâches terminées
            print("\t", title)

    except requests.exceptions.RequestException as e:  # Gestion des erreurs
        print("An error occurred:", e)  # Affichage de l'erreur
        sys.exit(1)  # Arrêt du programme avec un code d'erreur


if __name__ == "__main__":
    if len(sys.argv) != 2:  # Vérification du nombre d'arguments
        # Message d'erreur si l'ID de l'employé est manquant
        print("Missing employee ID as argument")
        sys.exit(1)  # Arrêt du programme avec un code d'erreur

    employee_id = sys.argv[1]  # Récupération de l'ID de l'employé
    # Appel de la fonction pour récupérer les tâches de l'employé
    get_employee_tasks(employee_id)
