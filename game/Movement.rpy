
init python:
  def placeobject(boxsheet,xpos,ypos,objectnum):
       boxsheet[ypos][xpos]= objectnum
       return boxsheet
  bg = 1
  bgyanchor = 720
  bgxanchor = 1280
  bgypos = 0.5*720
  bgxpos = 0.5*1280
  blockSize = 50
  jumphght = 0
  Running = True
  direction = 'down'


  boxsheet = stagehome
  Where = "Home"
  startplayerpos = [1,1] #(x,y)
  #ILY'S FIRST POSITION

  playerpos = startplayerpos
  playerxpos = playerpos[0]
  playerypos = playerpos[1]

  Here = boxsheet[playerypos][playerxpos]
  Hereisempty = (boxsheet[playerypos][playerxpos]=='0')

  playerxpos = playerpos[0]
  playerypos = playerpos[1]
  objxanchor = ((playerpos[0]+1)*blockSize)-(blockSize/2)
  objyanchor = ((playerpos[1]+1)*blockSize)-(blockSize/2)

  Upisempty = (boxsheet[playerypos-1][playerxpos]=='0')
  Downisempty = (boxsheet[playerypos+1][playerxpos]=='0')
  Leftisempty = (boxsheet[playerypos][playerxpos-1]=='0')
  Rightisempty = (boxsheet[playerypos][playerxpos+1]=='0')

  objectabove = boxsheet[playerypos-1][playerxpos]
  objectbelow = boxsheet[playerypos+1][playerxpos]
  objectleft = boxsheet[playerypos][playerxpos-1]
  objectright = boxsheet[playerypos][playerxpos+1]

  UpisActor = (objectabove!='0') and (direction == 'up')
  DownisActor = (objectbelow!='0') and (direction == 'down')
  LeftisActor = (objectleft!='0') and (direction == 'left')
  RightisActor = (objectright!='0') and (direction == 'right')
  FacingActor = (UpisActor or DownisActor) or (LeftisActor or RightisActor)
label initializemapvariables:
    python:
       gridpos = [192,168]

    return
label checkwalls:
   python:
      playerxpos = playerpos[0]
      playerypos = playerpos[1]
      Hereisempty = (boxsheet[playerypos][playerxpos]=='0')
      Here = boxsheet[playerypos][playerxpos]
      HereisDoor = ((Here=='a') or (Here=='b')) or ((Here=='c') or (Here=='d'))

   python:
      objectabove = boxsheet[playerypos-1][playerxpos]
      objectbelow = boxsheet[playerypos+1][playerxpos]
      objectleft = boxsheet[playerypos][playerxpos-1]
      objectright = boxsheet[playerypos][playerxpos+1]

      Upisempty = (objectabove=='0') or (objectabove=='d') or (objectabove=='c') or (objectabove=='b') or (objectabove=='a')
      Downisempty = (objectbelow=='0') or (objectbelow=='d') or (objectbelow=='c') or (objectbelow=='b') or (objectbelow=='a')
      Leftisempty = (objectleft=='0') or (objectleft=='d') or (objectleft=='c') or (objectleft=='b') or (objectleft=='a')
      Rightisempty = (objectright=='0') or (objectright=='d') or (objectright=='c') or (objectright=='b') or (objectright=='a')


      UpisActor = (objectabove!='0') and (direction == 'up')
      DownisActor = (objectbelow!='0') and (direction == 'down')
      LeftisActor = (objectleft!='0') and (direction == 'left')
      RightisActor = (objectright!='0') and (direction == 'right')
      FacingActor = (UpisActor or DownisActor) or (LeftisActor or RightisActor)

      if direction=='up':
        actornum = objectabove
      elif direction == 'down':
        actornum = objectbelow
      elif direction == 'left':
        actornum = objectleft
      elif direction == 'right':
        actornum = objectright

      # return
   if HereisDoor:
      play sound"sfx/door-fr_0009.wav"
      call doorjump
   return


# label poschange:
#     ""
#     return
label mapcall(position,stage):
    # scene bg
    #position is an (x,y) tuple declaring place in map.
    #stage is declared by stage number: stage = stage1
    #call mapcall((5,5),stage1)
    play music "bgm/ost/Grid_noyemi_K.mp3"
    call addsprites(gridpos)
    python:
        boxsheet = stage
        playerpos = position
        playerxpos = playerpos[0]
        playerypos = playerpos[1]
        objxanchor = ((playerpos[0]+1)*blockSize)-(blockSize/2)
        objyanchor = ((playerpos[1]+1)*blockSize)-(blockSize/2)
        for sprite in spritelist:
            spritename=str(sprite.name)
            boxsheet[sprite.position[1]][sprite.position[0]]=spritename
    $ map_active=True
    label maploop:

      show screen mapB
      call screen mapA
      call Returns

      if map_active==True:
        jump maploop

      else:
        return

label mapresume:

    play music "bgm/ost/Grid_noyemi_K.mp3"
    scene blue
    # $ boxsheet = globals()["GRID"][(gridpos[0],gridpos[1])]
    call addsprites(gridpos)
    show screen mapB
    call screen mapA
    call Returns
    return

label maptransfer(position,stage):
    # scene bg
    #position is an (x,y) tuple declaring place in map.
    #stage is declared by stage number: stage = stage1
    #call mapcall((5,5),stage1)
    call addsprites(gridpos)
    python:
        boxsheet = stage
        playerpos = position
        playerxpos = playerpos[0]
        playerypos = playerpos[1]
        # Here = boxsheet[playerxpos][playerypos]
        objxanchor = ((playerpos[0]+1)*blockSize)-(blockSize/2)
        objyanchor = ((playerpos[1]+1)*blockSize)-(blockSize/2)
        for sprite in spritelist:
            spritename=str(sprite.name)
            boxsheet[sprite.position[1]][sprite.position[0]]=spritename
    call checkwalls

    return
