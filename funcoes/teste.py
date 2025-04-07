import subprocess
import platform

def is_host_reachable(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]  # Envia apenas 1 pacote

    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Exemplo de uso
host = "google.com"
if is_host_reachable(host):
    print(f"O host {host} está respondendo!")
else:
    print(f"O host {host} NÃO está respondendo.")
