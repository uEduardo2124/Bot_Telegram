import telebot

API_key = 'Key do seu bot'

bot = telebot.TeleBot(API_key)

valor_basico = 'R$ 2,50'
valor_medio = 'R$ 4,00'
valor_grande = 'R$ 7,00'

@bot.message_handler(commands = ['basico'])
def basico(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo um Brownie básico, obrigado pela preferência e tenha uma boa refeição ;3')

@bot.message_handler(commands = ['medio'])
def medio(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo um Brownie médio, obrigado pela preferência e tenha uma boa refeição ;3')

@bot.message_handler(commands = ['grande'])
def grande(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo um Brownie grande, obrigado pela preferência e tenha uma boa refeição ;3')

@bot.message_handler(commands = ['opcao1'])
def opcao1(mensagem):
    texto = f'''Cardápio:
    Brownie /basico - {valor_basico} (desconto de  5% apartir de 50 unidades por encomenda)
    Brownie /medio  - {valor_medio}  (desconto de 10% apartir de 45 unidades por encomenda)
    Brownie /grande - {valor_grande} (desconto de 15% apartir de 35 unidades por encomenda)
    /Encomendas - cobramos os mesmos preços acima por unidade'''
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands = ['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'Para fazer uma reclamação, envie um email para Eduardomartinsbgw@gmail.com')

@bot.message_handler(commands = ['opcao3'])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, 'Okay, estaremos encaminhando a conversa para um de nossos atendentes, por favor, aguarde um momento ;3')


def verificar(mensagem):
    return True

@bot.message_handler(func = verificar)
def responder(mensagem):
    txt = '''Olá, seja bem vindo aos Brownies do Dudu (por favor, selecione uma das opções abaixo para seu atendimento ;3)
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Fale com um de nossos atendentes
    OBS: Responder qualquer outra coisa não irá funcionar, por favor, selecione uma das opções para prosseguir.'''
    bot.reply_to(mensagem, txt)


bot.polling()
