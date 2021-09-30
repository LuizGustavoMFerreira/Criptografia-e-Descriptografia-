from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from time import sleep

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def funcao_cripto(msg):
    key = b'1234567890123456'
    iv = b'4567890123456789'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    resultado = cipher.encrypt(pad(msg, AES.block_size))
    sleep(1)
    final = resultado.hex()
    print(f'Sua mensagem criptografada: \033[4;32m{final}\033[m')
    return resultado

def funcao_descripto(codigo):
    key = b'1234567890123456'
    iv = b'4567890123456789'
    decipher = AES.new(key, AES.MODE_CBC, iv)
    final = unpad(decipher.decrypt(codigo), AES.block_size).decode('ASCII')
    sleep(1)
    print(f'Sua mensagem descriptografada: \033[4;34m{final}\033[m')
    return final

while True:
    cabeçalho('LOGIN E SENHA')
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if ((login == 'luiz' or login == 'LUIZ' or login == 'Luiz')) and (senha == '123'):
        break
    else:
        print('\033[31mERRO! Digite seu login ou senha correta!\033[m')
        sleep(1)        

while True:
    cabeçalho('CRIPTOGRAFIA E DESCRIPTOGRAFIA')
    op = input("Digite a opção que deseja: C para criptografar ou D para descriptografar: ")

    if (op == "C") or (op == "c"):
        msg = input("Digite sua mensagem para ser criptografada: ").encode('utf-8')
        funcao_cripto(msg)
        cabeçalho('FIM DO PROGRAMA')
        break
    elif (op == "D") or (op == "d"):
        code = input("Digite sua mensagem para ser descriptografada: ")
        codigo = bytes.fromhex(code)
        funcao_descripto(codigo)
        cabeçalho('FIM DO PROGRAMA')
        break
    else: 
        print('\033 [33mERRO! Digite digite as opções válidas! \033[m')
        sleep(1)