# -*- coding: utf-8 -*-
"""
create by Samy Ben dhiab
"""

data = {
    0:['H',    'Hydrogen',    '1.00794',    1,    1,    'Diatomic nonmetal'],
    1:['He',    'Helium',    '4.002602',    18,    1,    'Noble gas'],
    2:['Li',    'Lithium',    '6.941',    1,    2,    'Alkali metal'],
    3:['Be',    'Beryllium',    '9.012182',    2,    2,    'Alkaline earth metal'],
    4:['B',    'Boron',    '10.811',    13,    2,    'Metalloid'],
    5:['C',    'Carbon',    '12.0107',    14,    2,    'Polyatomic nonmetal'],
    6:['N',    'Nitrogen',    '14.0067',    15,    2,    'Diatomic nonmetal'],
    7:['O',    'Oxygen',    '15.9994',    16,    2,    'Diatomic nonmetal'],
    8:['F',    'Fluorine',    '18.9984032',    17,    2,    'Diatomic nonmetal'],
    9:['Ne',    'Neon',    '20.1797',    18,    2,    'Noble gas'],
    10:['Na',    'Sodium',    '22.98976...',    1,    3,    'Alkali metal'],
    11:['Mg',    'Magnesium',    '24.305',    2,    3,    'Alkaline earth metal'],
    12:['Al',    'Aluminium',    '26.9815386',    13,    3,    'Poor metal'],
    13:['Si',    'Silicon',    '28.0855',    14,    3,    'Metalloid'],
    14:['P',    'Phosphorus',    '30.973762',    15,    3,    'Polyatomic nonmetal'],
    15:['S',    'Sulfur',    '32.065',    16,    3,    'Polyatomic nonmetal'],
    16:['Cl',    'Chlorine',    '35.453',    17,    3,    'Diatomic nonmetal'],
    17:['Ar',    'Argon',    '39.948',    18,    3,    'Noble gas'],
    18:['K',    'Potassium',    '39.948',    1,    4,    'Alkali metal'],
    19:['Ca',    'Calcium',    '40.078',    2,    4,    'Alkaline earth metal'],
    20:['Sc',    'Scandium',    '44.955912',    3,    4,    'Transition metal'],
    21:['Ti',    'Titanium',    '47.867',    4,    4,    'Transition metal'],
    22:['V',    'Vanadium',    '50.9415',    5,    4,    'Transition metal'],
    23:['Cr',    'Chromium',    '51.9961',    6,    4,    'Transition metal'],
    24:['Mn',    'Manganese',    '54.938045',    7,    4,    'Transition metal'],
    25:['Fe',    'Iron',    '55.845',    8,    4,    'Transition metal'],
    26:['Co',    'Cobalt',    '58.933195',    9,    4,    'Transition metal'],
    27:['Ni',    'Nickel',    '58.6934',    10,    4,    'Transition metal'],
    28:['Cu',    'Copper',    '63.546',    11,    4,    'Transition metal'],
    29:['Zn',    'Zinc',    '65.38',    12,    4,    'Transition metal'],
    30:['Ga',    'Gallium',    '69.723',    13,    4,    'Poor metal'],
    31:['Ge',    'Germanium',    '72.63',    14,    4,    'Metalloid'],
    32:['As',    'Arsenic',    '74.9216',    15,    4,    'Metalloid'],
    33:['Se',    'Selenium',    '78.96',    16,    4,    'Polyatomic nonmetal'],
    34:['Br',    'Bromine',    '79.904',    17,    4,    'Diatomic nonmetal'],
    35:['Kr',    'Krypton',    '83.798',    18,    4,    'Noble gas'],
    36:['Rb',    'Rubidium',    '85.4678',    1,    5,    'Alkali metal'],
    37:['Sr',    'Strontium',    '87.62',    2,    5,    'Alkaline earth metal'],
    38:['Y',    'Yttrium',    '88.90585',    3,    5,    'Transition metal'],
    39:['Zr',    'Zirconium',    '91.224',    4,    5,    'Transition metal'],
    40:['Nb',    'Niobium',    '92.90628',    5,    5,    'Transition metal'],
    41:['Mo',    'Molybdenum',    '95.96',    6,    5,    'Transition metal'],
    42:['Tc',    'Technetium',    '(98)',    7,    5,    'Transition metal'],
    43:['Ru',    'Ruthenium',    '101.07',    8,    5,    'Transition metal'],
    44:['Rh',    'Rhodium',    '102.9055',    9,    5,    'Transition metal'],
    45:['Pd',    'Palladium',    '106.42',    10,    5,    'Transition metal'],
    46:['Ag',    'Silver',    '107.8682',    11,    5,    'Transition metal'],
    47:['Cd',    'Cadmium',    '112.411',    12,    5,    'Transition metal'],
    48:['In',    'Indium',    '114.818',    13,    5,    'Poor metal'],
    49:['Sn',    'Tin',    '118.71',    14,    5,    'Poor metal'],
    50:['Sb',    'Antimony',    '121.76',    15,    5,    'Metalloid'],
    51:['Te',    'Tellurium',    '127.6',    16,    5,    'Metalloid'],
    52:['I',    'Iodine',    '126.90447',    17,    5,    'Diatomic nonmetal'],
    53:['Xe',    'Xenon',    '131.293',    18,    5,    'Noble gas'],
    54:['Cs',    'Caesium',    '132.9054',    1,    6,    'Alkali metal'],
    55:['Ba',    'Barium',    '132.9054',    2,    6,    'Alkaline earth metal'],
    56:['La',    'Lanthanum',    '138.90547',    4,    9,    'Lanthanide'],
    57:['Ce',    'Cerium',    '140.116',    5,    9,    'Lanthanide'],
    58:['Pr',    'Praseodymium',    '140.90765',    6,    9,    'Lanthanide'],
    59:['Nd',    'Neodymium',    '144.242',    7,    9,    'Lanthanide'],
    60:['Pm',    'Promethium',    '(145)',    8,    9,    'Lanthanide'],
    61:['Sm',    'Samarium',    '150.36',    9,    9,    'Lanthanide'],
    62:['Eu',    'Europium',    '151.964',    10,    9,    'Lanthanide'],
    63:['Gd',    'Gadolinium',    '157.25',    11,    9,    'Lanthanide'],
    64:['Tb',    'Terbium',    '158.92535',    12,    9,    'Lanthanide'],
    65:['Dy',    'Dysprosium',    '162.5',    13,    9,    'Lanthanide'],
    66:['Ho',    'Holmium',    '164.93032',    14,    9,    'Lanthanide'],
    67:['Er',    'Erbium',    '167.259',    15,    9,    'Lanthanide'],
    68:['Tm',    'Thulium',    '168.93421',    16,    9,    'Lanthanide'],
    69:['Yb',    'Ytterbium',    '173.054',    17,    9,    'Lanthanide'],
    70:['Lu',    'Lutetium',    '174.9668',    18,    9,    'Lanthanide'],
    71:['Hf',    'Hafnium',    '178.49',    4,    6,    'Transition metal'],
    72:['Ta',    'Tantalum',    '180.94788',    5,    6,    'Transition metal'],
    73:['W',    'Tungsten',    '183.84',    6,    6,    'Transition metal'],
    74:['Re',    'Rhenium',    '186.207',    7,    6,    'Transition metal'],
    75:['Os',    'Osmium',    '190.23',    8,    6,    'Transition metal'],
    76:['Ir',    'Iridium',    '192.217',    9,    6,    'Transition metal'],
    77:['Pt',    'Platinum',    '195.084',    10,    6,    'Transition metal'],
    78:['Au',    'Gold',    '196.966569',    11,    6,    'Transition metal'],
    79:['Hg',    'Mercury',    '200.59',    12,    6,    'Transition metal'],
    80:['Tl',    'Thallium',    '204.3833',    13,    6,    'Poor metal'],
    81:['Pb',    'Lead',    '207.2',    14,    6,    'Poor metal'],
    82:['Bi',    'Bismuth',    '208.9804',    15,    6,    'Poor metal'],
    83:['Po',    'Polonium',    '(209)',    16,    6,    'Poor metal'],
    84:['At',    'Astatine',    '(210)',    17,    6,    'Metalloid'],
    85:['Rn',    'Radon',    '(222)',    18,    6,    'Noble gas'],
    86:['Fr',    'Francium',    '(223)',    1,    7,    'Alkali metal'],
    87:['Ra',    'Radium',    '(226)',    2,    7,    'Alkaline earth metal'],
    88:['Ac',    'Actinium',    '(227)',    4,    10,    'Actinide'],
    89:['Th',    'Thorium',    '232.03806',    5,    10,    'Actinide'],
    90:['Pa',    'Protactinium',    '231.0588',    6,    10,    'Actinide'],
    91:['U',    'Uranium',    '238.02891',    7,    10,    'Actinide'],
    92:['Np',    'Neptunium',    '(237)',    8,    10,    'Actinide'],
    93:['Pu',    'Plutonium',    '(244)',    9,    10,    'Actinide'],
    94:['Am',    'Americium',    '(243)',    10,    10,    'Actinide'],
    95:['Cm',    'Curium',    '(247)',    11,    10,    'Actinide'],
    96:['Bk',    'Berkelium',    '(247)',    12,    10,    'Actinide'],
    97:['Cf',    'Californium',    '(251)',    13,    10,    'Actinide'],
    98:['Es',    'Einstenium',    '(252)',    14,    10,    'Actinide'],
    99:['Fm',    'Fermium',    '(257)',    15,    10,    'Actinide'],
    100:['Md',    'Mendelevium',    '(258)',    16,    10,    'Actinide'],
    101:['No',    'Nobelium',    '(259)',    17,    10,    'Actinide'],
    102:['Lr',    'Lawrencium',    '(262)',    18,    10,    'Actinide'],
    103:['Rf',    'Rutherfordium',    '(267)',    4,    7,    'Transition metal'],
    104:['Db',    'Dubnium',    '(268)',    5,    7,    'Transition metal'],
    105:['Sg',    'Seaborgium',    '(271)',    6,    7,    'Transition metal'],
    106:['Bh',    'Bohrium',    '(272)',    7,    7,    'Transition metal'],
    107:['Hs',    'Hassium',    '(270)',    8,    7,    'Transition metal'],
    108:['Mt',    'Meitnerium',    '(276)',    9,    7,    'Unknown'],
    109:['Ds',    'Darmstadium',    '(281)',    10,    7,    'Unknown'],
    110:['Rg',    'Roentgenium',    '(280)',    11,    7,    'Unknown'],
    111:['Cn',    'Copernicium',    '(285)',    12,    7,    'Transition metal'],
    112:['Uut',    'Unutrium',    '(284)',    13,    7,    'Unknown'],
    113:['Fl',    'Flerovium',    '(289)',    14,    7,    'Unknown'],
    114:['Uup',    'Ununpentium',    '(288)',    15,    7,    'Unknown'],
    115:['Lv',    'Livermorium',    '(293)',    16,    7,    'Unknown'],
    116:['Uus',    'Ununseptium',    '(294)',    17,    7,    'Unknown'],
    117:['Uuo',    'Ununoctium',    '(294)',    18,    7,    'Unknown'],
}

