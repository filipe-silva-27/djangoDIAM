from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Questao, Opcao, Aluno
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

#def index(request):
#    return HttpResponse("Viva DIAM. Esta e a pagina de entrada da app votacao.")
# Create your views here.

#######views com html templates

#def index(request):
#    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
#    output = ', '.join([q.questao_texto for q in latest_question_list])
#    return HttpResponse(output)

#def detalhe(request, questao_id):
#    return HttpResponse("Esta e a questao %s." % questao_id)

#def resultados(request, questao_id):
#    response = "Estes sao os resultados da questao %s."
#    return HttpResponse(response % questao_id)

#def voto(request, questao_id):
 #   return HttpResponse("Votacao na questao %s." % questao_id)

#def index(request):
#   latest_question_list = Questao.objects.all() #vai buscar todos os objetos
#   # #output = '<br> '.join([q.questao_texto for q in latest_question_list]) #\n não funciona pq html não existe \n
#   output = "<ul>"
#   for q in latest_question_list:
#       output += "<li>" + q.questao_texto + "</li>"        #poe em bullet points
#       output += '<ul>'

#       for o in q.opcao_set.all():
#           output += "<li>" + o.opcao_texto + "</li>"
#       output += "</ul>"

#   output += "</ul>"
#   return HttpResponse(output)
######fim


#######views com templates
def index(request):
    latest_question_list = Questao.objects.all() #vai buscar todos os objetos

    #colocar dicionario com o conteudo a apresentar
    return render(request, 'votacao/index.html', {'latest_question_list': latest_question_list,
                                                  'fruta': 'banana'})



#<!--pag 15  guiao  fazer uma view para cada questao-->
def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})


def texto_toto(request, texto_exemplo):
    return HttpResponse(texto_exemplo)

def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})


#parte 6 do guiao
def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao']) #vai buscar o input do html

    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para votar
            return render(request, 'votacao/detalhe.html', {'questao': questao,'error_message': "Não escolheu uma opção"})
    else:
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()
    # Retorne sempre HttpResponseRedirect depois de
    # tratar os dados POST de um form
    # pois isso impede os dados de serem tratados
    # repetidamente se o utilizador
    # voltar para a página web anterior.
    return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))

def formQuestao(request):
    return render(request, 'votacao/criarquestao.html')

def submeterQuestao(request):
    questao_texto = request.POST['novaQ']
    q=Questao(questao_texto = questao_texto, pub_data=timezone.now())
    q.save()
    return HttpResponseRedirect(reverse('votacao:index'))

def formOpcao(request, questao_id):
    return render(request, 'votacao/criaropcao.html', {'questao_id': questao_id})

def submeterOpcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    nova_opcao = request.POST['novaOp']
    o=Opcao(questao=questao, opcao_texto=nova_opcao)
    o.save()
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))

def apagar_questoes(request, questao_id):
    if not request.user.is_superuser:
       return HttpResponseRedirect(reverse('votacao:index'))
    else:
        questao = Questao.objects.get(pk=questao_id)
        questao.delete()
        return HttpResponseRedirect(reverse('votacao:index'))

def apagar_opcoes(request, questao_id):
    if not request.user.is_superuser:
       return HttpResponseRedirect(reverse('votacao:index'))
    else:
        if questao_id is not None:
            opcao = Opcao.objects.get(questao_id=questao_id, pk=request.POST["opcao"])
            opcao.delete()
            return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao_id,)))
        else:
            return HttpResponse("Nenhuma opcao foi selecionada")

def login_view(request):
    return render(request, 'votacao/login.html')

def dadosLogin_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('votacao:index'))
    else:
        return HttpResponse("Erro ao logar Utilizador")

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("Logout do Utilizador feito ")
    else:
        return HttpResponse("Erro no Logout do Utilizador feito ")

def form_register(request):
    return render(request, "votacao/registar.html")

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    curso = request.POST['curso']

    user = User.objects.create_user(username, email,password)
    aluno = Aluno(user, curso)
    return HttpResponse("Registado")

def mostra_detalhes(request):
    return render(request, 'votacao/mostra_detalhes.html')