class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message):
        self.message = message



while True:
    try:
        x = int(input('Entre 0 a 10'))
        print(x)
        if(x>10):
            raise InputError('Valor tem q ser menor ou igual 10')
        elif(x<0):
            raise InputError('tem q ser maior qu igual a zero')
        break
    except ValueError:
        print('Valor Invalido, digite somente numeros')
    except InputError as ex:
        print(ex)