image shock:
    "images/rpg/overworld/shock1.png"
    pause .05
    "images/rpg/overworld/shock12.png"
    pause .05
    "images/rpg/overworld/shock2.png"
    pause .05
    "images/rpg/overworld/shock22.png"
    pause .05
    "images/rpg/overworld/shock3.png"
    pause .05
    "images/rpg/overworld/shock32.png"
    pause .05
    choice:
      xzoom -1.0
    choice:
      yzoom -1.0
    choice:
      xzoom 1.0
    choice:
      yzoom 1.0
    repeat


screen mapB:
    vbox:
      at mover(objxanchor,objyanchor)
      for i in boxsheet:
         hbox:
           xalign 0.5 yalign 1.0
           for j in i:
             if j !='n':
               image "images/rpg/tile/Tilebg.png"

             elif j == 'n':
               null height blockSize width blockSize
    vbox:
      at mover(objxanchor,objyanchor)
      for i in boxsheet:
         hbox:
           xalign 0.5 yalign 1.0
           for j in i:
             if j =='1':
               image "images/rpg/overworld/object.png"
             elif j =='2':
               image "shock"
             elif j =='3':
               image "images/rpg/overworld/object3.png"
             elif j =='4':
               image "images/rpg/overworld/object4.png"
             elif j =='5':
               image "images/rpg/overworld/object5.png"
             elif j =='a':
               image "images/rpg/overworld/objectd.png"
             elif j =='b':
               image "images/rpg/overworld/objectd.png"
             elif j =='c':
               image "images/rpg/overworld/objectd.png"
             elif j =='d':
               image "images/rpg/overworld/objectd.png"
             elif j=='0':
               null height blockSize width blockSize
             elif j == 'n':
               null height blockSize width blockSize
             elif len(j)>1:
               null height blockSize width blockSize
##NPC SPRITES


    ##PLAYER CHARACTER
    frame:
      xpadding 15
      ypadding 15
      vbox:

        yalign 0.1 xalign 0.1
        null width 260
        text "GRID ([gridpos[0]],[gridpos[1]])" xalign 0.5 yalign 0.05
        text "{color=#fff}Position: [playerxpos],[playerypos]{/color}"
        text "{color=#fff}Running = [Running]{/color}"
        # text "{color=#fff}Here = [Here]{/color}"
        text "{color=#fff}Where = [Where]{/color}"
        frame:
            style_prefix "healthbar"
            xsize bar_size(playerHP,playerHPMax,200)
            # xsize
        null height 7
        text "HP: [playerHP]/[playerHPMax]"
        null height 10
    if len(objectbelow)>1:
      use playersprite(playerypos)
      for sprites in spritelist:
          use npcsprite(sprites)
    else:
      for sprites in spritelist:
        use npcsprite(sprites)
      use playersprite(playerypos)



    # zorder yvalue
screen npcsprite(sprites):
    zorder sprites.position[1]

    image "images/rpg/overworld/[sprites.name][sprites.direction].png" xpos 0.5 ypos 0.508 at mover2((objxanchor-(sprites.position[0])*50),objyanchor-(sprites.position[1])*50), halftrans# zorder maplayering(sprites.position[1])

screen playersprite(yvalue):
    zorder yvalue
    imagebutton idle "images/Characters/ILY/ILY[direction].png" action Return("jump") xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.9 at playerjump(jumphght), blockSizetrans(blockSize) #zorder maplayering(playerypos)


transform blockSizetrans(blockSize):
  zoom blockSize*.01 transform_anchor True
transform halftrans:
  zoom 0.5

transform zoombig:
    xalign 0.5 yalign 1.0
# init python:
#     btnhovered = 1.0
#     profilearray = []
transform transp:
        alpha 0.6
transform rpgsize:
        zoom 0.35 alpha 1.0


# transform maptrans:
#   on show:
#    zoom 1.0
#    xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
#   rotate 90
#   linear 0.1 xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5

transform mover(objxanchor,objyanchor):
  xpos 0.5 ypos 0.5
  linear 0.05 xanchor objxanchor yanchor objyanchor  transform_anchor True
transform mover2(objxanchor,objyanchor):
  # xpos 1.0 ypos 1.0
  linear 0.05 xanchor objxanchor yanchor objyanchor+(25)  transform_anchor True
# transform maplayering(yvalue):
#   zorder yvalue
transform playerjump(jumphght):
  xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.7
  linear 0.05 yoffset - jumphght
  linear 0.05 yoffset 0
  pause .1
  repeat
screen mapA:
    key 'K_UP'          action SetVariable("direction","up"),     Return("up")
    key 'K_DOWN'        action SetVariable("direction","down"),   Return("down")
    key 'K_LEFT'        action SetVariable("direction","left"),   Return("left")
    key 'K_RIGHT'       action SetVariable("direction","right"),  Return("right")

    if anim_done:
      key 'repeat_K_UP'     action SetVariable("direction","up"),     Return("up")
      key 'repeat_K_DOWN'   action SetVariable("direction","down"),   Return("down")
      key 'repeat_K_RIGHT'  action SetVariable("direction","right"),  Return("right")
      key 'repeat_K_LEFT'   action SetVariable("direction","left"),   Return("left")
    # key 'K_ESCAPE'      action Return("End")
    key 'A'         action Return("Pause")
    key 'a'         action Return("Pause")
    key 'z'             action Return("OK")
    key 'Z'             action Return("OK")
    key 'x'             action Return("MapTalk")
    key 'X'             action Return("MapTalk")
    # key 'x'             action ShowMenu("partylist")
    key 'r'             action Return("running")
    key 'R'             action Return("running")

    key 'K_SPACE'       action Return("jump")
    key 'repeat_K_SPACE'action Return("jump")
    key 'E'             action Return("End")
    key 'e'             action Return("End")

transform floatmov:
    linear 0.5 yoffset -2
    linear 0.5 yoffset 2
    repeat
transform ilymov2:
    linear 1.0 yoffset -10

    linear 1.0 yoffset 10
    repeat

