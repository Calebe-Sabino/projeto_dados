import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.mensagem_dados = 'Qual dado gostaria de rolar? (d4, d6, d8, d10, d12, d20, d100): '
        self.mensagem_quantidade = 'Quantos dados gostaria de rolar? '
        self.dados_disponiveis = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']

    def iniciar(self):
        while True:
            resposta = input('Você gostaria de gerar um valor em dado? (sim/não): ').lower()
        
            if resposta == 'sim' or resposta == 's':
                dado = input(self.mensagem_dados).lower()
                if dado in self.dados_disponiveis:
                    self.valor_maximo = int(dado[1:])
                    self.quantidade = int(input(self.mensagem_quantidade))
                    self.gerar_valor_do_dado()
                else:
                    print('Os dados disponíveis são d4, d6, d8, d10, d12, d20 e d100. Por favor, selecione uma das opções.')
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos a sua participação!')
                break
            else:
                print('Por favor, responda sim ou não')

    def gerar_valor_do_dado(self):
        resultados = []
        for j in range(self.quantidade):
            resultados.append(random.randint(self.valor_minimo, self.valor_maximo))
        resultado_individual = (resultados)
        soma_resultados = sum(resultados)
        print(f'Os resultados das rolagens individuais foram: {resultado_individual}')
        print(f'A soma total é {soma_resultados}')

simulador = SimuladorDeDado()
simulador.iniciar()
