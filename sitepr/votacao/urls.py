from django.urls import include, path
from . import views


# (. significa que importa views da mesma directoria)

app_name = 'votacao' #necessario porque a tag {% url %} necessita

urlpatterns = [
 path("", views.index, name="index"),
 path("<int:questao_id>", views.detalhe, name="detalhe"), #definir var inteira que aparece na path -> questao_id é o agumento usado na view detalhe
                                                         #do file views.py. O URL vai ser do tipo 127.0.0.1:80/votacao/idquestao
 path("<str:texto_exemplo>/toto", views.texto_toto, name="texto_toto"),
 path("<int:questao_id>/voto", views.voto, name="voto"),
 path("<int:questao_id>/resultados", views.resultados, name="resultados")

]