from datetime import datetime

Maršrutas = [

    [
        'Klaipėda',
        'Kaunas',
        datetime (2024, 10, 20, 10, 35,0),
        datetime ( 2024, 10,20, 13, 35, 0),
        '20',
        'Verslo'
    ],
    [
        'Klaipėda',
        'Vilnius',
        datetime (2024, 10, 20, 9, 00, 0),
        datetime (2024, 10, 20, 13, 30, 0),
        '35',
        'Verslo'
    ],
    [
        'Klaipėda',
        'Palanga',
        datetime (2024, 10, 20, 8, 20, 0),
        datetime (2024, 10, 20, 8, 50, 0),
        '10',
        "Ekonominė"
    ],
    [
        'Klaipėda',
        'Kretinga',
        datetime (2024, 10, 20, 8, 30, 0),
        datetime (2024, 10, 20, 9, 00, 0),
        '10',
        "Ekonominė"
    ],
]

while True:
    print("1. Peržiūrėti kelionių maršrutus")
    print("2. Įtraukti papildomą maršrutą")
    print("3. Redaguoti esamą maršrutą")
    print("4. Pašalinti esamą maršrutą")
    print("5. Išeiti iš programos")
    opt = int(input())
    match opt:
        case 1:
            print("Kelionių maršrutai")
            num = 1
            for kl in Maršrutas:
                print(f'{num} Kelionė iš {kl[0]} į {kl[1]}. Išvyksta {kl[2]}, atvyksta {kl[3]}. Kelionės trukmė - '
                      f'{kl[3] - kl[2]}. Kelionės kaina yra {kl[4]} eurų. Autobuso klasė - {kl[5]}')
                num += 1
        case 2:
            print("Iš kur išvyksta autobusas?")
            klFrom = input()
            print("Į kur važiuoja autobusas")
            klTo = input()
            print("Kada išvyksta autobusas? (yyyy-mm-dd hh:mm:ss)")
            klLeave = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
            print("Kada atvyksta autobusas? (yyyy-mm-dd hh:mm:ss)")
            klArrive = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
            print("Kiek kainuoja kelionė?")
            klPrice = int(input())
            print("Kokia autobuso komforto klasė?")
            klClass = input()
            Maršrutas.append([klFrom, klTo, klLeave, klArrive, klPrice, klClass])
        case 3:
            print("Įveskite maršruto numerį kurį norite redaguoti")
            ed = int(input())
            print(Maršrutas[ed - 1])
            print("Iš kur išvyksta autobusas?")
            klFrom = input()
            print("Į kur važiuoja autobusas")
            klTo = input()
            print("Kada išvyksta autobusas? (yyyy-mm-dd hh:mm:ss)")
            klLeave = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
            print("Kada atvyksta autobusas? (yyyy-mm-dd hh:mm:ss)")
            klArrive = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
            print("Kiek kainuoja kelionė?")
            klPrice = int(input())
            print("Kokia autobuso komforto klasė?")
            klClass = input()
            Maršrutas[ed - 1] = [klFrom, klTo, klLeave, klArrive, klPrice, klClass]
        case 4:
            print("Įveskite maršruto numerį kurį norite pašalinti")
            rem = int(input())
            Maršrutas.pop(rem - 1)
        case 5:
            exit()
