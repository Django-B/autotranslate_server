import socket
from googletrans import Translator


translator = Translator()
server_lang = 'ru'

SERVER_ADDRESS = ('', 1234)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)
server.listen()
print('Ожидание подключения клиента...')

while True:
    client, address = server.accept()
    print('Новый клиент:', address)

    while True:
        try: 
            data = client.recv(4096)
        except ConnectionResetError:
            pass

        if not data:
            print('Клиент отключился\nОжадаем подключения нового клиента')
            break

        data = data.decode('UTF-8')
        print('Сообщение клиента:', data)

        # Обработка сообщения
        data = translator.translate(data, dest=server_lang)

        print(f'Перевод <{data.src}>-<{server_lang}>:', data.text)

        client.send(f'{data.src}&{data.dest}&{data.text}'.encode('UTF-8'))

    client.close()
