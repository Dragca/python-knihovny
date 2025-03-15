# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/pocty-obyvatel

kraje = [
    ['Hlavní město Praha', '1 280 508'],
    ['Jihočeský kraj', '638 782'],
    ['Jihomoravský kraj', '1 178 812'],
    ['Karlovarský kraj', '296 749'],
    ['Kraj Vysočina', '508 952'],
    ['Královéhradecký kraj', '550 804'],
    ['Liberecký kraj', '440 636'],
    ['Moravskoslezský kraj', '1 209 879'],
    ['Olomoucký kraj', '633 925'],
    ['Pardubický kraj', '517 087'],
    ['Plzeňský kraj', '578 629'],
    ['Středočeský kraj', '1 338 982'],
    ['Ústecký kraj', '821 377'],
    ['Zlínský kraj', '583 698']
]
#1
nazvy_kraju = [kraj[0] for kraj in kraje]
print(nazvy_kraju) 

#2
pocty_obyvatel_kraju = [int(kraj[1].replace(' ', '')) for kraj in kraje]
print(pocty_obyvatel_kraju)
#3
kraje_seznamy = [nazvy_kraju, pocty_obyvatel_kraju]
print(kraje_seznamy)