init python:
    class FAI:
        def __init__(self,name,kind,HP,SP,ATK,DEF,deck,status):
            self.name=name
            self.HPmax = HP
            self.HP= HP
            self.SP= SP
            self.ATK = ATK
            self.DEF = DEF
            self.kind = kind
            self.deck = deck
            self.status = status
    class Card:
        def __init__(self,NAME,TYPE,MAG,FXN,COST):
            self.NAME = NAME
            self.TYPE = TYPE
            self.MAG = MAG
            self.FXN = FXN
            self.COST = COST
    class Concatenation:
        def __init__(self,NAME,TYPE,MAG,FXN,COST):
            self.NAME = NAME
            self.TYPE = TYPE
            self.MAG = MAG
            self.FXN = FXN
            self.COST = COST
    # class Card:
    #     def __init__(self,name,POW,SPD,fxn,rank):
    #         self.name=name
    #         # self.type =
    #         self.POW = POW
    #         self.SPD = SPD
    #         self.fxn = fxn
    #         self.rank = rank
    class Fxn:
        def __init__(self,name,text):
            #name to display
            self.name=name
            self.text=text
            # self.displayname=name+"()"
    class BattleStatus:
        def __init__(self,name,text,magnitude):
            self.name=name
            self.text=text
            self.magnitude=magnitude

    # ##Slash Functions:
    # Slash_EX = Fxn("Slash","EX","Greatly increase Slash for 1 turn",0.3,1)
    # Slash_A = Fxn("Slash","A","Increase Slash for 3 turns",0.2,3)
    # Slash_B = Fxn("Slash","B","Increase Slash for 3 turns",0.15,3)
    # Slash_C = Fxn("Slash","C","Increase Slash for 3 turns",0.1,3)
    # Slash_D = Fxn("Slash","D","Increase Slash for 3 turns",0.05,3)

    # ##Blast Functions:
    # Blast_EX = Fxn("Blast","EX","Greatly increase Blast for 1 turn",0.3,1)
    # Blast_A = Fxn("Blast","A","Increase Blast for 3 turns",0.2,3)
    # Blast_B = Fxn("Blast","B","Increase Blast for 3 turns",0.15,3)
    # Blast_C = Fxn("Blast","C","Increase Blast for 3 turns",0.1,3)
    # Blast_D = Fxn("Blast","D","Increase Blast for 3 turns",0.05,3)

    # ##Bomb functions:
    # Bomb_EX = Fxn("Bomb","EX","Greatly increase Bomb for 1 turn",0.3,1)
    # Bomb_A = Fxn("Bomb","A","Increase Bomb for 3 turns",0.2,3)
    # Bomb_B = Fxn("Bomb","B","Increase Bomb for 3 turns",0.15,3)
    # Bomb_C = Fxn("Bomb","C","Increase Bomb for 3 turns",0.1,3)
    # Bomb_D = Fxn("Bomb","D","Increase Bomb for 3 turns",0.05,3)

    Freeze = Fxn("Freeze()","Negate 1 execution")
    # Break = Fxn("Break","Break 1 execution")
    Breach = Fxn("Breach()","Inflict SP-Ignoring Damage.")

    Burn = Fxn("Burn()","Apply Burn status to opponent.")
    Damage = Fxn("Damage(MAG)","Inflict Damage.")
    DamageSP = Fxn("DamageSP(MAG)","Inflict Damage to SP.")
    DamageSPself = Fxn("DamageSPself(MAG)","Inflict Damage to own SP.")
    Recover = Fxn("Recover(MAG)","Increase HP.")
    Shield = Fxn("Shield(MAG)","Increase SP.")
    Reflect = Fxn("Reflect(MAG)","Apply Reflect Status:{Negate incoming Damage; BoostATK;}")
    Burn_Self = Fxn("Burnself()","Apply Burn status to self.")
    BoostATK = Fxn("BoostATK()","Increase ATK")
    BoostDEF = Fxn("BoostDEF()","Increase DEF")
    AntiAntiDamage = Fxn("AntiAntiDamage()","Remove all AntiDamage from your opponent")
    HalfHP_self = Fxn("HalfHP_self()","Half current HP of self.")
    Evade = Fxn("NegateDmg()","Negate a Damage function once.")
    ReduceBit = Fxn("ReduceBit()","Reduce opponent's bit value by 1.")
    BoostGun = Fxn("BoostGun()","Increase  MAG of \"Gun\" type Battleware")
    BoostSword = Fxn("BoostSword()","Increase  MAG of \"Sword\" type Battleware")



    # Recover_EX = Fxn("Recover","EX","Recover all HP",,0)
    # Recover_A = Fxn("Recover","A","Gain HP",1000,0)
    # Recover_B = Fxn("Recover","B","Gain some HP",700,0)

    Empty = Fxn("N","")

    # 0 2 4 8 16 32 64 128 256 512 1024
    """
    Average COST for functions

    BITS           1     2     3      4     5      6     7       8
    MAG(Damage)    0.25  0.5   0.75   1.0   1.25   1.5   1.75    2.0
    MAG(Shield)    0.5   0.75  1.0    1.25  1.5    1.75  2.0     2.25
    BoostATK                           *
    BoostDEF                           *
    FXN
    Freeze()       2



    """
    ##name              name             TYPE       MAG    HITS    FXN List               COST

