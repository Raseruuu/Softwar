init python:
    PFAI = ILY
    ILYStatsnow = {
        "name":PFAI.name,
        "HP":PFAI.HP,
        "HPMax":PFAI.HP,
        "SP":PFAI.SP,
        "SPMax":PFAI.SP,
        "ATK":PFAI.ATK,
        "DEF":PFAI.DEF,
        "Deck":PFAI.deck
    }

    playerbits = 8
    playerstats = ILYStatsnow

    playerName = ILYStatsnow["name"]
    playerHP = ILYStatsnow["HP"]
    playerHPMax = ILYStatsnow["HPMax"]
    playerSP = ILYStatsnow["SP"]
    playerSPMax = ILYStatsnow["SPMax"]
    playerATK = ILYStatsnow["ATK"]
    playerDEF = ILYStatsnow["DEF"]

    playerDeck = ILYStatsnow["Deck"]
    battle_done = False
    enemyfirst =False
    map_active=False
    playerbattlecode=[]
screen battlestats:
    frame:
        style_prefix "stats"
        xsize 560 ysize 135
        xpos 0.02 xanchor 0.0 yalign 0.63
        hbox:
            xalign 0.0
            null width 10
            for cards in playerbattlecode:
                add "images/Cards/[cards.NAME].png" at codesize
    frame:
        style_prefix "stats"
        xpos 0.02 xanchor 0.0 yalign 0.06 xsize 425
        vbox:
            hbox:
                style_prefix "battlestats"
                add "Icon_[playerName]"
                null width 8
                vbox:
                    text "{b}[playerName]{/b}"
                    vbox:
                        frame:
                            style_prefix "healthbar"
                            xsize bar_size(playerHP,playerHPMax,200)
                            ysize 8
                            # xsize
                        null height 7
                        text "HP: [playerHP]/[playerHPMax]"
                        null height 10
                        frame:
                            style_prefix "healthbar2"
                            xsize bar_size(playerSP,playerSPMax,200)
                            ysize 8
                        null height 7
                        text "SP: [playerSP]/[playerSPMax]"
                        null height 10
                        # text "ATK: [playerATK]  DEF: [playerDEF]"
                        hbox:
                            if (playerATK<playerATK_m):
                                text "ATK: {color=#0ff} [playerATK_m]{/color}"
                            elif (playerATK>playerATK_m):
                                text "ATK: {color=#f00} [playerATK_m]{/color}"
                            else:
                                text "ATK: [playerATK_m]"
                            null width 20
                            if (playerDEF<playerDEF_m):
                                text "DEF: {color=#0ff}[playerDEF_m]{/color}"
                            elif (playerDEF>playerDEF_m):
                                text "DEF: {color=#f00}[playerDEF_m]{/color}"
                            else:
                                text "DEF: [playerDEF_m]"
            null height 5
            hbox:

                grid 8 2:
                    for fxns in PlayerSts:
                        image "gui/battlests/[fxns].png"
                        if type(fxns)== list:
                            image "gui/battlests/[fxns[0]].png"
                        elif type(fxns) == str:
                            image "gui/battlests/[fxns].png"

                    for fillerz in range(0,16-len(PlayerSts)):
                        null width 50 height 50
            null height 10
                        # hbox:
                        #     text "{b}ATK: [playerATK]{/b}"
                        #     null width 10
                        #     text "{b}DEF: [playerDEF]{/b}"
            vbox:
                frame:
                    style_prefix "bit"
                    hbox:
                        # null width 0
                        grid 8 1:
                            for bit in range(0,playerbits):
                                add "gui/Bit.png"
                            for fillers in range(0,8-playerbits):
                                add "gui/Bit_empty.png"

                    # grid 4 2:
                    #     for bit in range(0,playerbits):
                    #         add "gui/Bit.png"
                    #     for fillers in range(0,8-playerbits):
                    #         null width 28 height 33

    frame:
        style_prefix "stats"
        xpos 0.98 xanchor 1.0 yalign 0.06 xsize 425
        hbox:
                style_prefix "battlestats"
                # add "Icon_[enemyName]"
                vbox:
                    text "{b}[enemyName]{/b}"
                    vbox:
                        frame:
                            style_prefix "healthbar"
                            xsize bar_size(enemyHP,enemyHPMax,200)
                            ysize 8
                        null height 7
                        text "HP: [enemyHP]/[enemyHPMax]"
                        null height 10
                        frame:
                            style_prefix "healthbar2"
                            xsize bar_size(enemySP,enemySPMax,200)
                            ysize 8
                        null height 7
                        text "SP: [enemySP]/[enemySPMax]"
                        null height 10
                        hbox:
                            null height 57
                            grid 8 2:
                                for fxns in EnmySts:
                                    image "gui/battlests/[fxns].png"
                                for fillers in range(0,16-len(EnmySts)):
                                        null width 50 height 50
                        # hbox:
                        #     text "{b}ATK: [enemyATK]{/b}"
                        #     null width 10
                        #     text "{b}DEF: [enemyDEF]{/b}"
