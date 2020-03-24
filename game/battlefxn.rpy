init python:

    def statusAppend(stslist,statusstring):
        if len(stslist)==16:
            stslist.pop(0)
            #FIFO First in, First out.
            print(stslist)
            print(statusstring)
        stslist.append(statusstring)

        return stslist
image bit:
    "gui/Bit.png"
    zoom 4.0
label Damageenemy:

  $ Magnitude = (currentcardMAG)

  $ damagetoenemy=int(playerATK_m*Magnitude)
  if currentcardTYPE == "Sword":
    play sound "sfx/slash.wav"
  elif currentcardTYPE == "Axe":
    play sound "sfx/slash.wav"
  elif currentcardTYPE == "Fire":
    play sound "sfx/Bust.wav"
  elif currentcardTYPE == "Gun":
    play sound "sfx/Bust.wav"
  else:
    if runnumber>1:
      play sound "sfx/sfx_exp_short_hard8.wav"
    else:
      play sound "sfx/sfx_exp_short_hard9.wav"
  call hurtnoise_Ave
  python:
    if enemySP>0:
        enemySP-=damagetoenemy
        if enemySP<0:
            enemyHP+=enemySP
            enemySP = 0
    else:
        enemyHP-=damagetoenemy

    if enemyHP <=0:
        enemyHP = 0
        battle_done=True
    dmgdist = ((currentcard.MAG*100)/20)
    dmgdist = int(dmgdist*2)

  show dmgpoint
  show Enemy:
    linear 0.05 zoom 0.96
    xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
    pause .05
    xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
    pause .05
    xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
    pause 0.05
    xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
    pause 0.05
    xoffset 0 yoffset 0
    linear 0.05 zoom 1.0
  $ renpy.pause(0.6,hard=True)
  return
label DamageSPplayer:
    if playerSP>0:
        $ Magnitude = (currentcardMAG)
        $ damagetoplayer=int(enemyATK_m*Magnitude)

        if currentcardTYPE == "Sword":
          play sound "sfx/slash.wav"
        elif currentcardTYPE == "Axe":
          play sound "sfx/slash.wav"
        elif currentcardTYPE == "Fire":
          play sound "sfx/Bust.wav"
        elif currentcardTYPE == "Gun":
          play sound "sfx/Bust.wav"
        else:
          if runnumber>1:
            play sound "sfx/sfx_exp_short_hard8.wav"
          else:
            play sound "sfx/sfx_exp_short_hard9.wav"
        call hurtnoise_Ave
        $ playerSP-=damagetoplayer
        if playerSP<0:
            $ playerSP=0

        $ dmgdist = ((currentcard.MAG*100)/20)
        $ dmgdist = int(dmgdist*2)

        show playerdmgpoint onlayer overlay
        # call hurtnoise
        with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
        $ renpy.pause(0.6,hard=True)
    return
label DamageSPenemy:
    if enemySP>0:
        $ Magnitude = (currentcardMAG)
        $ damagetoenemy=int(playerATK_m*Magnitude)

        if currentcardTYPE == "Sword":
          play sound "sfx/slash.wav"
        elif currentcardTYPE == "Axe":
          play sound "sfx/slash.wav"
        elif currentcardTYPE == "Fire":
          play sound "sfx/Bust.wav"
        elif currentcardTYPE == "Gun":
          play sound "sfx/Bust.wav"
        else:
          if runnumber>1:
            play sound "sfx/sfx_exp_short_hard8.wav"
          else:
            play sound "sfx/sfx_exp_short_hard9.wav"
        call hurtnoise_Ave
        $ enemySP-=damagetoenemy
        if enemySP<0:
            $ enemySP=0
        $ dmgdist = ((currentcard.MAG*100)/20)
        $ dmgdist = int(dmgdist*2)
        show dmgpoint
        show Enemy:
            linear 0.05 zoom 0.96
            xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
            pause .05
            xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
            pause .05
            xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
            pause 0.05
            xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
            pause 0.05
            xoffset 0 yoffset 0
            linear 0.05 zoom 1.0
        $ renpy.pause(0.6,hard=True)
    return
