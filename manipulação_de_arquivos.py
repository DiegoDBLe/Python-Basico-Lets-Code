# Manipulação de Arquivos:


# # Abrir arquivo: 1°) cria uma variavel onde vai receber o retorno do método; 2°) método open() onde passa o parametro o caminho(path) do arquivo se tiver na
# # mesma pasta do projeto entao é so digitar o nome do arquivo; 3°) forma de abertura do arquivo, nesteb exemplo utilizaremos o 'r' de leitura.
# arquivo = open('C:\\Users\\thyci\\PycharmProjects\\Lets_Code\\Lets_code_python\\python_basics', 'r', encoding='utf-8')
# # fazer a leitura do texto do arquivo:
# texto = arquivo.read()
# print(texto)
# # Toda vez que abrir um arquivo ele deve set fechado, para nao dar problemas futuros.7
# arquivo.close()


def leituraArquivo():
    '''
    -> criada uma variavel chamada de arquivo. Onde arquivo recebe o método ope() e o nome do arquivo como parametro.
    ->  if (arquivo.mode == 'r'): #Ou seja se o arquivo estiver no mode de leitura 'r'
    - >  conteudo = arquivo.read() # read() método de leitura. ou seja variavel conteudo recebe variavel arquivo no método de leitura
        #OBS: essa maneira é para leitura de arquivos pequenos. Nos casos de leitura de arquivos grandes é na função abaixo.
        print(f'Conteudo do arquivo: {conteudo}')

    -> arquivo.close() # fechadno o arquivo
    :return: sem retorno
    '''
    arquivo = open('dom_casmurro_cap_1.txt', 'r')
    if (arquivo.mode == 'r'):
        conteudo = arquivo.read()
        print(f'Conteudo do arquivo: {conteudo}')

    arquivo.close()


leituraArquivo()