style battlestats_text is text:
    color "#fff"
    size 18
style stats_frame is gui_frame:
    right_padding 14
    left_padding 14
    bottom_padding 14
    top_padding 14
style healthbar_frame is gui_frame:
    background Frame("gui/bar.png", 4, 4, tile=gui.frame_tile)
    ysize 25

    right_padding 0
    left_padding 0
    bottom_padding 0
    top_padding 0
style healthbar2_frame is gui_frame:
    background Frame("gui/barblue.png", 4, 4, tile=gui.frame_tile)
    ysize 25

    right_padding 0
    left_padding 0
    bottom_padding 0
    top_padding 0

transform codesize:
    zoom 0.45



label drawcards:
    python:
        playerhand = []
        playerbattlecode = []


        playerhand.append(playerDeck[0])
        playerhand.append(playerDeck[1])
        playerhand.append(playerDeck[2])
        playerhand.append(playerDeck[3])
        playerhand.append(playerDeck[4])
        for deckcard in range (0,5):
            playerDeck.pop(0)
        for handcard in range (0,5):
            playerDeck.append(playerhand[handcard])

        playercard1obj =playerhand[0]
        playercard1name = playerhand[0].NAME
        playercard1ATK = playerhand[0].TYPE
        playercard1DEF = playerhand[0].MAG
        playercard1FXN = playerhand[0].FXN
        playercard1COST = playerhand[0].COST

        playercard2obj =playerhand[1]
        playercard2name = playerhand[1].NAME
        playercard2ATK = playerhand[1].TYPE
        playercard2DEF = playerhand[1].MAG
        playercard2FXN = playerhand[1].FXN
        playercard2COST = playerhand[1].COST

        playercard3obj =playerhand[2]
        playercard3name = playerhand[2].NAME
        playercard3ATK = playerhand[2].TYPE
        playercard3DEF = playerhand[2].MAG
        playercard3FXN = playerhand[2].FXN
        playercard3COST = playerhand[2].COST

        playercard4obj =playerhand[3]
        playercard4name = playerhand[3].NAME
        playercard4ATK = playerhand[3].TYPE
        playercard4DEF = playerhand[3].MAG
        playercard4FXN = playerhand[3].FXN
        playercard4COST = playerhand[3].COST

        playercard5obj =playerhand[4]
        playercard5name =playerhand[4].NAME
        playercard5TYPE = playerhand[4].TYPE
        playercard5MAG = playerhand[4].MAG
        playercard5FXN = playerhand[4].FXN
        playercard5COST = playerhand[4].COST

        playerhandcosts = []
        playerhand2 = playerhand
    # call check_cost
    return
# label check_cost:
    # $ playerhandcosts = []
    # python:
    #     for cards in playerhand2:
    #         playerhandcosts.append(cards)
    # $ playerhandminimumcost = min(playerhandcosts)
    # return

    # call Damageplayer(1.0)
    # return
image cardflash:
    "cardflasher"
    xalign 0.5 ypos 0.7 yanchor 0.5 zoom 0.9
    linear 0.05 zoom 1.3
    linear 0.05 zoom 1.2

image cardflashenemy:
    "cardflasher"
    xalign 0.5 ypos 0.3 yanchor 0.5 zoom 0.9
    linear 0.05 zoom 1.3
    linear 0.05 zoom 1.2




label Slashfxn(FXNobject):
    # FXNobject.RANK
    # FXNobject.NAME

    "Slash"
    return
label Bombfxn():
    "Slash"
    return


