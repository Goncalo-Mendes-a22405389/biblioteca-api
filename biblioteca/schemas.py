from ninja import Schema


from typing import List, Optional


class AutorIn(Schema):
    nome : str
    ano_nascimento: int
    nacionalidade: str
    retrato: Optional[str] = None

class AutorOut(AutorIn):
    id: int
    
class ErrorSchema(Schema):
    message: str

class LivroOut(Schema):
    id : int 
    titulo : str

class AutorComLivrosOut(AutorOut):
    livros : List[LivroOut]