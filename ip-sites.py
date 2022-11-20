import socket as s

host = "google.com"

Ip = s.gethostbyname(host)

print(f"O IP do host {host} e {Ip}")