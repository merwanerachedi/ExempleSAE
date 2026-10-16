# TP REST - Python

## 1. Objectif

Dans ce TP, on a créé une API REST avec Flask en Python pour gérer une liste d'étudiants.

On utilise les méthodes HTTP GET, POST, PUT et DELETE pour effectuer les différentes opérations.

Les données sont stockées dans une liste Python, donc elles ne sont pas sauvegardées après l'arrêt du serveur.

## 2. Les routes

**GET /**

Permet de vérifier que le serveur fonctionne. Retourne un message de bienvenue.

**GET /students**

Retourne la liste de tous les étudiants au format JSON.

**GET /students/<id>**

Permet de récupérer un étudiant grâce à son identifiant.

Si l'étudiant n'existe pas, on retourne une erreur 404.

**POST /students**

Permet d'ajouter un étudiant à la liste.

On envoie les informations au format JSON et le serveur attribue un identifiant.

Le code 201 indique que l'ajout a réussi.

**PUT /students/<id>**

Permet de modifier les informations d'un étudiant existant.

On récupère les nouvelles données avec `request.get_json()` puis on met à jour l'étudiant.

**DELETE /students/<id>**

Permet de supprimer un étudiant grâce à son identifiant.

La route retourne un message de confirmation.

## 3. Test avec Postman

On a utilisé Postman pour envoyer des requêtes HTTP et tester les différentes routes de notre API.

Pour GET, on a testé la récupération de la liste des étudiants et la recherche par identifiant.

Pour POST, on a envoyé un JSON dans le Body de la requête :

```json
{
    "name": "Ahmed",
    "age": 22
}
```

Pour PUT, on a modifié les informations d'un étudiant avec son identifiant.

Pour DELETE, on a envoyé une requête avec l'identifiant de l'étudiant à supprimer.

On a aussi vérifié les codes de réponse HTTP, notamment `200`, `201` et `404`.

## 4. Exécution

Installer Flask :

```bash
pip install flask
```

Lancer le serveur :

```bash
python app.py
```

Le serveur démarre sur le port `5001`.

On peut ensuite utiliser Postman pour envoyer les requêtes à `http://localhost:5001`.

## 5. Remarques

- `@app.route()` permet de définir les routes.
- `jsonify()` permet de retourner les données au format JSON.
- `request.get_json()` récupère les données envoyées par le client.
- Le mode `debug=True` permet de voir les erreurs pendant le développement.
- Les données sont conservées uniquement en mémoire.