label DamageSPselfenemy:
    if enemySP>0:
        $ Magnitude = (currentcardMAG)
        $ damagetoenemy=int(enemyATK_m*Magnitude)

        if currentcardTYPE == "Sword":
          play sound "sfx/slash.wav"
        elif currentcardTYPE == "Axe":
          play sound "sfx/slash.wav"
        elif currentcardTYPE == "Fire":
          play sound "sfx/Bust.wav"
        elif currentcardTYPE == "Gun":
          play sound "sfx/Bust.wav"
        else:
          if runnumber>1:
            play sound "sfx/sfx_exp_short_hard8.wav"
          else:
            play sound "sfx/sfx_exp_short_hard9.wav"
        call hurtnoise_Ave
        $ enemySP-=damagetoenemy
        if enemySP<0:
            $ enemySP=0
        $ dmgdist = ((currentcard.MAG*100)/20)
        $ dmgdist = int(dmgdist*2)
        show dmgpoint
        show Enemy:
            linear 0.05 zoom 0.96
            xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
            pause .05
            xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
            pause .05
            xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
            pause 0.05
            xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
            pause 0.05
            xoffset 0 yoffset 0
            linear 0.05 zoom 1.0
        $ renpy.pause(0.6,hard=True)
    return
label Burnenemy:
    play sound "sfx/fire.wav"
    # $ EnmySts.append("burn")
    $ EnmySts=statusAppend(EnmySts,"burn")
    show Brnsts:
      zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide Brnsts
    return
label ReduceBitself:
    play sound "sfx/sfx_exp_odd3.wav"
    $ playerbits-=1
    $ dmgdist = 10
    show bit onlayer overlay:
      xalign 0.5 ypos 0.78 yanchor 0.5
      linear 0.05 zoom 0.96
      xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
      pause .05
      xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.6
      pause .05
      xoffset (dmgdist) yoffset (dmgdist) alpha 0.5
      pause 0.05
      xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
      pause 0.05
      ease 0.2 xoffset 0 yoffset 0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide bit
    return
label ReduceBit:
    play sound "sfx/sfx_exp_odd3.wav"
    $ enemybits-=1
    $ dmgdist = 10
    show bit onlayer overlay:
      xalign 0.5 ypos 0.25 yanchor 0.5
      linear 0.05 zoom 0.96
      xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
      pause .05
      xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.6
      pause .05
      xoffset (dmgdist) yoffset (dmgdist) alpha 0.5
      pause 0.05
      xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
      pause 0.05
      ease 0.2 xoffset 0 yoffset 0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide bit
    return
label AddBitself:
    play sound "sfx/sfx_exp_odd3.wav"
    $ playerbits+=1
    show bit onlayer overlay:
      xalign 0.5 ypos 0.78 yanchor 0.5
      linear 0.05 zoom 0.96
      xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
      pause .05
      xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.6
      pause .05
      xoffset (dmgdist) yoffset (dmgdist) alpha 0.5
      pause 0.05
      xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
      pause 0.05
      ease 0.2 xoffset 0 yoffset 0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide bit
    return
label Burnself:
    play sound "sfx/fire.wav"
    # $ PlayerSts.append("burn")
    $ PlayerSts=statusAppend(PlayerSts,"burn")
    show Brnsts onlayer overlay:
      zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide Brnsts
    return
label BoostATK:

    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Magnitude=currentcardMAG
    # $ PlayerSts.append("BoostATK")
    $ PlayerSts=statusAppend(PlayerSts,"BoostATK")
    call updatestats_player
    show BoostATKsts onlayer overlay:
      zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide BoostATKsts

    return
label BoostMAGenemy:
    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Magnitude=currentcardMAG
    # $ PlayerSts.append("BoostATK")
    $ PlayerSts=statusAppend(PlayerSts,"BoostMAG")
    call updatestats_enemy
    show BoostMAGsts onlayer overlay:
      zoom 1.3 xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide BoostMAGsts
    return