label randomencounter:
     $ randomenemy = renpy.random.randint(0,100)
     # $ safezone=(Where=="Home")
     $safezone=True #for debugging
     if ((randomenemy >99) and (safezone==False)) and not HereisDoor:
       $ enemy_encounter = True
     if enemy_encounter == True:
          $ enemyvirus = renpy.random.choice([Keylogger,Ransomware,Rootkit,Worm])
          hide screen mapB
          hide screen mapA
          call battlev3(ILY,enemyvirus)
          if playerHP<=0:
              return
          $ enemy_encounter=False
          $ map_active=True
          call mapresume
          return

     return
label Returns:
#   if not running:
  if _return=="card1":

      play sound "sound/Phase.wav" channel 2
      $ card1clicked = True

      $ playerbits-=playercard1COST
      $ playerbattlecode.append(playercard1obj)
  elif _return=="card2":
      play sound "sound/Phase.wav" channel 2
      $ card2clicked = True
      $ playerbits-=playercard2COST
      $ playerbattlecode.append(playercard2obj)
  elif _return=="card3":
      play sound "sound/Phase.wav" channel 2
      $ card3clicked = True
      $ playerbits-=playercard3COST
      $ playerbattlecode.append(playercard3obj)
  elif _return=="card4":
      play sound "sound/Phase.wav" channel 2
      $ card4clicked = True
      $ playerbits-=playercard4COST
      $ playerbattlecode.append(playercard4obj)
  elif _return=="card5":
      play sound "sound/Phase.wav" channel 2
      $ card5clicked = True
      $ playerbits-=playercard5COST
      $ playerbattlecode.append(playercard5obj)
  elif _return=="Return_card":
      if playerbattlecode != []:
        $ playerbattlecode.pop(-1)
  elif _return=="Execute":
      call Execution

  if map_active:
   if (_return=="running"):
    if not Running:
     $ Running = True
    elif Running:
     $ Running = False
   if (pdirection ==_return) or Running:
    #if Hereisempty:

      $ playerxpos = playerpos[0]
      $ playerypos = playerpos[1]
      $ anim_done = False

      if Upisempty:
       if (_return=="up"):
        $ objyanchor = objyanchor-blockSize
        $ playerpos = [playerxpos,playerypos-1]
      else:
        if _return=="up":
            play sound "sfx/bumpintowall_X5CNQPB.mp3"
      if Downisempty:
       if (_return=="down"):
        $ objyanchor = objyanchor+blockSize
        $ playerpos = [playerxpos,playerypos+1]
      else:
        if _return=="down":
            play sound "sfx/bumpintowall_X5CNQPB.mp3"
      if Leftisempty:
       if (_return=="left"):
        $ objxanchor = objxanchor-blockSize
        $ playerpos = [playerxpos-1,playerypos]
      else:
        if _return=="left":
            play sound "sfx/bumpintowall_X5CNQPB.mp3"
      if Rightisempty:
       if (_return=="right"):
        $ objxanchor = objxanchor+blockSize
        $ playerpos = [playerxpos+1,playerypos]
      else:
        if _return=="right":
          play sound "sfx/bumpintowall_X5CNQPB.mp3"
      pause 0.02
      $ anim_done = True
      #call wildenemy

   if (_return=="zoomin"):
     $ blockSize = blockSize + 10
     hide screen mapA
   if (_return=="zoomout"):
     $ blockSize = blockSize - 10
     hide screen mapA
   if (_return=="jump"):
        $ jumphght=blockSize*1.0
        pause 0.1
        $ jumphght=0

   if FacingActor:
     if (_return=="OK"):
       call whatactor
       return
   if (_return=="MapTalk"):
       call MapTalk
       return
   if (_return=="Pause"):
       # "Pause"
       call pauseshow
       return
   elif (_return=="End"):
        $map_active=False
        return
   else:
       $ pdirection = direction
   call checkwalls
       # $safezone=True
   call randomencounter
   if (playerHP<=0) or (map_active==False):
      return
   call screen mapA
   call Returns
   return
  return
  # elif (_return=="card1"):
  #       call makestats(0)
  #       if PlayerSpd >=EnmySpd:
  #         $ PlayerAttacked2nd = False
  #         play sound "sfx/swing.wav"
  #         show ring onlayer overlay:
  #           zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5
  #           linear 0.2 zoom 1.6
  #         show card1 onlayer overlay:
  #           xalign 0.5 ypos 0.7 yanchor 0.5
  #           zoom 1.0
  #           linear 0.1 zoom 1.5
  #           linear 0.2 zoom 1.4
  #         # pause 0.4
  #         $ renpy.pause(0.4,hard=True)
  #         call Damage#DAMAGE OPPONENT
  #         if not Battle_End:
  #             $ renpy.pause(0.1,hard=True)
  #             call EnemyAttack
  #       elif PlayerSpd<EnmySpd:
  #         $ PlayerAttacked2nd = True
  #         call EnemyAttack
  #         # pause 0.4
  #         # hide card1
  #         if not Battle_End:
  #             $ renpy.pause(0.1,hard=True)
  #             call battlecry
  #             play sound "sfx/swing.wav"
  #             show ring onlayer overlay:
  #               zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5
  #               linear 0.2 zoom 1.6
  #             show card1 onlayer overlay:
  #               xalign 0.5 ypos 0.7 yanchor 0.5
  #               zoom 1.0
  #               linear 0.1 zoom 1.5
  #               linear 0.2 zoom 1.4
  #             # pause 0.4
  #             $ renpy.pause(0.4,hard=True)
  #             call Damage #DAMAGE OPPONENT
  #       return
  # elif (_return=="card2"):
  #       call makestats(1)
  #       if PlayerSpd >=EnmySpd:
  #         $ PlayerAttacked2nd = False
  #         play sound "sfx/swing.wav"
  #         show ring onlayer overlay:
  #           zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5
  #           linear 0.2 zoom 1.6
  #         show card2 onlayer overlay:
  #           xalign 0.5 ypos 0.7 yanchor 0.5
  #           zoom 1.0
  #           linear 0.1 zoom 1.5
  #           linear 0.2 zoom 1.4
  #         # pause 0.4
  #         $ renpy.pause(0.4,hard=True)
  #         hide ring
  #         hide card1
  #         call Damage#DAMAGE OPPONENT
  #         if not Battle_End:
  #             $ renpy.pause(0.1,hard=True)
  #             call EnemyAttack
  #       elif PlayerSpd<EnmySpd:
  #         $ PlayerAttacked2nd = True
  #         call EnemyAttack
  #         if not Battle_End:
  #             $ renpy.pause(0.1,hard=True)
  #             call battlecry
  #             play sound "sfx/swing.wav"
  #             show ring onlayer overlay:
  #               zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5
  #               linear 0.2 zoom 1.6
  #             show card2 onlayer overlay:
  #               xalign 0.5 ypos 0.7 yanchor 0.5
  #               zoom 1.0
  #               linear 0.1 zoom 1.5
  #               linear 0.2 zoom 1.4
  #             # pause 0.4
  #             $ renpy.pause(0.4,hard=True)
  #             call Damage #DAMAGE OPPONENT
  #             hide ring
  #             hide card2
  #       return
  # elif (_return=="card3"):
  #       call makestats(2)
  #       if PlayerSpd >=EnmySpd:
  #         $ PlayerAttacked2nd = False
  #         call battlecry
  #         play sound "sfx/swing.wav"

  #         show ring onlayer overlay:
  #           zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5
  #           linear 0.2 zoom 1.6
  #         show card3 onlayer overlay:
  #           xalign 0.5 ypos 0.7 yanchor 0.5
  #           zoom 1.0
  #           linear 0.1 zoom 1.5
  #           linear 0.2 zoom 1.4
  #         # pause 0.4
  #         $ renpy.pause(0.4,hard=True)

  #         call Damage #DAMAGE OPPONENT
  #         if not Battle_End:
  #             $ renpy.pause(0.1,hard=True)
  #             call EnemyAttack

  #       elif PlayerSpd<EnmySpd:
  #         $ PlayerAttacked2nd = True
  #         call EnemyAttack
  #         if not Battle_End:
  #             $ renpy.pause(0.1,hard=True)
  #             call battlecry
  #             play sound "sfx/swing.wav"
  #             show ring onlayer overlay:
  #               zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5
  #               linear 0.2 zoom 1.6

  #             show card3 onlayer overlay:
  #               xalign 0.5 ypos 0.7 yanchor 0.5
  #               zoom 1.0
  #               linear 0.1 zoom 1.5
  #               linear 0.2 zoom 1.4
  #             # pause 0.4
  #             $ renpy.pause(0.4,hard=True)
  #             call Damage #DAMAGE OPPONENT

  #       return
  # elif (_return=="card4"):
  #       call makestats(3)

  #       if PlayerSpd >=EnmySpd:
  #         $ PlayerAttacked2nd = False
  #         call battlecry
  #         play sound "sfx/swing.wav"

  #         show ring onlayer overlay:
  #           zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5
  #           linear 0.2 zoom 1.6
  #         show card4 onlayer overlay:
  #           xalign 0.5 ypos 0.7 yanchor 0.5
  #           zoom 1.0
  #           linear 0.1 zoom 1.5
  #           linear 0.2 zoom 1.4
  #         # pause 0.4
  #         $ renpy.pause(0.4,hard=True)

  #         call Damage #DAMAGE OPPONENT
  #         if not Battle_End:
  #             $ renpy.pause(0.1,hard=True)
  #             call EnemyAttack

  #       elif PlayerSpd<EnmySpd:
  #         $ PlayerAttacked2nd = True
  #         call EnemyAttack
  #         if not Battle_End:
  #             $ renpy.pause(0.1,hard=True)
  #             call battlecry
  #             play sound "sfx/swing.wav"
  #             show ring onlayer overlay:
  #               zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5
  #               linear 0.2 zoom 1.6

  #             show card4 onlayer overlay:
  #               xalign 0.5 ypos 0.7 yanchor 0.5
  #               zoom 1.0
  #               linear 0.1 zoom 1.5
  #               linear 0.2 zoom 1.4
  #             # pause 0.4
  #             $ renpy.pause(0.4,hard=True)
  #             call Damage #DAMAGE OPPONENT

  #       return
  # elif (_return=="Concatenate"):
  #       call screen Concatenate
  #       return
