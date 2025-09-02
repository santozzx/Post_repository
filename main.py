from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List


class Receita(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str


app = FastAPI()


receitas: List[Receita] = [
    {
        'nome': 'Brownie',
        'ingredientes': [
            '3 ovos',
            '6 colheres de açúcar',
            '1/2 xícara (chá) de chocolate em pó',
            '100g de manteiga',
            '1 xícara (chá) de farinha de trigo'
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
        'modo_de_preparo': 'Bata os ovos com o açúcar, adicione os demais ingredientes e misture bem. Coloque em uma forma untada e leve ao forno a 180°C por cerca de 40 minutos.'
    }
]



@app.get("/receitas/{nome}", response_model=Receita)
def buscar_receita(nome: str):
    """
    Busca uma receita por nome, ignorando maiúsculas e minúsculas.
    """
    for receita in receitas:
        if receita.nome.lower() == nome.lower():
            return receita
    

    raise HTTPException(status_code=404, detail="Receita não encontrada")


@app.get("/receitas", response_model=List[Receita])
def listar_receitas():
    """
    Retorna a lista completa de receitas.
    """
    return receitas

@app.post("/receitas", response_model=Receita, status_code=status.HTTP_201_CREATED)
def criar_receita(dados: Receita):
    """
    Cria uma nova receita e a adiciona à lista.
    """
    receitas.append(dados)
    return dados

