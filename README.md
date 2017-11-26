Optei por separar o programa em duas partes, para facilitar legibilidade e manipulação. As funções que manipulam, extraem e escrevem os dados estão no arquivo 'correla_fase.py', de onde podem ser importadas. Dessa forma pode se utilizar um programa de analise que recrute essas funções, conforme necessário. Um exemplo de análise possível encontra-se em 'analisa.py'. Neste programa são calculados as médias e os desvios das correlações e dos taus separando a analise entre os clipes ictais e interictais. 


O programa correla_fase.py contém apenas duas funções: correla e escreve_array.
A função correla recebe o 'pattern' dos arquivos que se deseja estudar e retora dois arrays (ou listas) tridimensionais contendo a correlação e o tau, respectivamente. A primeira dimensão representa cada um dos arquivos, a segunda e a terceira representam os canais.
    Argumento obrigatório:
                          - pattern: string com o padrão para encontrar os aquivos que se deseja estudar. Em caso de dúvida procure informações no README
    Argumentos Opcionais:
                         - norm: booleano. Default 'True'. Retorna a correlação normalizada. Com o argumento norm='False' a correlação não é normalizada
                         - array: booleanp. Default 'True'. Retorna corr e tau como arrays. Com o argumento array='False' os valores retornam como listas

A função escreve_array escreve um array com três dimensões de maneira legível em um arquivo. Pode ser utilizado para escrever um array com um número diferente de dimensões, mas pode comprometer a legibilidade.
    Argumentos obigatórios
                           - array: array que desejamos escrever
                           - arquivo: string com o nome do arquivo de saída

Pattern:
A variável pattern consiste em uma string que expressa os padrões de nomeação dos arquivos. Funciona de maneira similar a uma expressão regular: '?' substitui um único caracter e '*' substitui qualquer sequência de caracteres. Abaixo tem alguns exemplos de patterns possíveis e o resultado que seria obtido: 

pattern = 'Patient_1/*_ictal_*mat' #Seleciona todos os ictais do pacientes 1

pattern = 'Patient_?/*_ictal_*mat' #Seleciona todos os ictais de todos os pacientes

pattern = 'Patient_?/*_interictal_*mat' #Seleciona todos os interictais de todos os pacientes

pattern = 'Patient_?/*_testing_*mat' #Seleciona todos os testes de todos os pacientes

pattern = 'Patient_?/*mat' #Seleciona todos os sinais de todos os pacientes

pattern = '*/*_ictal_*mat' #Seleciona os ictais de todos os humanos e cachorros

pattern = 'Dog_?/*_ictal_*mat' #Seleciona todos os ictais de todos os cachorros
