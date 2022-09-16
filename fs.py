import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
from pyqrcode import QRCode
import png
import os
import qrcode

PORT = 8010

# changing the directory to access the files desktop
# with the help of os module
# desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
#                        'OneDrive')
cw = os.getcwd()
os.chdir(cw)
 
 
# creating a http request
Handler = http.server.SimpleHTTPRequestHandler
# returns, host name of the system under
# which Python interpreter is executed
hostname = socket.gethostname()
 
 
# finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP
 
 
# converting the IP address into the form of a QRcode
# with the help of pyqrcode module
 
# converts the IP address into a Qrcode
import gen
gen.generate(link)

# def close():
#     devnull = open('/dev/null', 'w')
#     p = subprocess.Popen(["./main"], stdout=devnull, shell=False)
# # Get the process id
#     pid = p.pid
#     return pid
# opens the Qrcode image in the web browser
 
 
# Creating the HTTP request and  serving the
# folder in the PORT 8010,and the pyqrcode is generated
 
# continuous stream of data between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the QRCode")
    httpd.serve_forever()


