import requests  # Requêtes HTTP
import csv  # Manipulation de fichiers CSV
import sys  # Arguments de ligne de commande

def export_to_csv(employee_id, tasks):
    employee_name = tasks[0]["user"]["name"]  # Nom de l'employé
    filename = "{}.csv".format(employee_id)  # Nom du fichier CSV

    with open(filename, mode="w", newline="", encoding="utf-8") as file:  # Ouverture du fichier CSV en mode écriture
        writer = csv.writer(file)  # Création d'un objet writer pour écrire dans le fichier CSV
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Écriture de l'en-tête CSV
        for task in tasks:  # Boucle à travers les tâches
            row = [employee_id, employee_name, str(task["completed"]), task["title"]]  # Création de la ligne à écrire
            writer.writerow(row)  # Écriture de la ligne dans le fichier CSV

    print("Data exported to {}".format(filename))  # Message de confirmation

def get_employee_tasks(employee_id):
    URL = "https://jsonplaceholder.typicode.com"  # URL de l'API
    try:
        response = requests.get("{}/users/{}/todos".format(URL, employee_id), params={"_expand": "user"})  # Requête GET pour récupérer les tâches de l'employé
        response.raise_for_status()  # Vérification du statut de la réponse
        tasks = response.json()  # Conversion de la réponse en JSON

        # Export des données vers un fichier CSV
        export_to_csv(employee_id, tasks)
    except requests.exceptions.RequestException as e:  # Gestion des exceptions
        print("An error occurred:", e)  # Affichage de l'erreur
        sys.exit(1)  # Arrêt du programme en cas d'erreur

if __name__ == "__main__":
    if len(sys.argv) != 2:  # Vérification du nombre d'arguments
        print("Missing employee ID as argument")  # Message d'erreur si l'ID de l'employé est manquant
        sys.exit(1)  # Arrêt du programme avec un code d'erreur

    employee_id = sys.argv[1]  # Récupération de l'ID de l'employé depuis les arguments de ligne de commande
    get_employee_tasks(employee_id)  # Appel de la fonction pour récupérer les tâches de l'employé
