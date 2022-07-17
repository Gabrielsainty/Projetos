# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini

print ('Bem vindo ao pequeno jogo que estou testando em Python!')
jogar = input('Você deseja jogar?' )
if jogar != 'sim':
    print ('Ok então, até mais!')

pergunta1 = input ('Como se chama o fenômeno que envolve a refração da luz que é apreciado por todos? ')
if pergunta1 != 'Arcoiris':
    print ('Sinto muito, resposta errada!')
else: print ('Parabéns,voce conseguiu um ponto!')

pergunta2 = input ('Qual o nome técnico do USB em ingles? ')
if pergunta2 != 'Universal Serial Bus':
    print ('Sinto muito, resposta errada!')
else: print ('Parabéns,voce conseguiu mais um ponto!')

pergunta3 = input ('Como se chama o agente responsável pela troca térmica que ocorre na superfície da CPU? ')
if pergunta3 != 'Pasta Termica':
    print ('Sinto muito, resposta errada!')
else: print ('Parabéns,voce acertou todas as perguntas!')
