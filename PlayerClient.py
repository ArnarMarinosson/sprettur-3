import socket
import select
import time
from subprocess import call

class player_c(object):

    def __init__(self,s, s2):
        self.s = s
        self.s2= s2

    def playerInfo(self):
        while True:
            time.sleep(0.05)
            buf = self.s.recv(1024)
            msg = buf.decode('utf -8')
            print(msg, end='')

            msg = input('A for Argentina' '\n''I for Iceland' '\n''N for Nigeria' '\n''C for Croatia''\n' '>')
            self.s2.send(bytes(msg,'utf-8'))
            team = msg

            buf = self.s.recv(1024)
            msg = buf.decode('utf -8')
            print(msg, end='')

            if team == 'A':
                msg = input('Messi #10''\n''Higuain #9''\n''>')
                self.s2.send(bytes(msg,'utf-8'))
            elif team == 'I':
                msg = input('Gylfi #10''\n''Aron Einar #17''\n''>')
                self.s2.send(bytes(msg,'utf-8'))
            elif team == 'N':
                msg = input('John Obi Mikel #10''\n''Iwobi #18''\n''>')
                self.s2.send(bytes(msg,'utf-8'))
            else:
                msg = input('Modric #10''\n''Mandzukic #17''\n''>')
                self.s2.send(bytes(msg,'utf-8'))
            break
def main():
    #call('clear')
    s = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
    s.connect(('localhost', 3030))
    s2.connect(('localhost', 3031))

    playr = player_c(s,s2)
    playr.playerInfo()



if __name__ == '__main__':
    main()