# label makestats(cardchosen):
#   hide screen choosecard
#   $ Playercardname = myhand[cardchosen].name
#   $ PlayerDmg = myhand[cardchosen].POW
#   $ PlayerSpd = myhand[cardchosen].SPD
#   $ PlayerFxn = myhand[cardchosen].fxn
#   $ PlayerRank = myhand[cardchosen].rank
#   $ enmychoice=renpy.random.randint(0, (len(Enmyhand)-1))
#   $ Enmycardname = Enmyhand[enmychoice].name
#   $ EnmyDmg = Enmyhand[enmychoice].POW
#   $ EnmySpd = Enmyhand[enmychoice].SPD
#   $ EnmyFxn = Enmyhand[enmychoice].fxn
#   $ EnmyRank = Enmyhand[enmychoice].rank

#   if "SPD_Up" in PlayerSts:
#     python:
#       # for fxns in PlayerSts:
#       #   if fxns=="Buffed":
#       #     PlayerDmg = PlayerDmg+int(PlayerDmg*0.1)
#       PlayerSpd = int(PlayerSpd*1.5)
#       PlayerSts.remove('SPD_Up')
#     if not ("SPD_Up" in PlayerSts):
#       hide Blueframe

#   return
# label EnemyAttack:
# ## Enemy's Attack. Checks for Status problems
#       if "Frozen" in EnmySts:
#         play sound "sfx/frz.wav"
#         show Frzsts:
#           zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
#           linear 0.1 zoom 0.98
#           linear 0.2 zoom 1.0 alpha 0.0
#         $ renpy.pause(0.4,hard=True)
#         hide Frzsts
#         "Enemy is Frozen and cannot attack!!"
#         $ EnmySts.remove('Frozen')
#       elif "Broken" in EnmySts:
#         play sound "sfx/frz.wav"
#         show Brksts:
#           zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
#           linear 0.1 zoom 0.98
#           linear 0.2 zoom 1.0 alpha 0.0
#         $ renpy.pause(0.4,hard=True)
#         hide Brksts
#         "Enemy cannot attack with Broken Battleware!!"
#         $ EnmySts.remove('Broken')

