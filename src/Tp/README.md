# Service SOAP StudentService

Service web SOAP développé en Python avec Spyne pour gérer une liste d’étudiants en mémoire.

## Modèle Student

- `id` : identifiant de l’étudiant (entier).
- `name` : nom de l’étudiant (chaîne de caractères).
- `age` : âge de l’étudiant (entier).

## Méthodes

| Méthode | Paramètres | Description | Retour |
| --- | --- | --- | --- |
| `get_all_students` | Aucun | Récupère tous les étudiants. | Liste de `Student` |
| `get_student` | `id` | Recherche un étudiant par son identifiant. | Un `Student` |
| `add_student` | `student` | Ajoute un étudiant si son identifiant est disponible. | Aucun |
| `delete_student` | `id` | Supprime un étudiant par son identifiant. | Aucun |
| `update_student` | `id`, `name`, `age` | Modifie le nom et/ou l’âge d’un étudiant. | Aucun |

Les paramètres `name` et `age` de `update_student` sont facultatifs.

Les données sont perdues au redémarrage du serveur.