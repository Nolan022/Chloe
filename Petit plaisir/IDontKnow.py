import time
a = input("Aimes tu Rayan ? (répond pas oui ou non) ")

if a == "oui":
    print("mhhh grosse merde")
    time.sleep(5)
if a == "non":
    print("Tu es nulle")
elif not a == "oui" or "non":
    exit()