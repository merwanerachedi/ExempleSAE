from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel, Fault
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

# Liste d'étudiants en mémoire
students = [
    {"id": 1, "name": "Youcef", "age": 21},
    {"id": 2, "name": "Samir", "age": 41},
]

# Modèle étudiant
class Student(ComplexModel):
    id = Integer
    name = Unicode
    age = Integer

class StudentService(ServiceBase):

    @rpc(_returns=Iterable(Student))
    def get_all_students(ctx):
        # Renvoie la liste des étudiants
        return [Student(**s) for s in students]

    @rpc(Integer, _returns=Student)
    def get_student(ctx, id):
        s=next((i for i in students if i["id"] == id),None)
        if s:
            return Student(**s)
        raise Fault(
            faultcode="Client",
            faultstring="L'étudiant n'existe pas"
        )

    @rpc(Student)
    def add_student(ctx, student):
        if any(s["id"] == student.id for s in students):
            raise Fault(
                faultcode="Client",
                faultstring="Un étudiant avec cet identifiant existe déjà."
            )

        students.append({
            "id": student.id,
            "name": student.name,
            "age": student.age
        })

    @rpc(Integer)
    def delete_student(ctx, id):
        s = next((i for i in students if i["id"] == id), None)

        if s is None:
            raise Fault(
                faultcode="Client",
                faultstring="L'étudiant n'existe pas"
            )

        students.remove(s)

    @rpc(Integer, Unicode, Integer)
    def update_student(ctx, id, name=None, age=None):
        s = next((i for i in students if i["id"] == id), None)
        if s is None:
            raise Fault(
                faultcode="Client",
                faultstring="L'étudiant n'existe pas"
            )
        if name is not None:
            s["name"] = name
        if age is not None:
            s["age"] = age



# Création de l'application Spyne
application = Application(
    [StudentService],
     tns='spyne.examples.students',
     in_protocol=Soap11(validator='lxml'),
     out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == "__main__":
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Service SOAP démarré sur http://localhost:8000")
    server.serve_forever()