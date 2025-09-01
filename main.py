from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()

class Receita(BaseModel):
    nome : str
    ingredientes : List[str]
    mood_de_preparo : str

receita = List[Receita] = []

@app.get("/receitas/")
def get_todas_receitas():
    return receitas

@app.post("/receitas", response_model-Receita, status_code=status.HTTP_201_CREATED)
def criar_receita(dados : Receita):

    nova_receita = dados
    receitas.append(nova_receita)

    return nova_receita

receitas = [
    {
        'nome': 'Brownie',
        'ingredientes': [
            '3 ovos',
            '6 colheres de açúcar',
            '1/2 xícara (chá) de chocolate em pó',
            '100g de manteiga',
            '1 xícara (chá) de farinha de trigo'
        ],
        'utensílios': [
            'Tigela',
            'Forma',
            'Colher de pau',
            'Forno'
        ],
        'modo_de_preparo': 'Misture todos os ingredientes em uma tigela, coloque a massa em uma forma untada e leve ao forno pré-aquecido a 180°C por cerca de 30 minutos.'
    },
    {
        'nome': 'Torta',
        'ingredientes': [
            '3 ovos',
            '6 colheres de açúcar',
            '1/2 xícara (chá) de chocolate em pó',
            '2 xícaras (chá) de farinha de trigo',
            '1 xícara (chá) de leite',
            '1 colher (sopa) de fermento em pó'
        ],
        'utensílios': [
            'Tigela',
            'Forma',
            'Batedeira ou fouet',
            'Forno'
        ],
        'modo_de_preparo': 'Bata os ovos com o açúcar, adicione os demais ingredientes e misture bem. Coloque em uma forma untada e leve ao forno a 180°C por cerca de 40 minutos.'
    }
]

@app.get("/receitas")
def listar_receitas():
            return receitas


@app.get("/receitas/{nome}")
def buscar_receita(nome: str):
    for receita in receitas:
        if receita['nome'].lower() == nome.lower():
         return receita
    return {"erro": "Receita não encontrada"}