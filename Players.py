import socket
import select
import sys
import time
import random
import unittest

class Players():

    def __init__(self, team, playername):
        self.team = ''
        self.playername = ''

# Leikmaður velur sér lið
    def getTeam(self,c,c2):
        while True:
            #try:
            msg = 'Pick a nation' '\n'
            c.send(bytes(msg, 'utf-8'))
            buf = c2.recv(1024)
            msg = buf.decode('utf-8')

            if msg == 'A':
                self.team = 'Argentina'
            elif msg == 'I':
                self.team = 'Iceland'
            elif msg == 'N':
                self.team = 'Nigeria'
            else:
                self.team = 'Croatia'
            break
        return msg
    def getPlayer(self, c, c2):
        while True:
            msg = 'You picked '+self.team+', now pick a player''\n'
            c.send(bytes(msg, 'utf -8'))
            buf = c2.recv(1024)
            msg = buf.decode('utf -8')
            self.playername = msg
            print(self.playername)
            break

s = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
s2 = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
def main():
    #s = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
    #s2 = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
    port = 3030
    port2 = 3031
    cnt=0
    print('test0')
    try:
        s.bind (('',port))
        s2.bind (('',port2))
    except socket.error as msg:
        print( 'Bind failed - aborting' )
        sys.exit ()

    s.listen (5)
    s2.listen (5)

    team = 'I'
    player = '10'
    tem = Players(team,player)

    while True:
        c,addr = s.accept()
        c2,addr2 = s2.accept()
        print('New connection:', addr)
        print('New connection:', addr2)
        c.send(b'Hello\n')
        cnt += 1
        msg='Your id is '+str(cnt)+'\n'
        c.send(bytes(msg ,'utf -8'))
        print('test2')
        tem.getTeam(c,c2)
        print('test3')
        tem.getPlayer(c,c2)
        #print('test3')

    s.close()
    s2.close()

class testMaxFunctions(unittest.TestCase):
    def setup(self): pass
    def test1_getTeam(self):
        c = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
        c2 = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
        self.assertEqual(Players.getTeam(self,c,c2), 'N')
        c.close()
        c2.close()
    def test2_getPlayer(self):
        c = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
        c2 = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
        self.assertEqual(Players.getPlayer(self,c,c2), 'Gylfi')
if __name__ == '__main__':
    #main()
    unittest.main()
