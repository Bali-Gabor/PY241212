from random import randint


fajta:dict[int,int]={
    5: 90,
    6: 45,
    7: 35
}

def szelveny(tipus:int)->list[int]:
    while tipus not in fajta.keys():
        print('Ilyen fajta lottó nincs!')
        tipus=int(input('Milyen lottót szeretnél játszani? [5,6,7]   '))
    print('Töltsd ki a szelvényt!')
    mezo=[]
    while len(mezo) < tipus:
        szam=int(input(f'{len(mezo)+1}. szám:  '))
        if szam in mezo: print('Ez a szám már szerepel a szelvényen!')
        elif szam < 1 or szam > fajta[tipus]: print('A szám határértéken kívülre esik!')    
        else: mezo.append(szam)
    mezo.sort()
    print(f'A számaid:              {mezo}')
    return mezo


def sorsolas(tipus:int)->list[int]:
    gepi=[]
    kezi=[]
    while len(gepi) < tipus:
        szam=randint(1,fajta[tipus])
        if szam not in gepi: gepi.append(szam)
    gepi.sort()
    print(f'A gépi sorsolás számai: {gepi}')
    if tipus == 7:
        while len(kezi) < tipus:
            szam=randint(1,fajta[tipus])
            if szam not in kezi: kezi.append(szam)
        kezi.sort()
        print(f'A kézi sorsolás számai: {kezi}')
    return gepi, kezi


def eredmeny(a:list, b:list, c:list, d:int):
    darab=0
    for x in a:
        if x in b:
            darab+=1
    if darab >= d-3: print(f'Gratulálok a gépi sorsoláson NYERTÉL! {darab} találatod van.')
    else: print(f'Sajnos a gépi sorsoláson nem nyertél! {darab} találatod van.')
    darab=0
    if c:
        for x in a:
            if x in c:
                darab+=1
        if darab >= d-3: print(f'Gratulálok a kézi sorsoláson NYERTÉL! {darab} találatod van.')
        else: print(f'Sajnos a kézi sorsoláson nem nyertél! {darab} találatod van.')        