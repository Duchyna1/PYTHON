from random import randrange

# ü ö ä

slovicka = [
    ['denken', 'an', 'myslit na'],
    ['glauben', 'an', 'verit v, na'],

    ['aufpassen', 'auf', 'davat pozor na'],
    ['sich freuen', 'auf', 'tesit sa na'],
    ['warten', 'auf', 'cakat na'],

    ['anrufen', 'bei', 'zavolat niekomu'],
    ['sich bewerben', 'bei', 'uchadzat sa u'],
    ['arbeiten', 'bei', 'pracovat u'],
    ['sich informieren', 'bei', 'informovat sa u'],
    ['sich entschuldigen', 'bei', 'ospravedlnit sa niekomu'],

    ['brauchen', 'für', 'potrebovat pre, na'],
    ['sich entschuldigen', 'für', 'ospravedlnit sa za'],
    ['sich interessieren', 'für', 'zaujimat sa o'],

    ['aufhören', 'mit', 'prestat s'],
    ['einverstanden sein', 'mit', 'suhlasit s'],
    ['spielen', 'mit', 'hrat sa s'],
    ['sprechen', 'mit', 'hovorit s'],
    ['telefonieren', 'mit', 'telefonovat s'],
    ['vergleichen', 'mit', 'porovnavat s'],

    ['fragen', 'nach', 'pytat sa na'],
    ['suchen', 'nach', 'hladat nieco'],

    ['sich ärgern', 'über', 'nevat sa kvoli, na'],
    ['sich aufregen', 'über', 'rozculovat sa nad'],
    ['erzählen', 'über', 'rozpravat o'],
    ['sich freuen', 'über', 'mat radost z'],
    ['lachen', 'über', 'smiat na nicomu, niekomu'],
    ['schreiben', 'über', 'pisat o'],
    ['sprechen', 'über', 'rozpravat o'],
    ['diskutieren', 'über', 'diskutovat o'],
    ['informieren', 'über', 'informovat o'],
    ['nachdenken', 'über', 'premyslat o'],
    ['weinen', 'über', 'plakat nad'],
    ['wissen', 'über', 'vediet o'],
    ['sich beschweren', 'über', 'stazovat sa na']
]

neviem = [
    ['brauchen', 'für', 'potrebovat pre, na'],
    ['aufhören', 'mit', 'prestat s'],
    ['vergleichen', 'mit', 'porovnavat s'],
    ['suchen', 'nach', 'hladat nieco'],
    ['sich aufregen', 'über', 'rozculovat sa nad'],
    ['sich beschweren', 'über', 'stazovat sa na']
]

mode = int(input('mode: '))

dic = slovicka

while True:
    if input("continue") == 'q':
        break

    else:
        ran = randrange(len(dic))
        print(len(dic))
        print(dic [ran][mode])
        input("show")
        print(dic[ran])
        dic.pop(ran)
        if len(dic) == 0:
            break
        print()