label BoostATKenemy:
    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Magnitude=currentcardMAG

    # $ EnmySts.append("BoostDEF")
    $ EnmySts=statusAppend(EnmySts,"BoostATK")
    call updatestats_enemy
    show BoostATKsts onlayer overlay:
      zoom 1.3 xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide BoostDEFsts
    return
label BoostDEFenemy:
    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Magnitude=currentcardMAG

    # $ EnmySts.append("BoostDEF")
    $ EnmySts=statusAppend(EnmySts,"BoostDEF")
    call updatestats_enemy
    show BoostDEFsts onlayer overlay:
      zoom 1.3 xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide BoostDEFsts
    return
label updatestats_player:
    python:
        playerATK_m=playerATK
        playerDEF_m=playerDEF
        for fxns in PlayerSts:
                if fxns == 'BoostATK':

                    playerATK_m+=playerATK*0.25
                    playerATK_m = int(playerATK_m)
                    # "This shit happened"
                elif fxns == 'BoostDEF':
                    playerDEF_m+=playerDEF*0.25
                    playerDEF_m = int(playerDEF_m)
                    # "This shit happened"

    return
label updatestats_enemy:
    python:
        enemyATK_m=enemyATK
        enemyDEF_m=enemyDEF
        for fxns in EnmySts:
                if fxns == 'BoostATK':
                    enemyATK_m+=enemyATK*0.25
                    enemyATK_m = int(enemyATK_m)
                    # "This shit happened"
                elif fxns == 'BoostDEF':
                    enemyDEF_m+=enemyDEF*0.25
                    enemyDEF_m = int(enemyDEF_m)
                    # "This shit happened"

    return


image shieldbit = "images/battle/Shield_bit.png"
image shieldlight = "images/battle/Shield_light.png"
label Shieldplayer:
    play sound "sfx/healx.ogg"
    $ Magnitude = (currentcardMAG)
    $ shieldtoplayer=int(playerDEF*Magnitude)
    python:
        playerSP+=shieldtoplayer
        # if playerSP>=playerSPMax:
        #     playerSP=playerSPMax
    #Animation
    show shieldlight:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.0
    show shieldbit onlayer overlay:
        alpha 0.0 xpos 0.5 ypos 0.7 yanchor 0.5 xanchor 0.5
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    show text "{size=70}HP+=[shieldtoplayer]{/size}" onlayer overlay:
        alpha 0.0 zoom 0.0 xpos 0.5 ypos 0.9 yanchor 0.5 xanchor 0.5
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.55
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return
image healbit = "images/battle/Heal_bit.png"
image heallight = "images/battle/Heal_light.png"
label Recoverplayer:
    play sound "sfx/heal.ogg"
    $ Magnitude = (currentcardMAG)
    $ healtoplayer=int(playerHPMax*Magnitude)
    python:
        playerHP+=healtoplayer
        if playerHP>=playerHPMax:
            playerHP=playerHPMax
    #Animation
    show heallight:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.0
    show healbit onlayer overlay:
        alpha 0.0 xpos 0.5 ypos 0.7 yanchor 0.5 xanchor 0.5
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    show text "{size=70}HP+=[healtoplayer]{/size}" onlayer overlay:
        alpha 0.0 zoom 0.0 xpos 0.5 ypos 0.9 yanchor 0.5 xanchor 0.5
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.55
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return

label Shieldenemy:
    play sound "sfx/healx.ogg"
    $ Magnitude = (currentcardMAG)
    $ shieldtoenemy=int(enemyDEF_m*Magnitude)
    python:
        enemySP+=shieldtoenemy
        # if enemySP>=enemySPMax:
        #     enemySP=enemySPMax
    #Animation
    # show shieldlight:
    #     alpha 0.0
    #     ease 0.3 alpha 1.0
    #     ease 0.3 alpha 0.0
    show shieldbit onlayer overlay:
        alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.35
        ease 0.2 alpha 1.0
        pause 0.1
        ease 0.4 alpha 0.0
    show text "{size=40}SP+=[shieldtoenemy]{/size}" onlayer overlay:
        alpha 0.0 zoom 0.0 xalign 0.5 yanchor 0.5 ypos 0.45
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.2
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return

