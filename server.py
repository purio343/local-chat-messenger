from faker import Faker
import socket
import os

class Person:
    def __init__(self, name, address, job):
       self.name = name
       self.address = address
       self.job = job

    def introduce(self):
       string = f'私の名前は{self.name}です。\n{self.address}に住んでいて、{self.job}として働いています。'
       return string
    
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/tmp/server_socket_1099'

# サーバーソケットがあったら削除
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f'Server starging up on {server_address}')
sock.bind(server_address)
fake = Faker('jp-JP')

try:
 while True:
    print('Waiting to receive message')
    # データを受信
    data, address = sock.recvfrom(4096)
    print(f'Received data: {data.decode()}')

    if data:
    #    fake = Faker('jp-JP')
       person = Person(fake.name(), fake.address(), fake.job())
       sent = sock.sendto(person.introduce().encode('utf-8'), address)
       print(f'sent {sent} bytes to {address}')
finally:
    os.unlink(server_address)