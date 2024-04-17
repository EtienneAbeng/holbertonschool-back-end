#!/usr/bin/python3

import requests  # Module pour les requêtes HTTP
import json  # Module pour la manipulation de JSON
import sys  # Module pour accéder aux arguments de ligne de commande

def export_to_json(employee_id, tasks):
    """
    Exporte les tâches de l'employé au format JSON dans un fichier.

    Args:
        employee_id (str): L'ID de l'employé.
        tasks (list): La liste des tâches de l'employé.

    Returns:
        None
    """
    # Récupération du nom de l'employé à partir de la première tâche
    employee_name = tasks[0]["user"]["username"]  
    # Construction du nom de fichier JSON basé sur l'ID de l'employé
    filename = "{}.json".format(employee_id)  

    # Création d'un dictionnaire contenant les tâches de l'employé dans le format spécifié
    employee_data = {
        employee_id: [{"task": task["title"], "completed": task["completed"], "username": employee_name} for task in tasks]
    }

    # Écriture des données dans un fichier JSON
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(employee_data, file)  # Écriture des données JSON dans le fichier

    print("Data exported to {}".format(filename))  # Message de confirmation

def get_employee_tasks(employee_id):
    """
    Récupère les tâches de l'employé à partir de l'API et les exporte au format JSON.

    Args:
        employee_id (str): L'ID de l'employé.

    Returns:
        None
    """
    URL = "https://jsonplaceholder.typicode.com"  # URL de l'API JSONPlaceholder
    try:
        # Requête GET pour récupérer les tâches de l'employé avec son ID
        response = requests.get("{}/todos".format(URL), params={"userId": employee_id})  
        response.raise_for_status()  # Vérification du statut de la réponse
        tasks = response.json()  # Conversion de la réponse en JSON

        # Export des données vers un fichier JSON
        export_to_json(employee_id, tasks)  
    except requests.exceptions.RequestException as e:  # Gestion des exceptions liées aux requêtes HTTP
        print("An error occurred:", e)  # Affichage de l'erreur
        sys.exit(1)  # Arrêt du programme en cas d'erreur

if __name__ == "__main__":
    if len(sys.argv) != 2:  # Vérification du nombre d'arguments
        print("Missing employee ID as argument")  # Message d'erreur si l'ID de l'employé est manquant
        sys.exit(1)  # Arrêt du programme avec un code d'erreur

    employee_id = sys.argv[1]  # Récupération de l'ID de l'employé depuis les arguments de ligne de commande
    get_employee_tasks(employee_id)  # Appel de la fonction pour récupérer les tâches de l'employé
