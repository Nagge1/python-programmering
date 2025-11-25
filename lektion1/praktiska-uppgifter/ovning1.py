# Uppgift 1 - Pentest variabler
print("=== Uppgift 1 ===")

# 1. Skapa variabler
target_ip = "192.168.1.100"
open_ports = [22, 80, 443]
vulnerable = True

# 2. Skriv ut värden och datatyper
print(f"Target IP: {target_ip} - Datatyp: {type(target_ip)}")
print(f"Open ports: {open_ports} - Datatyp: {type(open_ports)}")
print(f"Vulnerable: {vulnerable} - Datatyp: {type(vulnerable)}")