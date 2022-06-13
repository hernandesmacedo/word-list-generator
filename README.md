# word-list-generator
## Gerador de lista de palavras em Python

Este algoritmo tem como função a leitura de uma entrada contendo um conjunto de palavras chaves e, a partir delas, gera um arquivo *.txt* com palavras associadas.

Para isso, as seguintes estratégias foram tomadas:

- Substituição de caracteres acentuados por não acentuados, e de hífens e sublinhados por espaço;

- Geração de acrônimo de todas as palavras da entrada;

- Geração de acrônimos das palavras grandes da entrada. Esses acrônimos variam de tamanho 1 até a quantidade de palavras grandes total;

- Geração de permutações das palavras grandes;

- Remoção de espaços da entrada;

- Geração de abreviações das palavras grandes da entrada;

- Geração de permutações das abreviações;

- Individualização das palavras da entrada;

- Associação de todas as palavras geradas a 18 sequências numéricas de tamanhos 4, 5 e 6, comumente utilizadas em senhas;

- Todas as palavras geradas são armazenadas em um arquivo *.txt* salvo no mesmo diretório do script `words.py` como nome que segue o padrão *wordlist_data_hora* de execução *("wordlist_AAAAmmDD_HHMMSS.txt")*.