#       else:
#         play sound "sfx/swing.wav"
#         show ring2 onlayer overlay:
#           zoom 0.0 xalign 0.5 ypos 0.3 yanchor 0.5
#           linear 0.2 zoom 1.6
#         if enmychoice ==0:
#           show Enmycard1 onlayer overlay:
#             xalign 0.5 ypos 0.3 yanchor 0.5
#             zoom 1.0
#             linear 0.1 zoom 1.5
#             linear 0.2 zoom 1.4
#         elif enmychoice ==1:
#           show Enmycard2 onlayer overlay:
#             xalign 0.5 ypos 0.3 yanchor 0.5
#             zoom 1.0
#             linear 0.1 zoom 1.5
#             linear 0.2 zoom 1.4
#         elif enmychoice ==2:
#           show Enmycard3 onlayer overlay:
#             xalign 0.5 ypos 0.3 yanchor 0.5
#             zoom 1.0
#             linear 0.1 zoom 1.5
#             linear 0.2 zoom 1.4
#         elif enmychoice ==3:
#           show Enmycard4 onlayer overlay:
#             xalign 0.5 ypos 0.3 yanchor 0.5
#             zoom 1.0
#             linear 0.1 zoom 1.5
#             linear 0.2 zoom 1.4
#         # pause 0.4
#         $ renpy.pause(0.4,hard=True)
#         call EnmyDamage #DAMAGE PLAYER
#       return
label Damage:
        # DAMAGING ENEMY USING OWN CARD

        hide ring
        hide card1
        hide card2
        hide card3
        hide card4
        #Calculate dmg here
        call fxnCaller(PlayerFxn)
        if EnmyHP <=0:
          $EnemyHP=0
          show Enemy:
            linear 0.15 zoom 0.94
            xoffset 0.12 yoffset 0.2 alpha 0.5
            pause .05
            xoffset 0.-17 yoffset 0.-17 alpha 0.8
            pause .05
            xoffset 0.13 yoffset 0.2 alpha 1.0
            pause 0.1
            xoffset 0.-19 yoffset 0.11
            pause 0.4
            linear 0.1 zoom 0.8 alpha 0.0
          $ renpy.pause(0.4,hard=True)
          $Battle_End = True
          hide Enemy
          hide screen stats
          hide screen choosecard
          stop music

          # jump cardcycle
        return


label EnmyDamage:
        #ILY LOSING HP
        #Calculate dmg here
        call fxnCallerp(EnmyFxn)
        if playerHP <=0:
          $playerHP=0
          #Losing Animation
          "ILY Deleted!"
          $Battle_End = True
          hide Enemy
          hide screen stats
          hide screen choosecard
          stop music

          # jump cardcycle
        return

screen finishingflash(say):
    image "black" at pausedim
    add "flashline" at flashtrans

    text "{size=25}[say]{/size}" xalign 0.5 yalign 0.80

    add "diamondblue" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.3 ypos 0.25
    add "diamondblue2" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.7 ypos 0.75
    add "diamondred" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.8 ypos 0.2
    add "diamondred2" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.2 ypos 0.8
    add "diamondwhite" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.1 ypos 0.9
    add "diamondwhite2" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.9 ypos 0.1
    # if anim_done:
    key 'mouseup_1' action Return()
    key 'K_RETURN' action Return()
    key 'K_SPACE' action Return()
    key 'K_KP_ENTER' action Return()
    key 'K_SELECT' action Return()
    key 'z' action Return()
    key 'Z' action Return()
    key 'x' action Return()
    key 'X' action Return()
transform flashtrans:
    alpha 0.0
    pause 0.35
    xpos 0.0 xanchor 1.0 yalign 0.5 alpha 1.0
    linear 0.1 xalign 0.5
    pause 0.1
    linear 0.1 yzoom 1.1
    linear 0.08 yzoom 1.0
image flashline:
    "images/battle/flashpanel/bar.png"
    pause 0.8
    "images/battle/flashpanel/frame.png"
    yzoom 0.5
    pause 0.1
    "images/battle/flashpanel/frame.png"
    yzoom 1.1
    pause 0.1
    "images/battle/flashpanel/[flashuser].png"
    yzoom 1.0
image diamondblue:
    "images/battle/flashpanel/diamondblue.png"
    zoom 0.5
image diamondblue2:
    "diamondblue"
    zoom 0.8
image diamondred:
    "images/battle/flashpanel/diamondred.png"
    zoom 0.7
image diamondred2:
    "diamondred"
    zoom 0.9
image diamondwhite2:
    "images/battle/flashpanel/diamondwhite.png"
    zoom 0.7
image diamondwhite2:
    "diamondwhite"
    zoom 0.9

transform diamondtrans:

    alpha 0.0
    pause 0.8
    block:
        alpha 1.0
        xoffset 10 yoffset -16
        pause 0.08
        xoffset 0 yoffset 20
        pause 0.08
        xoffset -10 yoffset -17
        pause 0.08
        repeat
