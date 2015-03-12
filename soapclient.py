from SOAPpy import SOAPProxy
import socket


def startcalculate(host, port, data=None):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except socket.error:
        sock.close()
        return 'Server is down, try later!'
    sock.close()
    url = str(host) + ':' + str(port)
    conn = SOAPProxy(url)
    # conn.config.dumpSOAPOut = 1        #Debug option for output connection
    # conn.config.dumpSOAPIn = 1         #Debug option for input connection
    if data:
        return str(conn.calculate(data))

if __name__ == '__main__':
    assert startcalculate('localhost', 8080, '2+2*(5-6/2)') == '6'
    print startcalculate('localhost', 8080, '(8+5*2)/(2*3+1)')