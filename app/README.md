<!--  mode de usar conversor
  a) as bases devem estar no diretorio origem
  b) as basess devem ser renomeadas com os nomes das fontes...caso mais de um arquivo por base. Basta sequenciar os arquivos com numeros
-->
python3 conversor.py -p '../bases/origem/' -l 10


<!--  mode de usar RodoBot
  a) processo busca por arquivos sinalizados no source preparado pelo conversor
  b) processo executa tentativas enquanto existirem arquivos para serem baixados
-->
python3 rodibot.py
