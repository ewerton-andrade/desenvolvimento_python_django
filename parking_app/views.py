from django.shortcuts import render

# Create your views here.
def index(request):
    placas = {
        1: 'VAP-1234',
        2: 'TIC-8500',
        3: 'EAD-4567',
        4: 'REC-1234'
    }

    dados = {
        'placa_do_carro': placas
    }
    return render(request,'index.html', dados) #Funcao comando para mostrar na aplicacao criada com conteudo html para formatacao da pagina escrito no arquivo index.html na pasta templates dentro da aplicacao parking_app

def carro(request):
    return render(request, 'carro.html')