label battlecry_Ave:
    if enemyName=="Ave":
      python:
        burndmg = 0
        for fxns in PlayerSts:
          if fxns=="burn":
            burndmg = burndmg +40
      $ playerburndamage = burndmg
      $ damagecard = (currentcardFXN[0].name =="Damage(MAG)" or currentcardFXN[1].name=="Damage(MAG)")
      $ Magnitude = (currentcardMAG)
      $ enemydamagetoplayer=int(enemyATK_m*Magnitude)+playerburndamage
      if (enemydamagetoplayer>=(playerHP+playerSP)) and (damagecard==True):

        $flashuser="Ave"
        voice "voice/Ave_voice/No, I won't lose!.ogg"
        $ anim_done=False
        pause 0.1
        call screen finishingflash("No, I won't lose, It's over ILY!")

      elif (enemyHP <=2800):# and 'POW_Up' not in PlayerFxn:
        $ avcount=avcount+1
        if avcount == 1:
          voice "voice/Ave_voice/Heeaah.ogg"
          a"Heeaah!"
        elif avcount == 2:
          voice "voice/Ave_voice/Hhaagh.ogg"
          a"Hhagh!!"
        elif avcount == 3:
          voice "voice/Ave_voice/Hrrah!.ogg"
          a"Hrrah!"
        elif avcount == 4:
          voice "voice/Ave_voice/Hah!.ogg"
          a"Hah!"
        elif avcount >= 5:
          voice "voice/Ave_voice/It's Over, ILY!.ogg"
          a"It's over, ILY!"
          $avcount=1
    return
label battlecry:
    python:
      burndmg = 0
      for fxns in EnmySts:
        if fxns=="burn":
          burndmg = burndmg +40
    $ damagetoenemy += burndmg
    if ((enemyHP+enemySP)<=damagetoenemy) and (damagecard==True):
    # or EnemyHP<=(damagetoenemy+burndmg) and 'Recover' not in PlayerFxn) and 'POW_Up' not in PlayerFxn:
      voice "voice/ILY24B - Break down & disappear!.mp3"
      $ anim_done=False
      $ flashuser = "ILY"
      call screen finishingflash("Break down and disappear!")

    elif (playerHP <=1500):# and 'POW_Up' not in PlayerFxn:
      $ vcount=vcount+1
      if vcount == 1:
        voice "voice/ILY26 - I won't let you.mp3"
        i"I won't let you!"
      elif vcount == 2:
        voice "voice/ILY08 - This attack, receive it!.mp3"
        i"This attack, receive it!"
      elif vcount == 3:
        voice "voice/ILY05D - Swing heavy sword sounds.mp3"
        i"Hnnngg--Yah!"
      elif vcount == 4:
        voice "voice/ILY05C - Swing medium sword sounds.mp3"
        i"Hnnngg--Hah!"
      elif vcount >= 5:
        voice "voice/ILY05 - Swing light sword sounds.mp3"
        i"Nnnhhhh!"
        $vcount=0
    return
label hurtnoise_Ave:
    if enemyName=="Ave":
      $ ahcount=ahcount+1
      if ahcount ==1:
        play sound "voice/Ave_voice/hurt/Eugh!.ogg" channel "voice"
      elif ahcount == 2:
        play sound "voice/Ave_voice/hurt/Euh!.ogg" channel "voice"
        $ ahcount=0
    return
label hurtnoise:
    $ hcount=hcount+1
    if hcount ==1:
      play sound "voice/hurt/ILY13D - Light Bullet Grazed, punched or hit.wav" channel "voice"
    elif hcount == 2:
      play sound "voice/hurt/ILY13B - Light Bullet Grazed, punched or hit.wav" channel "voice"
    elif hcount == 3:
      play sound "voice/hurt/ILY13C - Light Bullet Grazed, punched or hit.wav" channel "voice"
    elif hcount == 4:
      play sound "voice/hurt/ILY05B - Swing light sword sounds.wav" channel "voice"
    elif hcount == 5:
      play sound "voice/hurt/ILY12J - Bullet Grazed, punched or hit.wav" channel "voice"
      $ hcount=0
    return
screen notif(notiftext):
    frame:
      null height 100 width 1280
      text "[notiftext]" at notifanim
      null height 100 width 1280

transform notifanim:
  on show:
    yzoom 0.0
    linear 0.2 yzoom 1.0

image ILY_byTorakun14:
  "images/characters/ILY/ILY nobg_by_Torakun.png"
  zoom 0.3

label win:
    #MAKE VICTORY ANIMATION
    # show ILY_byTorakun14:
    #   xalign 0.0
    show screen phasemsg("VICTORY!")
    "ILY Wins!"
    hide screen phasemsg
    # "VICTORY!"
    #BATTLE DROPS
    return
label lose:
    $ okdesktop = False
    hide screen mapA
    hide screen mapB
    scene ILYgameover with pixellate
    "I'm.. Sorry, John. "
    extend"I'm sorry Lisa."

return


##Card Functions: FXN = Card effect
label fxnCallerp(fxn):
  #Enemy-to-Player Damage Calculation, based on Fxn.
  if "Damage" in fxn:
    call hurtnoise
    with Shake((0, 0, 0, 0), 0.5, dist=EnmyDmg/10)
    $ playerHP = playerHP-EnmyDmg
  if "Burn" in fxn:
    play sound "sfx/fire.wav"
    $ PlayerSts.append("Burned")
    $ PlayerSts.append("Burned")
    $ PlayerSts.append("Burned")
    $ PlayerSts.append("Burned")
    show Brnsts onlayer overlay:
      zoom 1.3 xanchor 0.5 xpos 0.15 yanchor 0.5 ypos 0.1 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.5,hard=True)
    hide Brnsts
  if "Burned" in PlayerSts:
        play sound "sfx/fire.wav"
        python:
          burndmg = 0
          for fxns in PlayerSts:
            if fxns=="Burned":
              burndmg = burndmg +10
        show Brnsts onlayer overlay:
          zoom 1.3 xanchor 0.5 xpos 0.15 yanchor 0.5 ypos 0.1 alpha 1.0
          linear 0.1 zoom 0.98
          linear 0.2 zoom 1.0 alpha 0.0

        $ playerHP = playerHP-burndmg

        $ playerSts.remove('Burned')
        play sound "sfx/fire.wav"
        with Shake((0, 0, 0, 0), 0.5, dist=burndmg/10)
        hide Brnsts
  return


# label fxnCaller(fxn):

#   if "POW_Up" in PlayerSts:
#     python:
#       # for fxns in PlayerSts:
#       #   if fxns=="POW_Up":
#       #     PlayerDmg = PlayerDmg+Powboost
#       PlayerDmg = int(PlayerDmg*1.5)
#       PlayerSts.remove('POW_Up')

