from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional 
from uuid import uuid4

class Animal(BaseModel):
    id: Optional[str]
    name: str
    age: int
    gender: str
    color: str

base: List[Animal] = []
  
app = FastAPI()

@app.get('/animais')
def listar_animais():
    return base

@app.post('/animais')
def criar_animais(animal: Animal):
    animal.id = str(uuid4())
    base.append(animal)
    return None


@app.get('/animais/{animal_id}')
def buscar_animal(animal_id: str):    
    for animal in base:
        if animal.id == animal_id:
            return animal
    return {'erro':'Animal não localizado'}


@app.delete('/animais/{animal_id}')
def deletar_animal(animal_id: str):
    posicao = -1
    #Buscar a posição do animal
    for index, animal in enumerate(base):
        if animal.id == animal_id:
            posicao = index
            break
    
    if posicao != -1:
        base.pop(posicao)
        return {'mensagem':'Animal removido com sucesso!!!'}
    
    else:
        return{'Erro':'Animal não encontradoo'}
