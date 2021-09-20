from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html') #Funcao comando para mostrar na aplicacao criada com conteudo html para formatacao da pagina escrito no arquivo index.html na pasta templates dentro da aplicacao parking_app

def carro(request):
    return render(request, 'carro.html')