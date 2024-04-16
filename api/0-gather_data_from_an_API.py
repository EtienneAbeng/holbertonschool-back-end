#!/usr/bin/python3
"""
Recupere les donnees Json de la premiere tâche à partir de l'API JDSON Placeholde
"""
import requests


def team_todo():  # Fonction pour recuperer les donnees JSON
    """
    Recupere les donnees Json de la premiere tâche à partir de l'API JDSON Placeholde
    """
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    # Envoi une méthode HTTP de type GET pour recuperer une information aupres
    # du serveur
    reponse = requests.get(url)

    # Verification de la reussite de la requete
    if reponse.status_code == 200:  # Si la requête a réussi
        json_data = reponse.json()  # Extraction des données JSON
        return json_data  # Renvoi des donnee JSON

    else:
        print("Error: Impossible to recuperate the data in file Json")
        return None  # Indication qu'il n'y a pas de données


todo_data = team_todo()  # Appel de la fonction pour recuperer les donnees JSON

# Affichage des donnees JSON si elles ont des recuperees avec succes
if todo_data:  # Si des donnees ont ete recuperees avec succes
    print(todo data)  # Affichage des doinnees JSON