#ILY's cards

    SpamAtk=      Card("SpamAtk",         "Mail",    0.25,    [Damage,Empty],           1)
    MailSaber=    Card("MailSaber",       "Sword",    1.0,    [Damage,Empty],           4)
    HeartBurn=    Card("HeartBurn",       "PowerUp",   0.2,    [BoostATK,Burn_Self],    3)
    ChocolateBar= Card("ChocolateBar",    "Chocolate",0.25,   [Recover,Empty],         2)

#Ave's cards
    FiberBuster=  Card("FiberBuster",    "Gun",      0.75,    [Damage, Empty],         4)
    DataBuster=   Card("DataBuster",     "Gun",      0.75,    [Damage,Empty],         3)

    FiberSword=   Card("FiberSword",     "Sword",    0.25,    [AntiAntiDamage,Damage], 4)
    DataSaber=    Card("DataSaber",      "Sword",    1.0,     [Damage,Empty],           4)
    Vslash=       Card("V-Slash",        "Sword",    0.5,     [Damage,Empty],          2)
    BreakSaber=   Card("BreakSaber",     "Sword",    0.5,     [DamageSP,Damage],       3)

    XAxess=       Card("X-Axess",        "Axe",      0.75,     [DamageSP,Damage],        4)

    Vshot=        Card("V-Shot",         "Gun",      0.6,     [Damage,Empty],          3)
    VirusFlame=   Card("V-Flame",       "Fire",      0.5,     [Damage,Burn],           3)

    DataBomb=     Card("DataBomb",       "Bomb",     1.0,     [Damage,Empty],          4)
    BruteForce=   Card("BruteForce",     "Force",    1.0,     [Damage,BoostATK],      8)
    DataForce=    Card("DataForce",     "Force",    1.0,      [BoostATK,BoostDEF],       6)


    DataDrill=    Card("DataDrill",       "Drill",   1.0,     [DamageSP,Damage],       6)
    Firewall=     Card("Firewall",        "Wall",    0.75,    [Shield,BoostDEF],      4)
    Powersol=     Card("Powersol",        "Wall",    1.0,     [Shield,BoostATK],        4)
    Shieldbit=    Card("Shieldbit",       "Wall",    0.25,     [Shield,Empty],          1)

    Assault=      Card("Assault",       "Tech",    1.0,       [DamageSPself,BoostATK],  2)
    Bitbuster=    Card("Bitbuster",       "Gun",    0.25,     [Damage,ReduceBit],       2)
    # Snipe=        Card("Snipe",           "Gun",    0.0,     [BoostGun,Evade],       6)
    Laserbeam=    Card("Laserbeam",       "Gun",    2.0,      [Damage,Empty],          8)



    Cursorclaw=   Card("Cursorclaw",      "Claw",    1.0,   [Damage,Empty],           2)


    ##NO ART
    # Parasol=      Card("Parasol",      20,     256,     1, "Firewall",         'C')
    # Chainsaw=     Card("Chainsaw",     550,     32,     1, "Break",            'B')
    # SoftDrink=    Card("SoftDrink",    500,    256,     1, "Recover",          'D')
    # Noisewave=    Card("Noisewave",    200,    256,     1, "Firewall",         'C')
    # DataBarrier=  Card("DataBarrier",  300,    256,     1, "Firewall",         'C')

    # Laserbeam=    Card("Laserbeam",    600,    128,     1, "Damage",           'A')
    # WormSlayer=   Card("WormSlayer",   350,    128,     1, "Anti-Worm",        'A')
    # HyperCannon=  Card("HyperCannon",  700,    32,      1,  "Damage",           'A')


    # MegaBomb=    ("MegaBomb",    700,    70)
    # GigaBomb=    ("GigaBomb",    1500,   60)
    #ILY's Deck at the beginning of the game.
    #20 Cards Per deck
    deckdefault = [
        VirusFlame,VirusFlame,
        SpamAtk,DataSaber,
        DataSaber,DataSaber,
        SpamAtk,ChocolateBar,
        ChocolateBar,MailSaber,
        HeartBurn,Shieldbit,
        HeartBurn,BreakSaber,
        XAxess,SpamAtk]

    # deckdefault = [
    #     VirusFlame,DataBomb,
    #     DataDrill,DataBuster,
    #     Vshot,Vslash,
    #     Vslash,DataDrill,
    #     XAxess,XAxess,
    #     XAxess,XAxess,
    #     DataDrill,DataDrill,
    #     BreakSaber,DataDrill,
    #     HeartBurn,BreakSaber,
    #     BreakSaber,BreakSaber]

    #The first deck you will fight.
    decktrojan = [
        VirusFlame,VirusFlame,
        VirusFlame,DataBomb,
        DataBuster,DataBomb,
        DataBuster,DataBuster,
        DataBomb,Cursorclaw,
        Cursorclaw,Cursorclaw,
        Vslash,Vslash,
        Vslash,Vslash,
        Vshot,Vshot,
        Vshot,Vshot]

    deckkeylogger = [
        VirusFlame,VirusFlame,
        VirusFlame,DataBuster,
        DataBuster,DataBuster,
        DataBuster,Vslash,
        DataBomb,Cursorclaw,
        Cursorclaw,Cursorclaw,
        Vslash,Vslash,
        Vslash,Vslash,
        Vshot,Vshot,
        Vshot,Vshot]
    deckransomware = [
        VirusFlame,VirusFlame,
        VirusFlame,DataBuster,
        DataBuster,DataBuster,
        DataBuster,DataBuster,
        Vslash,Vslash,
        Vslash,Vslash,
        Vshot,Vshot,
        Vshot,Vshot]
    deckrootkit = [
        Vshot,Vshot,
        Vshot,Vshot,
        Vslash,Vslash,
        Vslash,Vslash,
        Vslash,Vslash,
        Vshot,Vshot,
        Vslash,Vslash,
        Vslash,Vslash,
        Vshot,Vshot,
        Vshot,Vshot]
    deckvira = [
        Firewall,
        Firewall,Firewall,
        Firewall,DataBuster,
        DataBuster,
        Shieldbit,Shieldbit,
        DataBuster,Shieldbit,
        Shieldbit,
        Powersol,Powersol,
        Firewall,Firewall,
        Shieldbit,
        Powersol,Powersol,
        DataForce,Firewall,

        ]
    deckave = [
        DataBuster,
        DataBuster,DataBuster,
        DataBuster,Firewall,
        Firewall,
        Firewall,Shieldbit,
        DataBomb,DataBomb,
        Laserbeam,
        Shieldbit,Shieldbit,
        Shieldbit,Bitbuster,
        Bitbuster,
        Assault,Assault,
        Assault,Assault]
    deckred = [
        DataSaber,DataSaber,
        DataSaber,DataSaber,
        VirusFlame,VirusFlame,
        Vslash,Vslash,
        Shieldbit,BruteForce,
        DataBomb,BruteForce,
        Laserbeam,Laserbeam,
        Shieldbit,Shieldbit,
        Shieldbit,Shieldbit,
        DataForce,DataForce]


    selectedcard = ""


    mydeck = deckdefault
    Enmydeck = decktrojan
    decknum = len(mydeck)
    import random
    random.shuffle(mydeck)
    random.shuffle(Enmydeck)
    movecard = MoveTransition(0.2)

    card1name = "DataSaber"
    card2name = "FiberSword"
    Enmycard1name = "DataSaber"
    Enmycard2name = "FiberSword"
    EnmySts = []
    PlayerSts = []
    Enmyname = "Trojan Horse"
    #DEFINE CHARACTERS BY NAME,TYPE,HP,DECK,STATUS
    ILY=FAI("ILY","Virus",2500,1250,500,500,deckdefault,[])
    Trojan=FAI("Trojan Horse","Virus",3000,1500,300,250,decktrojan,[])
    Keylogger=FAI("Keylogger","Virus",500,250,300,250,deckkeylogger,[])
    Ransomware=FAI("Ransomware","Virus",600,300,300,250,deckransomware,[])
    Rootkit=FAI("Rootkit","Virus",700,350,300,250,deckrootkit,[])
    Worm=FAI("Worm","Virus",800,400,300,250,deckrootkit,[])
    Vira=FAI("Vira","Antivirus",3500,1750,450,550,deckvira,[])
    CodeRed=FAI("Code Red","Antivirus",4000,1000,500,500,deckred,[])
    Ave=FAI("Ave","Antivirus",3000,1500,550,440,deckave,[])




    # Vira=FAI("Vira","Antivirus",4000,deckvira)