label Damageplayer:
  # if currentcardTYPE == "Sword":
  #   play sound "sfx/slash.wav"
  # elif currentcardTYPE == "Fire":
  #   play sound "sfx/fire.wav"
  # else:
  #   if runnumber>1:
  #     play sound "sfx/sfx_exp_short_hard8.wav"
  #   else:
  #     play sound "sfx/sfx_exp_short_hard9.wav"

  $ Magnitude = (currentcardMAG)
  $ damagetoplayer=int(enemyATK_m*Magnitude)
  if currentcardTYPE == "Sword":
    play sound "sfx/slash.wav" channel 1
  elif currentcardTYPE == "Axe":
    play sound "sfx/slash.wav" channel 1
  elif currentcardTYPE == "Fire":
    play sound "sfx/Bust.wav" channel 1
  elif currentcardTYPE == "Gun":
    play sound "sfx/Bust.wav" channel 1
  if playerSP>0:
    play sound "sfx/noise.wav"
    $ playerSP-=damagetoplayer
    if playerSP<0:
       $ playerHP+=playerSP
       $ playerSP = 0
  else:
    play sound "sfx/damage2.wav"
    $ playerHP-=damagetoplayer
  if playerHP <=0:
    $ playerHP = 0
    $ battle_done=True
  $ dmgdist = ((currentcard.MAG*100)/20)
  $ dmgdist = int(dmgdist*2)

  show playerdmgpoint onlayer overlay
  call hurtnoise
  with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
  $ renpy.pause(0.6,hard=True)
  return
transform ringtransform:
    zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5 rotate 0
    linear 0.15 zoom 1.4 rotate 180 alpha 0.8
transform ringtransform2:
    zoom 0.0 xalign 0.5 ypos 0.3 yanchor 0.5
    linear 0.15 zoom 1.4
screen cardflashscreen:
    # key "mousedown_5" action Return()
    # key "K_PAGEDOWN" action Return()
    add "ring" at ringtransform
    add "cardflash"
    key 'mouseup_1' action Return()
    key 'K_RETURN' action Return()
    key 'K_SPACE' action Return()
    key 'K_KP_ENTER' action Return()
    key 'K_SELECT' action Return()
    key 'z' action Return()
    key 'Z' action Return()
screen cardflashscreenenemy:
    # key "mousedown_5" action Return()
    # key "K_PAGEDOWN" action Return()
    add "ring2" at ringtransform2
    add "cardflashenemy"
    key 'mouseup_1' action Return()
    key 'K_RETURN' action Return()
    key 'K_SPACE' action Return()
    key 'K_KP_ENTER' action Return()
    key 'K_SELECT' action Return()
    key 'z' action Return()
    key 'Z' action Return()



label Execution:
    $ runnumber = 0
    #Index of looper
    $iterations =len(playerbattlecode)
    show screen phasemsg("EXECUTE")
    $renpy.pause(0.5,hard=True)
    hide screen phasemsg

    label exec_loop:
        $ currentcard = playerbattlecode.pop(0)
        # $ currentcard = (playerbattlecode[runnumber])
        $ currentcardFXN = currentcard.FXN
        $ currentcardMAG = currentcard.MAG
        $ currentcardTYPE = currentcard.TYPE
        $ Magnitude = (currentcardMAG)
        $ damagetoenemy=int(playerATK_m*Magnitude)
        $ damagecard = ("Damage" in currentcardFXN[0].name or "Damage" in currentcardFXN[1].name)
        call battlecry
        # show ring onlayer overlay:
        #     zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5 rotate 0
        #     linear 0.15 zoom 1.4 rotate 180 alpha 0.8

        # show cardflash onlayer overlay
        play sound "sound/swing.wav"
        call screen cardflashscreen
        ##
        $fxnindex=0
        label runfunctions:
            $ runfxnstring = currentcardFXN[fxnindex].name
            label hitloop:
                call functioneffects(runfxnstring)
            $fxnindex+=1
            if fxnindex==1:
                jump runfunctions
        hide cardflash
        hide ring
        $runnumber+=1
        if (runnumber<iterations) and (battle_done==False):
            jump exec_loop
        else:
            call PlayerEndPhase
            info"[playerName]'s turn has ended."
            if not battle_done:
                call enemyattack
    return