label battlev3(PFAI,EFAI):
    $ ILY_m="sad"
    $ ILY_e="2"
    $ ILY_p="0"

    $ battle_done=False
    $ playerName = PFAI.name
    $ playerHP = PFAI.HP
    $ playerSP = PFAI.SP
    $ playerATK = PFAI.ATK
    $ playerDEF = PFAI.DEF
    $ playerDeck = PFAI.deck


    python:
        hcount=0
        vcount=0
        ahcount=0
        avcount=0

        playerbits = 8
        random.shuffle(playerDeck)
        # playerstats = ILYStatsnow
        battle_done = False
        enemyfirst =False
        map_active=False
        playerbattlecode=[]
        playerSP = ILYStatsnow["SPMax"]
        playerATK_m = playerATK
        playerDEF_m = playerDEF

        EnmySts = []
        PlayerSts = []
        PlayerFAIstats = ILYStatsnow
        EnemyFAIstats = {
            "name":EFAI.name,
            "HP":EFAI.HP,
            "HPMAX":EFAI.SP,
            "SP":EFAI.SP,
            "SPMAX":EFAI.SP,
            "Deck":EFAI.deck,
            "ATK":EFAI.ATK,
            "DEF":EFAI.DEF

        }
        enemyName = EnemyFAIstats["name"]
        enemyHP = EnemyFAIstats["HP"]
        enemyHPMax = EnemyFAIstats["HP"]
        enemySP = EnemyFAIstats["SP"]
        enemySPMax = EnemyFAIstats["SP"]
        enemyDeck = EnemyFAIstats["Deck"]
        enemyATK = EnemyFAIstats["ATK"]
        enemyDEF = EnemyFAIstats["DEF"]
        enemyATK_m = enemyATK
        enemyDEF_m = enemyDEF
        random.shuffle(enemyDeck)
    scene battlebg
    with pixellate

    if enemyName=="Ave":
        play music "bgm/ost/BOSSBATTLE-A_by-Noyemi_K.ogg"
    elif enemyName=="Vira":
        play music "<from 0 to 16.9>bgm/ost/BOSSBATTLE-V_by-StarryMarshmell_0.ogg"
        queue music "bgm/ost/BOSSBATTLE-V-Loop_by-StarryMarshmell_0.ogg"
        # queue music "bgm/ost/BOSSBATTLE-V-Loop_by-StarryMarshmell_0.ogg"

    else:
        play music "bgm/Fight_bgm_maoudamashii_cyber14.ogg"
    show battlering:
        xalign 0.5 ypos 0.15 yanchor 0.5
        block:
            rotate 0
            linear 15.0 rotate 360
            repeat
    show curve:
        xpos 0.5 xanchor 0.0 ypos 0.15 yanchor 0.5
    show curve as curve2:
        xpos 0.5 xanchor 1.0 ypos 0.17 yanchor 0.5
        zoom -1.0

    show battleroad:
        yalign 1.0 xalign 0.5
    show Enemy:
        xalign 0.5 yanchor 0.32 ypos 0.25


    voice "voice/ILY11C - I'll show you.mp3"

    $ ILY_m = 'sad'
    i"I'll show you... What love can do!"
    if enemyName=="Ave":
       voice "voice/Ave_voice/I'm-The-Ultimate-Antivirus.ogg"
       a"I'm the Ultimate Antivirus!"
    # show screen decknum
    # with pixellate
    # show screen stats
    # show cardback at poscarddeck
    # label battleinit:


    show screen battlestats
    call showphasemsg("SOFTWAR BEGIN!")
    #Start Dialogue
    $ phasenum=0
    label battleloop:
        # if enemyfirst:
        #     call enemyattack
        if not battle_done:
            pass
        # elif battle_done:
        #     call showphasemsg("BATTLE_END")
        call drawcards
        call screen Activate_Battleware
        play sound "sound/Phase.wav" channel 1
        python:
            card1clicked = False
            card2clicked = False
            card3clicked = False
            card4clicked = False
            card5clicked = False

        label Codephase:

            call screen choosecardv2
            call Returns
            $ card1usable = (playercard1COST<=playerbits) and (card1clicked==False)
            $ card2usable = (playercard2COST<=playerbits) and (card2clicked==False)
            $ card3usable = (playercard3COST<=playerbits) and (card3clicked==False)
            $ card4usable = (playercard4COST<=playerbits) and (card4clicked==False)
            $ card5usable = (playercard5COST<=playerbits) and (card5clicked==False)
            $ cardusable = (((card1usable) or (card2usable)) or ((card3usable) or (card4usable))) or (card5usable)
            if (playerbits > 0) and cardusable:
                jump Codephase
            else:
                call screen Execute
                call Returns
                # if not enemyfirst:
                #     call enemyattack
            #Execute button runs "Execution" label
        if not battle_done:
            jump battleloop
        elif battle_done:

            show screen phasemsg("BATTLE_END")
            $renpy.pause(0.9,hard=True)
            hide screen phasemsg
            hide screen battlestats
            if playerHP<=0:
                stop music
                call lose
            else:
                play music "bgm/bgm_maoudamashii_cyber16.mp3"
                show Enemy:
                    linear 0.15 zoom 0.94
                    xoffset 0.12 yoffset 0.2 alpha 0.5
                    pause .05
                    xoffset 0.-17 yoffset 0.-17 alpha 0.8
                    pause .05
                    xoffset 0.13 yoffset 0.2 alpha 1.0
                    pause 0.1
                    xoffset 0.-19 yoffset 0.11
                    pause 0.1
                    xoffset 0.12 yoffset 0.2 alpha 0.5
                    pause .05
                    xoffset 0 yoffset 0
                    linear 0.1 zoom 0.8 alpha 0.0
                $ renpy.pause(0.4,hard=True)
                call win


    return
