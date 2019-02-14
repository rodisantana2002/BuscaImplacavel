<!--  mode de usar conversor
  a) as bases devem estar no diretorio origem
  b) as basess devem ser renomeadas com os nomes das fontes...caso mais de um arquivo por base. Basta sequenciar os arquivos com numeros
  c) deve ser informado o limite inferior e superior de busca, esses parametros servem para poder extrair de forma fragmentada as listas as serem baixadas
  d) A versão do python sempre deverá ser a 3.7 ou superior

  NOTE(** se rodar uma lista muito grande no o site scihub vai detectar a tentativa de força-bruta e ira bloquear o IP)
-->
python3 conversor.py -p '../bases/origem/' -inf 9 -sup 20

<!--  -->
<!--  mode de usar RodoBot
  a) processo busca por arquivos sinalizados no source preparado pelo conversor
  b) processo executa tentativas enquanto existirem arquivos para serem baixados
-->
python3 rodibot.py