# label battlev2(PFAI,EFAI):
#
#     $okdesktop = False
#     $ map_active=False
#     $ PlayerFAI = PFAI
#     $ Playername = PlayerFAI.name
#     $ PlayerHPmax = PlayerFAI.HP
#     $ PlayerHP = PlayerHPmax
#     $ EnemyFAI = EFAI
#     $ Enmyname = EnemyFAI.name
#     $ EnmyHPmax = EnemyFAI.HP
#     $ EnmyHP = EnmyHPmax
#     $ EnmySts = []
#     $ PlayerSts = []
#     $ Battle_End = False
#     $ burndmg = 0
#     $ ILYSprite('mad')
#     $ ILY_m = 'happy3'
#     $ vcount=0
#     $ hcount=0
#     $ fxnpreview = "Damage"
#
#     $ PlayerAttacked2nd = False
#     scene battlebg
#     with pixellate
#     play music "bgm/Fight_bgm_maoudamashii_cyber14.ogg"
#     show battlering:
#         xalign 0.5 ypos 0.15 yanchor 0.5
#         block:
#             rotate 0
#             linear 15.0 rotate 360
#             repeat
#     show curve:
#         xpos 0.5 xanchor 0.0 ypos 0.15 yanchor 0.5
#     show curve as curve2:
#         xpos 0.5 xanchor 1.0 ypos 0.10 yanchor 0.5
#         zoom -1.0
#
#     show battleroad:
#         yalign 1.0 xalign 0.5
#     show Enemy:
#         xalign 0.5 yanchor 0.32 ypos 0.25
#     show screen decknum
#     with pixellate
#     show screen stats
#     show cardback at poscarddeck
#     # label battleinit:
#
#
#     voice "voice/ILY11C - I'll show you.mp3"
#     $ ILY_m = 'sad'
#     i"I'll show you... What love can do!"
#     label cardcycle:
#         hide card1
#         hide card2
#         hide card3
#         hide card4
#         call drawcards
#         call screen choosecard
#         hide card1
#         hide card2
#         hide card3
#         hide card4
#         call Returns
#
#         if not Battle_End:
#             jump cardcycle
#         elif Battle_End:
#             hide screen decknum
#             if PlayerHP<=0:
#                 call lose
#             else:
#                 call win
#     return


# screen cardgallery:
#     ""
