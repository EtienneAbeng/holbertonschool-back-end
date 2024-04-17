#!/usr/bin/python3

import requests  # Module pour les requêtes HTTP
import json  # Module pour la manipulation de JSON
import sys  # Module pour accéder aux arguments de ligne de commande


def export_to_json(employee_id, tasks):
    employee_name = tasks[0]["user"]["name"]  # Nom de l'employé
    filename = "{}.json".format(employee_id)  # Nom du fichier JSON

    # Création du dictionnaire contenant les tâches de l'employé
    employee_data = {employee_id: [{"task": task["title"],
                                    "completed": task["completed"],
                                    "username": employee_name} for task in tasks]}

    # Écriture des données dans un fichier JSON
    with open(filename, mode="w", encoding="utf-8") as file:
        # Écriture des données JSON dans le fichier
        json.dump(employee_data, file)

    print("Data exported to {}".format(filename))  # Message de confirmation


def get_employee_tasks(employee_id):
    URL = "https://jsonplaceholder.typicode.com"  # URL de l'API
    try:
        # Requête GET pour récupérer les tâches de l'employé
        response = requests.get(
            "{}/users/{}/todos".format(URL, employee_id), params={"_expand": "user"})
        response.raise_for_status()  # Vérification du statut de la réponse
        tasks = response.json()  # Conversion de la réponse en JSON

        # Export des données vers un fichier JSON
        export_to_json(employee_id, tasks)
    except requests.exceptions.RequestException as e:  # Gestion des exceptions
        print("An error occurred:", e)  # Affichage de l'erreur
        sys.exit(1)  # Arrêt du programme en cas d'erreur


if __name__ == "__main__":
    if len(sys.argv) != 2:  # Vérification du nombre d'arguments
        # Message d'erreur si l'ID de l'employé est manquant
        print("Missing employee ID as argument")
        sys.exit(1)  # Arrêt du programme avec un code d'erreur

    # Récupération de l'ID de l'employé depuis les arguments de ligne de
    # commande
    employee_id = sys.argv[1]
    # Appel de la fonction pour récupérer les tâches de l'employé
    get_employee_tasks(employee_id)