#     if not ("POW_Up" in PlayerSts):
#       hide Redframe
#   if ("Saber_Up" in PlayerSts) :
#     python:
#       if ("Saber" in Playercardname):
#         Saberboost = int(PlayerDmg*0.10)
#         for fxns in PlayerSts:

#           if fxns=="Saber_Up" :
#             PlayerDmg = PlayerDmg+Saberboost
#       PlayerSts.remove('Saber_Up')
#     # if not ("POW_Up" in PlayerSts):
#     #   hide Redframe
#   if "Damage" in fxn:
#     $ EnmyHP = EnmyHP-PlayerDmg
#     if "Bomb" in Playercardname:
#       play sound "sfx/sfx_exp_medium8.wav"
#     elif (("Buster" in Playercardname) or ("Flame" in Playercardname)) or ("Shot" in Playercardname):
#       $ blastsound = renpy.random.randint(0,1)
#       if blastsound ==0:
#         play sound "sfx/sfx_exp_short_hard8.wav"
#       elif blastsound ==1:
#         play sound "sfx/sfx_exp_short_hard9.wav"
#     else:
#       play sound "sfx/slash.wav"

#     $ dmgdist = (PlayerDmg/20)
#     $ dmgdist = int(dmgdist)
#     show dmgpoint
#     show Enemy:
#       linear 0.15 zoom 0.96
#       xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#       pause .05
#       xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#       pause .05
#       xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#       pause 0.1
#       xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#       pause 0.05
#       xoffset 0 yoffset 0
#       linear 0.1 zoom 1.0
#     $ renpy.pause(0.45,hard=True)
#   if "POW_Up" in fxn:
#     # $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/sfx_sounds_powerup16.wav"
#     show Redframe:
#       linear 0.7 alpha 1.0
#       linear 0.7 alpha 0.01
#       repeat
#     with Shake((0, 0, 0, 0), 0.5, dist=10)
#     # $ EnmyHP = EnmyHP-PlayerDmg
#     $ PlayerSts.append("POW_Up")
#     $ PlayerSts.append("POW_Up")
#     $ PlayerSts.append("POW_Up")
#     $ renpy.pause(0.4,hard=True)
#   if "Saber_Up" in fxn:
#     # $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/Saber-up.wav"
#     show Saber_Upsts onlayer overlay:
#           zoom 0.8 xanchor 0.5 xpos 0.15 yanchor 0.5 ypos 0.19 alpha 1.0
#           linear 0.35 zoom 0.7 alpha 1.0
#           linear 0.15 zoom 0.6 alpha 0.0
#     # $ EnmyHP = EnmyHP-PlayerDmg
#     $ PlayerSts.append("Saber_Up")
#     $ PlayerSts.append("Saber_Up")
#     $ PlayerSts.append("Saber_Up")
#     $ renpy.pause(0.6,hard=True)
#     hide Saber_Upsts
#   if "SPD_Up" in fxn:
#     # $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/sfx_sounds_powerup16.wav"
#     show Blueframe:
#       linear 0.7 alpha 1.0
#       linear 0.7 alpha 0.01
#       repeat
#     with Shake((0, 0, 0, 0), 0.5, dist=10)
#     # $ EnmyHP = EnmyHP-PlayerDmg
#     $ PlayerSts.append("SPD_Up")
#     $ PlayerSts.append("SPD_Up")
#     $ PlayerSts.append("SPD_Up")
#     $ renpy.pause(0.4,hard=True)
#   if "Recover" in fxn:
#     play sound "sfx/heal.ogg"
#     show white:
#       alpha 0.0
#       linear 0.1 alpha 1.0
#       linear 0.1 alpha 0.0
#     $ PlayerHP = PlayerHP + PlayerDmg
#     if PlayerHP >PlayerHPmax:
#       $PlayerHP=PlayerHPmax

#     $ renpy.pause(0.4,hard=True)

#   elif "DoubleHit" in fxn:
#     $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/slash.wav"
#     $ dmgdist = (PlayerDmg/20)
#     $ dmgdist = int(dmgdist)
#     show dmgpoint
#     show Enemy:
#       linear 0.025 zoom 0.88
#       xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#       pause .025
#       xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#       pause .025
#       xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#       pause 0.025
#       xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#       pause 0.025
#       xoffset 0 yoffset 0
#       linear 0.025 zoom 1.0
#     $ renpy.pause(0.15,hard=True)
#     $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/slash.wav"
#     $ dmgdist = (PlayerDmg/20)
#     $ dmgdist = int(dmgdist*4)
#     show dmgpoint
#     show Enemy:
#       linear 0.025 zoom 0.80
#       xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#       pause .025
#       xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#       pause .025
#       xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#       pause 0.025
#       xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#       pause 0.025
#       xoffset 0 yoffset 0
#       linear 0.005 zoom 1.1
#       linear 0.020 zoom 1.0
#     $ renpy.pause(0.4,hard=True)

#   elif "TripleHit" in fxn:
#     $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/sfx_exp_short_hard9.wav"
#     $ dmgdist = (PlayerDmg/20)
#     $ dmgdist = int(dmgdist)
#     show dmgpoint
#     show Enemy:
#       linear 0.025 zoom 0.88
#       xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#       pause .025
#       xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#       pause .025
#       xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#       pause 0.025
#       xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#       pause 0.025
#       xoffset 0 yoffset 0
#       linear 0.025 zoom 1.0
#     $ renpy.pause(0.15,hard=True)
#     $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/sfx_exp_short_hard9.wav"
#     $ dmgdist = (PlayerDmg/20)
#     $ dmgdist = int(dmgdist)
#     show dmgpoint
#     show Enemy:
#       linear 0.025 zoom 0.88
#       xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#       pause .025
#       xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#       pause .025
#       xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#       pause 0.025
#       xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#       pause 0.025
#       xoffset 0 yoffset 0
#       linear 0.025 zoom 1.0
#     $ renpy.pause(0.15,hard=True)
#     $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/sfx_exp_short_hard8.wav"
#     $ dmgdist = (PlayerDmg/20)
#     $ dmgdist = int(dmgdist*4)
#     show dmgpoint
#     show Enemy:
#       linear 0.025 zoom 0.80
#       xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#       pause .025
#       xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#       pause .025
#       xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#       pause 0.025
#       xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#       pause 0.025
#       xoffset 0 yoffset 0
#       linear 0.005 zoom 1.1
#       linear 0.020 zoom 1.0
#     $ renpy.pause(0.4,hard=True)

