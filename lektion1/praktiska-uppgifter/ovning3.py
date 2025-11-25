# Uppgift 3 - Logganalys
print("=== Uppgift 3 ===")

# 1. Skapa variabel
log = "2025-11-13 12:55:21 - LOGIN FAILED - user=root"

# 2. Extrahera delar med slicing
datum = log[0:10]  # Första 10 tecknen
tid = log[11:19]   # Tid-delen
status = log[22:35] # "LOGIN FAILED"
anvandarnamn = log[42:] # Allt efter "user="

# 3. Skriv ut varje del
print("Datum:", datum)
print("Tid:", tid)
print("Status:", status)
print("Användarnamn:", anvandarnamn)

# 4. Vänd strängen baklänges
log_baklanges = log[::-1]
print("Baklänges:", log_baklanges)