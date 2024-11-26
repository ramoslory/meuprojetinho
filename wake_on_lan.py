import socket
import struct

def wake_on_lan(mac_address):
    """Envia um pacote WOL para o MAC Address especificado."""
    mac_address = mac_address.replace(":", "").replace("-", "")
    if len(mac_address) != 12:
        raise ValueError("MAC Address inválido.")
    data = b'FF' * 6 + (mac_address * 16).encode()
    send_data = b''
    for i in range(0, len(data), 2):
        send_data += struct.pack('B', int(data[i:i+2], 16))
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, ('<broadcast>', 9))
    
if __name__ == "__main__":
    mac = input("Digite o MAC Address: ")
    wake_on_lan(mac)
    print("Pacote WOL enviado.")
