import os


def start():
    print("Olá! Welcome Loja Bendita Benê ")
    nome = input("Informe seu nome: ")
    email = input("Informe seu email: ")

    while True:
        resposta = input(
            f'O que você gostaria de saber hoje?{os.linesep}[1] - Quais são os prazos de entrega?{os.linesep}[2] - Quais formas de pagamento vocês aceitam?{os.linesep}[3] - Posso parcelar minha compra?{os.linesep}[4] - Vocês fazem produtos sob encomenda?{os.linesep}')
        processar_resposta(resposta, nome)


        sair = input(f'{os.linesep}Deseja sair? (S para sim, qualquer outra tecla para continuar): ')
        if sair.lower() == 's':
            despedida()
            break

-----------------------------------------------------------------------
def processar_resposta(resposta, nome):
    if resposta == '1':
        print(
            f'{os.linesep}{nome}, os prazos variam de acordo com a região e o tipo de produto. (3 a 5 dias úteis para produtos sob encomenda){os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, aceitamos cartões de crédito, débito, Pix e boleto bancário.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, claro! Parcelamos em até 2 vezes sem juros nos cartões de crédito.{os.linesep}')
    elif resposta == '4':
        print(
            f'{os.linesep}{nome}, sim! Além dos produtos importados, que são de marcas reconhecidas, também personalizamos. Entre em contato para saber mais sobre as opções de personalização e os prazos de produção.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def despedida():
    print(f'{os.linesep}XOXO, EQUIPE BENDITA BENÊ')


if __name__ == '__main__':
    start()
