#byMHUONG10
#cho-biet-pet-se-dung-skill/danh-thuong-o-turn-nao
maxmana=int(input('Mana:'))
cost=int(input('Cost:'))
wgen=float(input('Wgenvalue:'))
nmana=maxmana
turnstouse=int(input("How many turns do ur pet use skill once:"))
for i in range(0,20):
    if (i%turnstouse)==0:
        if nmana-cost >= 0:
            nmana=nmana-cost
            print("Turn",i+1,": Use skill")
        else:
            print("Turn",i+1,": Auto attack")
    else:
        print("Turn",i+1,": Auto attack")
    nmana=nmana+wgen
    print('mana:',round(nmana,1))