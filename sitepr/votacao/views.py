from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Questao, Opcao
from django.urls import reverse
from django.http import HttpResponseRedirect

#def index(request):
#    return HttpResponse("Viva DIAM. Esta e a pagina de entrada da app votacao.")
# Create your views here.

#######views com html templates

def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    output = ', '.join([q.questao_texto for q in latest_question_list])
    return HttpResponse(output)

def detalhe(request, questao_id):
    return HttpResponse("Esta e a questao %s." % questao_id)

def resultados(request, questao_id):
    response = "Estes sao os resultados da questao %s."
    return HttpResponse(response % questao_id)

def voto(request, questao_id):
    return HttpResponse("Votacao na questao %s." % questao_id)

######fim



def index2(request):
   latest_question_list = Questao.objects.all() #vai buscar todos os objetos
   # #output = '<br> '.join([q.questao_texto for q in latest_question_list]) #\n não funciona pq html não existe \n
   output = "<ul>"
   for q in latest_question_list:
       output += "<li>" + q.questao_texto + "</li>"        #poe em bullet points
       output += '<ul>'

       for o in q.opcao_set.all():
           output += "<li>" + o.opcao_texto + "</li>"
           output += "</ul>"

   output += "</ul>"
   return HttpResponse(output)


#def index2(request):
#    latest_question_list = Questao.objects.all() #vai buscar todos os objetos
#
#    #colocar dicionario com o conteudo a apresentar
#    return render(request, 'votacao/index.html', {'latest_question_list':latest_question_list,
#                                                  'fruta': 'banana',
#                                                  'dinheiro': 25})



#<!--pag 15  guiao  fazer uma view para cada questao-->
def detalhe2(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})


def texto_toto(request, texto_exemplo):
    return HttpResponse(texto_exemplo)

def resultados2(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})


#parte 6 do guiao
def voto2(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])

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