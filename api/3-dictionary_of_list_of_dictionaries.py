#!/usr/bin/python3

import json  # Module pour la manipulation de fichiers JSON


def export_to_json(tasks):
    """
    Exporte toutes les tâches des employés au format JSON dans un fichier.

    Args:
        tasks (dict): Un dictionnaire contenant les tâches de chaque employé.

    Returns:
        None
    """
    # Nom du fichier JSON
    filename = "todo_all_employees.json"

    # Ouverture du fichier JSON en mode écriture
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(tasks, file)  # Écriture du dictionnaire JSON dans le fichier


# Exemple d'utilisation
if __name__ == "__main__":
    # Les tâches des employés sous forme de dictionnaire
    tasks = {
        "1": [
            {"username": "Bret", "task": "delectus aut autem", "completed": False},
            {"username": "Bret",
             "task": "quis ut nam facilis et officia qui",
             "completed": False},
            # Ajoutez d'autres tâches ici...
        ],
        "2": [
            {"username": "Antonette",
             "task": "suscipit repellat esse quibusdam voluptatem incidunt",
             "completed": False},
            {"username": "Antonette",
             "task": "distinctio vitae autem nihil ut molestias quo",
             "completed": True},

        ],

    }

    # Exportation des tâches au format JSON
    export_to_json(tasks)
