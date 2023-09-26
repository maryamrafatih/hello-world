import random
javab=random.randint(1,99)
print(type(javab))
hads=input('what is your hads?')
print(type(hads))
while hads!=javab:
    hads=int(hads)
    if hads>javab:
        print('mine is smaller!')
    else:
        print('mine is larger')
    hads=input('what is your hads again?')
    hads=int(hads)
print('wooowoooww!!!you did it!you rock')   