label PlayerEndPhase:
    if "burn" in EnmySts:
            play sound "sfx/fire.wav"
            python:
              burndmg = 0
              for fxns in EnmySts:
                if fxns=="burn":
                  burndmg = burndmg +80
            show Brnsts:
              zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
              linear 0.1 zoom 0.98
              linear 0.2 zoom 1.0 alpha 0.0
            $ enemyHP = enemyHP-burndmg
            if enemyHP <=0:
                $enemyHP = 0
                $battle_done=True
            # $ EnmySts.remove('burn')
            $ dmgdist = (burndmg/20)
            $ dmgdist = int(dmgdist*2)

            show dmgpointb
            call hurtnoise_Ave
            show Enemy:
              linear 0.1 zoom 0.96
              xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
              pause .05
              xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
              pause .05
              xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
              pause 0.1
              xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
              pause 0.05
              xoffset 0 yoffset 0
              linear 0.1 zoom 1.0
            $ renpy.pause(0.6,hard=True)
            hide Brnsts
    $ playerbits = 8
    return
label EnemyEndPhase:
    if "burn" in PlayerSts:
            python:
              burndmg = 0
              for fxns in PlayerSts:
                if fxns=="burn":
                  burndmg = burndmg +80

            # i"[playerName] receives [burndmg] burn damage!"
            play sound "sfx/fire.wav"
            $ damagetoplayer = burndmg
            $ playerHP = playerHP-burndmg
            if playerHP <=0:
                $ playerHP = 0
                $ battle_done=True
            # $ EnmySts.remove('burn')
            $ dmgdist = (burndmg/20)
            $ dmgdist = int(dmgdist*2)
            $ damagetoplayer = burndmg
            show Brnsts:
              zoom 1.3 xpos 0.5 xanchor 0.5 yanchor 0.5 ypos 0.75 alpha 1.0
              linear 0.1 zoom 0.98
              linear 0.2 zoom 1.0 alpha 0.0

            show playerdmgpoint onlayer overlay
            call hurtnoise
            with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
            $ renpy.pause(0.6,hard=True)


            hide Brnsts
    return
label enemyexecutecard:
    if enemybits>=currentcardCOST:
        # $ enemyrunnumber=enemynumberofattacks
    # else:
        $ enemybits-=currentcardCOST
        # show ring2 onlayer overlay:
        #   zoom 0.0 xalign 0.5 ypos 0.3 yanchor 0.5
        #   linear 0.15 zoom 1.4
        # show cardflashenemy onlayer overlay
        call battlecry_Ave
        play sound "sound/swing.wav"
        call screen cardflashscreenenemy

        $ fxnindex=0
        label runfunctions2:
            $ runfxnstring = currentcardFXN[fxnindex].name

            # $ hitindex=0
            label hitloop2:
                call enemyfunctioneffects(runfxnstring)

            $fxnindex+=1
            if fxnindex==1:
                jump runfunctions2

        hide cardflashenemy
        hide ring2
    return
