# Uppgift 2 - Statistik från skanning
print("=== Uppgift 2 ===")

# 1. Skapa variabler
scanned_hosts = 50
found_vulnerable = 8

# 2. Beräkna andel sårbara maskiner
vulnerability_percentage = (found_vulnerable / scanned_hosts) * 100

# 3. Kontrollera om andelen är större än 10%
is_above_10_percent = vulnerability_percentage > 10

# 4. Skriv ut resultat
print("Skanning statistik:")
print(f"Skannade maskiner: {scanned_hosts}")
print(f"Sårbara maskiner: {found_vulnerable}")
print(f"Andel sårbara: {vulnerability_percentage:.1f}%")
print(f"Över 10% sårbara: {is_above_10_percent}")