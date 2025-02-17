def cifra_cesar(mensagem, chave, modo): # 1=codifica 0=decodifica
    alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ0123456789'
    msg_cript = ''
    for i in mensagem:
        index = alfabeto.find(i)
        if index == -1:
            msg_cript += i
        else:
            new_index = index + chave if modo == 1 else index - chave
            new_index = new_index % len(alfabeto)
            msg_cript += alfabeto[new_index:new_index+1]
    return msg_cript