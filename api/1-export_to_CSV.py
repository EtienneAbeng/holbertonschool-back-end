#!/usr/bin/python3

import requests  # Module pour les requêtes HTTP
import csv  # Module pour la manipulation de fichiers CSV
import sys  # Module pour accéder aux arguments de ligne de commande


def export_to_csv(employee_id, tasks):
    """
    Exporte les tâches de l'employé au format CSV dans un fichier.

    Args:
        employee_id (str): L'ID de l'employé.
        tasks (list): La liste des tâches de l'employé.

    Returns:
        None
    """
    employee_name = tasks[0]["user"]["name"]  # Nom de l'employé
    filename = "{}.csv".format(employee_id)  # Nom du fichier CSV

    # Ouverture du fichier CSV en mode écriture
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        # Création d'un objet writer pour écrire dans le fichier CSV
        writer = csv.writer(file)
        # Écriture de l'en-tête CSV
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:  # Boucle à travers les tâches
            # Création de la ligne à écrire
            row = [
                employee_id, employee_name, str(
                    task["completed"]), task["title"]]
            writer.writerow(row)  # Écriture de la ligne dans le fichier CSV

    print("Data exported to {}".format(filename))  # Message de confirmation


def get_employee_tasks(employee_id):
    """
    Récupère tâches de l'employé depuis l'API et les exporte au format CSV.

    Args:
        employee_id (str): L'ID de l'employé.

    Returns:
        None
    """
    URL = "https://jsonplaceholder.typicode.com"  # URL de l'API
    try:
        # Requête GET pour récupérer les tâches de l'employé avec son ID
        response = requests.get(
            "{}/users/{}/todos".format(URL, employee_id),
            params={"_expand": "user"})
        response.raise_for_status()  # Vérification du statut de la réponse
        tasks = response.json()  # Conversion de la réponse en JSON

        # Export des données vers un fichier CSV
        export_to_csv(employee_id, tasks)
        # Gestion des exceptions liées aux requêtes HTTP
    except requests.exceptions.RequestException as e:
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
