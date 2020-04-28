import string
from random import randrange

from controls.operacoes import *
from app.controls.utils import *
from app.model.models import *

if __name__ == '__main__':
    oper = Operacoes()

    _processo = Processo()
    _processo.descricao = "teste"
    _processo.objetivo = "meu primeiro teste"
    oper.registrarProcesso(_processo)
