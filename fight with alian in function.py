from random import randint 
def report(stamina):
    if stamina >8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamina >5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina >3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina >=1:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")
def alian():
    stamina = 10
    while stamina>0:
        user=input("choose the way you want to fight \n1.fight \n2.attack \n3.hit \n4.run:-")
        if user=="fight":
            print("how?,there is no wepons")
        elif user=="hit" or user=="attack":
            a=randint(0,stamina)
            print(a)
            stamina=stamina-a
            report(stamina)
        elif user=="run":
            print("there is no space for run")
alian()