screen Execute:
    imagebutton idle "gui/Execute.png" hover "gui/Execute_hover.png" action  Play("sound","sound/Execute.wav"), Return("Execute") xalign 0.5 yalign 0.95
    key "K_BACKSPACE" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
    key "x" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
    key 'K_RETURN' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
    key 'K_KP_ENTER' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
    imagebutton idle "images/Cards/cardreturn.png" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback() hovered Show("card6hover"), Play("sound","sfx/select.wav") unhovered Hide("card6hover") xpos 0.86 xanchor 0.5 yalign 0.95
    key 'z' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
    key 'Z' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
screen phasemsg(Message):
    frame:

        xalign 0.5 yalign 0.5 xsize 1280 at phasetrans
        text "{b}{size=100}[Message]{/b}{/size}" xalign 0.5 yalign 0.5
transform phasetrans:
    on show:
        yzoom 0.0
        linear 0.08 yzoom 1.1
        linear 0.02 yzoom 1.0
    on hide:
        linear 0.1 yzoom 0.0

label showphasemsg(msg):
    show screen phasemsg(msg)
    $renpy.pause(0.9,hard=True)
    hide screen phasemsg
    return


transform zoomBattlecards:
    zoom 0.6
screen choosecardv2:
        if (playercard1COST<=playerbits) and (card1clicked==False):
            ###TODO:: ADD HOVER DESCRIPTION Layered Images
            imagebutton idle "card1" action Play("sound","sound/Phase.wav"), Hide("card1hover"), Return("card1") hovered Show("card1hover"), Play("sound","sfx/select.wav") unhovered Hide("card1hover") at zoomBattlecards xpos 0.26 xanchor 0.5 yalign 0.95
        else:
            add "images/Cards/cardblank2.png" xpos 0.26 xanchor 0.5 yalign 0.95
        if (playercard2COST<=playerbits) and (card2clicked==False):
            imagebutton idle "card2" action Play("sound","sound/Phase.wav"), Hide("card2hover"), Return("card2")  hovered Show("card2hover"), Play("sound","sfx/select.wav") unhovered Hide("card2hover") at zoomBattlecards xpos 0.38 xanchor 0.5 yalign 0.95
        else:
            add "images/Cards/cardblank2.png" xpos 0.38 xanchor 0.5 yalign 0.95
        if (playercard3COST<=playerbits) and (card3clicked==False):
            imagebutton idle "card3" action Play("sound","sound/Phase.wav"), Hide("card3hover"), Return("card3")  hovered Show("card3hover"), Play("sound","sfx/select.wav") unhovered Hide("card3hover") at zoomBattlecards xpos 0.5 xanchor 0.5 yalign 0.95
        else:
            add "images/Cards/cardblank2.png" xpos 0.5 xanchor 0.5 yalign 0.95
        if (playercard4COST<=playerbits) and (card4clicked==False):
            imagebutton idle "card4" action Play("sound","sound/Phase.wav"), Hide("card4hover"), Return("card4")  hovered Show("card4hover"), Play("sound","sfx/select.wav") unhovered Hide("card4hover") at zoomBattlecards xpos 0.62 xanchor 0.5 yalign 0.95
        else:
            add "images/Cards/cardblank2.png" xpos 0.62 xanchor 0.5 yalign 0.95
        if (playercard5COST<=playerbits) and (card5clicked==False):
            imagebutton idle "card5" action Play("sound","sound/Phase.wav"), Hide("card5hover"), Return("card5") hovered Show("card5hover"), Play("sound","sfx/select.wav") unhovered Hide("card5hover") at zoomBattlecards xpos 0.74 xanchor 0.5 yalign 0.95
        else:
            add "images/Cards/cardblank2.png" xpos 0.74 xanchor 0.5 yalign 0.95
        if playerbattlecode!=[]:
            imagebutton idle "images/Cards/cardreturn.png" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback() hovered Show("card6hover"), Play("sound","sfx/select.wav") unhovered Hide("card6hover") xpos 0.86 xanchor 0.5 yalign 0.95
            key "K_BACKSPACE" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
            key "x" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
        else:

            add "images/Cards/cardblank2.png" xpos 0.86 xanchor 0.5 yalign 0.95
