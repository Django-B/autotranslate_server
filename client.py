import socket


SERVER_ADDRESS = ('192.168.31.70', 1234)

client = socket.socket()

try:
    client.connect(SERVER_ADDRESS)
    print('Вы подключены к серверу')
    print('Для выхода введите "q"')
except ConnectionRefusedError:
    print('Server Connect Failed')
    exit()

while True:
    input_data = input('Введите текст: ')
    if input_data == 'q':
        client.close()
        print('Goodbye!')
        break
    client.send(input_data.encode('UTF-8'))

    data = client.recv(4096).decode('UTF-8').split('&', maxsplit=2)
    print(f'Перевод {data[0]}-{data[1]}:', data[2])