label enemyattack:
    $ enemyrunnumber = 0
    $ enemynumberofattacks = 5 #renpy.random.randint(1,3)+renpy.random.randint(0,2)
    $ enemybits= 8
    $ enemyhand = [enemyDeck[0],enemyDeck[1],enemyDeck[2],enemyDeck[3],enemyDeck[4]]

    python:
      for enemyhandcards in range(0,5):
        enemyDeck.pop(0)



    #Buffs Priority
    $ enemyhand.sort(key=lambda x: x.FXN[1].name)
    if playerHP<= int(playerHPMax/2) or ("BoostATK" in EnmySts):
      #Damage priority
      $ enemyhand.sort(key=lambda x: x.FXN[0].name)
    elif (enemySP==0) and (enemyHP<=enemyHPMax):
      #Strongest card priority

      $ enemyhand.sort(key=lambda x: x.COST,  reverse = True)
      if "Shield" in enemyhand[0].FXN and "BoostATK" in [handcard.FXN for handcard in enemyhand]:
        $ enemyhand.sort(key=lambda x: x.FXN[1].name)
    python:
      for cardindex in range(0,5):

        enemyDeck.append(enemyhand[cardindex])

    $ choicecount=0
    label enemyattackloop:
        # $ enemycardtoexecute = enemyDeck[0]

        $ currentcard = enemyhand[0]

        # $ enemyhand.append(currentcard)
        # $ currentcard = (playerbattlecode[runnumber])
        $ currentcardFXN = currentcard.FXN
        $ currentcardMAG = currentcard.MAG
        $ currentcardTYPE = currentcard.TYPE
        $ currentcardCOST = currentcard.COST

        # $ enemycannotaffordtoattack = currentcardCOST>enemybits

        # $ goodcardtouse = True

        # $ boostcard = ("Boost" in currentcardFXN[0].name or "Boost" in currentcardFXN[1].name)
        # $ goodcardtouse = boostcard and (enemySP>100) or (not boostcard  and enemySP<=100)
        # $ goodcardused = False
        # $ choicecount = 0
        # $ notprioritycard = not (goodcardtouse)
        # $ nochoice = (choicecount==5)
        # if (goodcardtouse ==True) and (goodcardused==False):
        #   $ goodcardused = True
        #   call enemyexecutecard

        # elif notprioritycard :
        #   $ choicecount+=1
        #   $ enemyrunnumber-=1
        #   $ enemyhand.append(enemyhand[0])
        #   $ enemyhand.pop(0)
        # elif choicecount ==4:
        #   call enemyexecutecard
        # else:
        call enemyexecutecard
        $ enemyhand.pop(0)
        $ enemyrunnumber+=1



        if enemyrunnumber<enemynumberofattacks and (battle_done==False):
            jump enemyattackloop

        else:
            call EnemyEndPhase
            info"[enemyName]'s turn has ended."
    return



label functioneffects(runfxnstring):
    if runfxnstring=="Damage(MAG)":
        call Damageenemy
    elif runfxnstring=="DamageSP(MAG)":
        call DamageSPenemy
    elif runfxnstring=="DamageSPself(MAG)":
        call DamageSPplayer
    elif runfxnstring=="Shield(MAG)":
        call Shieldplayer
    elif runfxnstring=="Recover(MAG)":
        call Recoverplayer
    elif runfxnstring=="Burn()":
        call Burnenemy
    elif runfxnstring=="Burnself()":
        call Burnself
    elif runfxnstring=="BoostATK()":
        call BoostATK
    elif runfxnstring=="BoostDEF()":
        call BoostDEF
    elif runfxnstring=="ReduceBit()":
        call ReduceBit
    return

label enemyfunctioneffects(runfxnstring):
    if runfxnstring=="Damage(MAG)":
        call Damageplayer
    elif runfxnstring=="DamageSP(MAG)":
        call DamageSPplayer
    elif runfxnstring=="DamageSPself(MAG)":
        call DamageSPselfenemy
    elif runfxnstring=="Shield(MAG)":
        call Shieldenemy
    elif runfxnstring=="Recover(MAG)":
        call Recoverenemy
    elif runfxnstring=="Burn()":
        call Burnself
    elif runfxnstring=="Burnself()":
        call Burnenemy
    elif runfxnstring=="BoostATK()":
        call BoostATKenemy
    elif runfxnstring=="BoostDEF()":
        call BoostDEFenemy
    elif runfxnstring=="ReduceBit()":
        call ReduceBitself
    elif runfxnstring=="ReduceBit()":
        call ReduceBitself

    return
