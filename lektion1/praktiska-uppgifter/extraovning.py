# Extra Uppgift - Inloggningskontroll
print("=== Extra Uppgift ===")

# Testdata - du kan ändra dessa värden för att testa
username = "anna"
password = "lösen"
login_attempts = 3

print("Testar inloggning:")
print(f"Användarnamn: {username}")
print(f"Lösenord längd: {len(password)} tecken")
print(f"Login försök: {login_attempts}")

# Kontrollera villkor
if username == "":
    print("BLOCKERAD: Användarnamn får inte vara tomt")
elif len(password) < 8:
    print("BLOCKERAD: Lösenord måste vara minst 8 tecken")
elif login_attempts > 5:
    print("BLOCKERAD: För många inloggningsförsök")
else:
    print("TILLÅTEN: Inloggning godkänd")