screen Activate_Battleware:
        add "images/Cards/cardblank2.png" xpos 0.26 xanchor 0.5 yalign 0.95
        add "images/Cards/cardblank2.png" xpos 0.38 xanchor 0.5 yalign 0.95
        add "images/Cards/cardblank2.png" xpos 0.5 xanchor 0.5 yalign 0.95
        add "images/Cards/cardblank2.png" xpos 0.62 xanchor 0.5 yalign 0.95
        add "images/Cards/cardblank2.png" xpos 0.74 xanchor 0.5 yalign 0.95
        text "{size=50}{b}ACTIVATE BATTLEWARE{/size}{/b}" xpos 0.5 xanchor 0.5 yalign 0.87 at alphablinking
        key 'mouseup_1' action Return()
        key 'K_RETURN' action Return()
        key 'K_SPACE' action Return()
        key 'K_KP_ENTER' action Return()
        key 'K_SELECT' action Return()
        key 'K_LEFT' action Return()
        key 'K_RIGHT' action Return()
        key 'K_UP' action Return()
        key 'K_DOWN' action Return()
        key 'Z' action Return()
        key 'z' action Return()
transform alphablinking:
    ease 0.25 alpha 0.0
    ease 0.25 alpha 1.0
    repeat
image selectring:
    "images/Cards/selectring.png"
    rotate 0 zoom 1.4
    linear 4.0 rotate 360
    repeat
screen card1hover:
    # image "selectring" xanchor 0.5 xpos 0.26 yanchor 0.5 ypos 0.75
    image "card1" xanchor 0.5 xpos 0.26 yalign 0.95 at cardtrans
screen card2hover:
    # image "selectring" xanchor 0.5 xpos 0.38 yanchor 0.5 ypos 0.75
    image "card2" xanchor 0.5 xpos 0.38 yalign 0.95 at cardtrans
screen card3hover:
    # image "selectring" xanchor 0.5 xpos 0.5 yanchor 0.5 ypos 0.75
    image "card3" xanchor 0.5 xpos 0.5 yalign 0.95 at cardtrans
screen card4hover:
    # image "selectring" xanchor 0.5 xpos 0.62 yanchor 0.5 ypos 0.75
    image "card4" xanchor 0.5 xpos 0.62 yalign 0.95 at cardtrans
screen card5hover:
    # image "selectring" xanchor 0.5 xpos 0.74 yanchor 0.5 ypos 0.75
    image "card5" xanchor 0.5 xpos 0.74 yalign 0.95 at cardtrans
screen card6hover:
    # image "selectring" xanchor 0.5 xpos 0.86 yanchor 0.5 ypos 0.75
    image "images/Cards/cardreturn.png" xanchor 0.5 xpos 0.86 yalign 0.95 at cardtrans2



label ConcatenationExec:
    ""
