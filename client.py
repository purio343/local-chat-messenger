import socket
import os

server_address = '/tmp/server_socket_1099'
client_address = '/tmp/client_socket_1099'

try:
    os.unlink(client_address)
except FileNotFoundError:
    pass

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.bind(client_address)

message = input('Message to send from the client\n')

try:
    if message:
        print(f'Sending {message} to {server_address}')
        sent = sock.sendto(message.encode('utf-8'), server_address)
        print('Waiting for a response from the server')
        data, server = sock.recvfrom(4096)
        print(f'Received following message:\n{data.decode()}')
except Exception as e:
    print(f'An error occurred:/n {e}')
finally:
    print('Closing socket')
    sock.close()
    os.unlink(client_address)
