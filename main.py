#1.  (0,2 décimos) Ser dinâmico (não pode ser randômico, isso quer dizer que a informação na tela deve ser exibida de acordo com dados dantes informados pelo usuário)
#2.  (0,1 décimos) Apresentar retornos de ajuda ao usuário: Informar ao usuário sobre as possibilidades de recepção dos campos (ex.: “Este campo aceita somente valores inteiros”, e claro, trazer retornos das pesquisas e inserções (avise quando acontecer de o usuário ter informado uma informação inválida, ou ainda, quando houver pesquisa encontrada ou não encontrada.))
#3.  (0,2 décimos) Apresentar estrutura de dados composta heterogênea (EDCH), para aceitar até 5 registros cada, ou seja, com no mínimo 5 campos para preenchimento, que poderão ser manipulados, exemplo: registros advindos da tela de cadastro de aluno, em que devem ser preenchidos os seguintes campos: Matrícula, Nome Completo, RG, CPF e Curso.
#4.  (0,2 décimos) Apresentar um Menu de Opções, onde, seja possível que o usuário escolha um dos tipos de pesquisa tratados nos itens 5 a 8 (ele pode informar a chave de pesquisa, o programa lê a chave, mas, o usuário deve escolher como será tratada internamente a pesquisa da chave)
#5.  (0,5 ponto) Apresentar modo de pesquisa sequencial(linear), sem uso de recurso ou de função pré-definida de bibliotecas em linguagem, para um campo do tipo string/texto, sendo realizado a comparação com a chave informada considerando os dados pesquisados da EDCH que dantes fora instanciada.
#6.  (0,5 ponto) Apresentar modo de pesquisa sequencial(linear), com uso de recurso ou de função pré-definida de bibliotecas em linguagem, para um campo do tipo string/texto, sendo realizado a comparação com a chave informada considerando os dados pesquisados da EDCH que dantes fora instanciada.
#7.  (0,5 ponto) Apresentar modo de pesquisa binário sem uso de recurso ou de função pré-definida de bibliotecas em linguagem, para um campo do tipo numérico, sendo realizado a comparação com a chave informada considerando os dados pesquisados da EDCH que dantes fora instanciada.
#8.  (0,5 ponto) Apresentar modo de pesquisa binário com uso de recurso ou de função pré-definida de bibliotecas em linguagem, para um campo do tipo numérico, sendo realizado a comparação com a chave informada considerando os dados pesquisados da EDCH que dantes fora instanciada.
#9.  (0,2 décimos) Apresentar-se em sua a versão completa em único arquivo, e este, deverá ser compilado, interpretado e em funcionamento sem apresentar erros (não é para enviar o diretório de seu projeto e nem dividi-lo em vários arquivos).
#10. (0,1 décimos) Apresentar comentários identificando apenas o início dos trechos de código em que está sendo evidenciado as soluções (no caso, somente comentar o início das pesquisas: sequencial e binária).
import modelo

def menu_de_busca():
    pass


def main():
    temp_Nome = input("Insira o nome completo: ")
    print(temp_Nome == None)
    
    temp_Nacimento = ''
    temp_Matricula = ''
    temp_RG = ''
    temp_CPF = ''

    

    Igor = modelo.Aluno('0001', 'Igor Pablo da Silva Freitas', '15.03.1992', '1882322', '923.929.123-53')
    Igor.tete()










if __name__ == "__main__":
    main()