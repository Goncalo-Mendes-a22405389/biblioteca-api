from ninja import NinjaAPI
from .models import *

api = NinjaAPI(
    title = "API RESTFULL Biblioteca"
)

@api.get("ola/")
def ola(request):
    return {"mensagens" :"ola!"}

@api.get("autores1/")
def autores1(request):
    autores = [
        {'Nome' : a.nome , 'Ano de nascimento' : a.ano_nascimento} for a in Autor.objects.all()
    ]

    return autores

from .schemas import *
from typing import List

@api.get(
    'autores/',
    response = {200 : List[AutorOut]},
    tags = ['Autores']
)

def autores(request):
    return 200, Autor.objects.all()


@api.get(
    "autores/{autor_id}",
    response={
        200 : AutorOut,
        404 : ErrorSchema,
    },
    tags = ['Autores'],
)
def autor(request, autor_id):
    try:
        return 200, Autor.objects.get(id=autor_id)
    except:
        return 404, {"message" :"Autor não encontrado"}
    

@api.post(
    "autores/", 
    response= {201: AutorOut},
    tags = ['Autores'],
)
def cria_autor(request, data: AutorIn):
    autor = Autor.objects.create(**data.dict())

    return 201, autor