import pygame
#construire une grille de 18 colonnes et 9 lignes. Remplir les différentes cases par les éléments chimiques correspondant à leur numéro atomique grace au donee de data
pygame.init()
width, height = 1440,800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Table Periodique")
#couleur
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
#police
fontTitre = pygame.font.Font('freesansbold.ttf', 32)
fontTexte = pygame.font.Font('freesansbold.ttf', 20)
fontDescription = pygame.font.Font('freesansbold.ttf', 12)
fontNum = pygame.font.Font('freesansbold.ttf', 8)
#texte
text = fontTitre.render('Table Periodique', True, black, white)
textRect = text.get_rect()
textRect.center = (width // 2, 50)


colors = {'Diatomic nonmetal':'purple',
          'Unknown':'gray',
          'Noble gas':'darkturquoise',
          'Transition metal':'darkolivegreen1',
          'Actinide':'darkolivegreen2',
          'Alkaline earth metal':'orange',
          'Alkali metal':'darkorange',
          'Metalloid':'chartreuse',
          'Poor metal':'yellow',
          'Lanthanide':'darkseagreen',
          'Polyatomic nonmetal':'darkorchid1'

          }
global selected
selected = None

global familles
familles = list(colors.keys())
class element:

    def __init__(self,num,symbole,nom,poids,groupe,colonne,famille):

        #variables
        self.num = num+1
        self.symbole = symbole
        self.nom = nom
        self.poids = poids
        self.groupe = groupe
        self.colonne = colonne
        self.famille = famille
        self.color = colors[famille]
        #vue
        self.width = 80
        self.height = 80
        self.px = (self.groupe-1) * self.width
        self.py = (self.colonne-1) * self.height

    def afficher(self):
        self.afficher2(self.px,self.py)


    def afficher2(self,px,py):
        global familles
        if self.famille in familles :
            pygame.draw.rect(screen, black, (px+2, py+2, self.width-2, self.height-2),width = 2)
            pygame.draw.rect(screen, self.color, (px+4, py+4, self.width-4, self.height-4))
            screen.blit(fontNum.render(str(self.num), True, black, self.color), (px+5, py+5))
            screen.blit(fontTexte.render(self.symbole, True, black, self.color), (px+20, py+20))
            screen.blit(fontDescription.render(self.nom, True, black, self.color), (px+5, py+40))
            screen.blit(fontDescription.render(self.poids, True, black, self.color), (px+5, py+55))

    def afficherfamille(self,px,py):
        global familles
        if self.famille in familles :
            screen.blit(fontTexte.render(self.famille, True, black, white), (px+85, py+20))

    def testHover(self):
        mx, my = pygame.mouse.get_pos()
        global selected

        if (mx>self.px and mx<self.px+self.width and my>self.py and my<self.py+self.height):
            pygame.draw.rect(screen, white, (self.px+2, self.py+2, self.width-2, self.height-2),width = 2)
            selected = self

    def __str__(self):
        return str(self.num+1)+ " " +self.nom+ " " +self.symbole+ " " +str(self.poids)+ " " +str(self.groupe)+ " " +str(self.colonne)






class Bouton:
    def __init__(self,couleur,nom,x,y):
        self.nom = nom
        self.couleur = couleur
        self.x = 40*x+100
        self.y = y
        self.hover = False

    def afficher(self):
        global familles
        if self.nom in familles:
            pygame.draw.rect(screen , green,(self.x,self.y,30,30),width = 2)
            pygame.draw.rect(screen , self.couleur,(self.x+2,self.y+2,30-3,30-3))
        else:
            pygame.draw.rect(screen , red,(self.x,self.y,30,30),width = 2)
            pygame.draw.rect(screen , self.couleur,(self.x+2,self.y+2,30-3,30-3))

    def testHover(self):
        mx, my = pygame.mouse.get_pos()
        global familles

        if (mx>self.x and mx<self.x+30 and my>self.y and my<self.y+30):
            pygame.draw.rect(screen , white,(self.x,self.y,30,30),width=2)
            screen.blit(fontNum.render(self.nom, True, black,white), (self.x, self.y+40))
            self.hover = True
        else:
            self.hover = False

    def Click(self):
        global familles

        if event.type == pygame.MOUSEBUTTONUP and self.hover:
            if self.nom in familles:
                familles.remove(self.nom)
            else:
                familles.append(self.nom)



def afficherElements(elements,boutons):
    #les cases de la grille ont le numero atomique en haut a gauche en petit
    #au centre le symbole chimique
    #en bas le nom de l'element en font description
    #encore plus bas le poids en font description
    for i in elements:
        i.afficher()
        i.testHover()

    if (selected != None):
        selected.afficher2(500,90)
        selected.afficherfamille(500,90)

    for i in boutons:
        i.afficher()
        i.testHover()

elements = []
for i in data:
    elements.append(element(i,data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]))


boutons = []
x=0
for i in colors:
    boutons.append(Bouton(colors[i],i,x,10))
    x+=1

print(elements)
for i in elements:
    print(i)
#boucle


print(familles)

running = True
while running:
    screen.fill(white)
    screen.blit(text, textRect)


    afficherElements(elements,boutons)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        for i in boutons:
            if event.type == pygame.MOUSEBUTTONUP and i.hover:
                i.Click()

    pygame.display.flip()