#   elif "Break" in fxn:
#     #BREAK CARD
#     $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/slash.wav"
#     $ dmgdist = (PlayerDmg/20)
#     $ dmgdist = int(dmgdist*2)

#     if EnmyDmg < PlayerDmg:
#       if not PlayerAttacked2nd:
#         $ EnmySts.append('Broken')

#       if enmychoice ==0:
#         show Enmycard1 onlayer overlay:
#           xalign 0.5 yalign 0.1
#           linear 0.15 zoom 0.96 alpha 0.8
#           xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#           pause .05
#           xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#           pause .05
#           xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#           pause 0.1
#           xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#           pause 0.05
#           xoffset 0 yoffset 0
#           linear 0.1 zoom 0.7 alpha 0.0
#       elif enmychoice ==1:
#         show Enmycard2 onlayer overlay:
#           xalign 0.5 yalign 0.1
#           linear 0.15 zoom 0.96 alpha 0.8
#           xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#           pause .05
#           xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#           pause .05
#           xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#           pause 0.1
#           xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#           pause 0.05
#           xoffset 0 yoffset 0
#           linear 0.1 zoom 0.7 alpha 0.0
#       elif enmychoice ==2:
#         show Enmycard3 onlayer overlay:
#           xalign 0.5 yalign 0.1
#           linear 0.15 zoom 0.96 alpha 0.8
#           xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#           pause .05
#           xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#           pause .05
#           xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#           pause 0.1
#           xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#           pause 0.05
#           xoffset 0 yoffset 0
#           linear 0.1 zoom 0.7 alpha 0.0
#       elif enmychoice ==3:
#         show Enmycard4 onlayer overlay:
#           xalign 0.5 yalign 0.1
#           linear 0.15 zoom 0.96 alpha 0.8
#           xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#           pause .05
#           xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#           pause .05
#           xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#           pause 0.1
#           xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#           pause 0.05
#           xoffset 0 yoffset 0
#           linear 0.1 zoom 0.7 alpha 0.0

#     show Enemy:
#       linear 0.15 zoom 0.96
#       xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#       pause .05
#       xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#       pause .05
#       xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#       pause 0.1
#       xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#       pause 0.05
#       xoffset 0 yoffset 0
#       linear 0.1 zoom 1.0
#     show dmgpoint onlayer overlay
#     $ renpy.pause(0.8,hard=True)
#     $ Enmyhand.remove(Enmyhand[enmychoice])

#   elif "Freeze" in fxn:
#     #FREEZE TARGET

#     play sound "sfx/frz.wav"
#     $ EnmySts.append("Frozen")
#     show Frzsts:
#       zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
#       linear 0.1 zoom 0.98
#       linear 0.2 zoom 1.0 alpha 0.0
#     $ renpy.pause(0.5,hard=True)
#     hide Frzsts
#   elif "Burn" in fxn:
#     #FREEZE TARGET
#     play sound "sfx/fire.wav"
#     $ EnmySts.append("Burned")
#     $ EnmySts.append("Burned")
#     $ EnmySts.append("Burned")
#     $ EnmySts.append("Burned")
#     show Brnsts:
#       zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
#       linear 0.1 zoom 0.98
#       linear 0.2 zoom 1.0 alpha 0.0
#     $ renpy.pause(0.5,hard=True)
#     hide Brnsts
#   elif "Search" in fxn:
#     #NEGATE MISS
#     $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/slash.wav"
#     $ dmgdist = (PlayerDmg/20)
#     $ dmgdist = int(dmgdist)
#     show Enemy:
#       linear 0.15 zoom 0.96
#       xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#       pause .05
#       xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#       pause .05
#       xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#       pause 0.1
#       xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#       pause 0.05
#       xoffset 0 yoffset 0
#       linear 0.1 zoom 1.0
#     $ renpy.pause(0.4,hard=True)
#   elif "Firewall" in fxn:
#     #NEGATE Attack
#     $ EnmyHP = EnmyHP-PlayerDmg
#     play sound "sfx/slash.wav"
#     $ dmgdist = (PlayerDmg/20)
#     $ dmgdist = int(dmgdist)
#     show Enemy:
#       linear 0.15 zoom 0.96
#       xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#       pause .05
#       xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#       pause .05
#       xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#       pause 0.1
#       xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#       pause 0.05
#       xoffset 0 yoffset 0
#       linear 0.1 zoom 1.0
#     $ renpy.pause(0.4,hard=True)

#   if "Burned" in EnmySts:
#         play sound "sfx/fire.wav"
#         python:
#           burndmg = 0
#           for fxns in EnmySts:
#             if fxns=="Burned":
#               burndmg = burndmg +10
#         show Brnsts:
#           zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
#           linear 0.1 zoom 0.98
#           linear 0.2 zoom 1.0 alpha 0.0
#         $ EnmyHP = EnmyHP-burndmg
#         $ EnmySts.remove('Burned')
#         $ dmgdist = (burndmg/20)
#         $ dmgdist = int(dmgdist)
#         show dmgpointb
#         show Enemy:
#           linear 0.1 zoom 0.96
#           xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
#           pause .05
#           xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
#           pause .05
#           xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
#           pause 0.1
#           xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
#           pause 0.05
#           xoffset 0 yoffset 0
#           linear 0.1 zoom 1.0
#         $ renpy.pause(0.5,hard=True)
#         hide Brnsts
#   call TurnEnd
#   return
# screen Game_menu:

# screen Concatenate:

# label narrative

# label Game_cycle:
#     call narrative
#     call screen Game_menu

#     if not game_ending:
#       jump Game_cycle
#     return
