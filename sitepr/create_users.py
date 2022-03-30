from django.contrib.auth.models import User
from votacao.models import Aluno

new_users = ['Ana', 'Rui', 'Mario', 'Salvador']


def apagar_users():
    users=User.objects.all()
    for u in users:
        if not u.is_superuser:
            u.delete()

def criar_users():
    for nome in new_users:
        email = nome+'@iscte-iul.pt'
        password = '12345'
        u = User.objects.create_user(nome, email, password)
        a = Aluno(user=u, curso='IGE')
        a.save()

apagar_users()
criar_users()