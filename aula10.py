from datetime import date,datetime, time

def trabalhando_date():
    data_atual = date.today()
    print('formato: {}'.format(data_atual.strftime('%d/%m/%y')))
    print('formato: {}'.format(data_atual.strftime('%d/%m/%Y')))
    print('formato: {}'.format(data_atual.strftime('%d %m %Y')))
    print('formato: {}'.format(data_atual.strftime('%A %B %Y')))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual))

def trabalhando_time():
    horario=time(hour=15,minute=18, second=10)
    print(horario.strftime('%H:%M:%S'))

def trabalhando_date_time():
    datahora = datetime.today();
    datahora_str = datahora.strftime('%d/%m/%y %H:%M:%S')
    print(datahora_str);
    print(datahora.strftime('%c'))
    tupla = ('Segunda', 'Terça','Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[datahora.weekday()])
    data_criada = datetime(2018,6,20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string,'%d/%m/%Y')
    print(data_convertida)

# trabalhando_date_time()

data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
hora = time(hour=13, minute=14, second=00)
print('{} às {}'.format(data, hora))


data_atual = datetime.now()
resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S')
print(resultado)

data_viagem = datetime.now() - timedelta(days=1)
print(datetime.now().weekday()) #retornou 0
print(data_viagem)
