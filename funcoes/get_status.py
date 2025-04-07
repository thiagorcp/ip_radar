import subprocess
import platform
import time


def contador():
    for _ in range(0, 29):
        print('.', end=" ")
        time.sleep(1)
    print("")
def ping(ip_host):

    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    qtd_pacotes_env = "1"

    comando = ["ping", parametro, qtd_pacotes_env, ip_host]

    try:
        subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    ips = ['10.0.42.253', '10.0.162.252', '10.0.154.253', '10.0.152.253', '10.0.152.252', '10.0.146.253', '10.0.156.253',
           '10.0.158.253', '10.0.150.253', '10.0.160.253', '10.0.140.253', '10.0.142.253', '10.0.148.253', '10.0.40.114']

    while True:
        for ip in ips:
            print(ping(ip))

        print("-- NOVA TENTATIVA EM 30 SEGUNDOS --")
        contador()