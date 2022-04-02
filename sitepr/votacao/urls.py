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
 path("<int:questao_id>/resultados", views.resultados, name="resultados"),
 path("inserir_questao", views.formQuestao, name="formQuestao"),
 path("submeter_Questao", views.submeterQuestao, name='submeterQuestao'),
 path("<int:questao_id>/inserir_opcao", views.formOpcao, name="formOpcao"),
 path("<int:questao_id>/submeter_Opcao", views.submeterOpcao, name='submeterOpcao'),
 path("<int:questao_id>/apagarquestao", views.apagar_questoes, name="apagar_questoes"),
 path("<int:questao_id>/apagaropcao", views.apagar_opcoes, name="apagar_opcoes"),
 path("login", views.login_view, name="login_view"),
 path("dadosLogin", views.dadosLogin_view, name="dadosLogin_view"),
 path("logoutview", views.logoutview, name="logoutview"),
 path("registo", views.form_register, name="form_register"),
 path("registerData", views.register, name="register"),
 path("detalhes", views.mostra_detalhes, name="mostra_detalhes"),

]