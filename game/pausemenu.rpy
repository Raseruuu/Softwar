label pauseshow:
    $ILY_p = '0'
    $ILY_m = 'happy3'
    $ILY_e = '1'

    call screen pausemenu
    if _return=="FAI":
        "Uguu"
    elif _return=="Items":
        "Items"
    elif _return=="Plugins":
        "Plugins"


    return

screen Items:
    frame:
        null width 10
transform marquee:
   #on show:
     xpos 1.0 xanchor 0.0
     linear 6.0 xpos 0.0 xanchor 1.0

     repeat
transform vmarquee:
   #on show:
     rotate -90
     ypos 1.0 yanchor 0.0
     linear 6.0 ypos 0.0 yanchor 1.0
     repeat     
screen pausemenu:
    key "p" action Return()
    key "P" action Return()
    # key 'x' action Return("MapTalk")
    # key 'X' action Return("MapTalk")
    image "black" at pausedim
    text "{size=100}{b}SOFTWAR{/b}{/size}" at marquee ypos 0.03
    image "gui/rpgmenu/frame1.png" at pausetrans3 xalign 0.0 yalign 0.0
    image "gui/rpgmenu/frame2.png" at pausetrans4 xalign 1.0 yalign 1.0
    add "ILY" xalign 0.15 at pausetrans1
    frame:
        at pausetrans1
        style_prefix "stats"
        xalign 0.05 yalign 0.85 xsize 400
        hbox:
            style_prefix "battlestats"
            null width 4
            vbox:
                text "{b}[playerName]{/b}"
                vbox:
                    frame: 
                        style_prefix "healthbar"
                        xsize bar_size(playerHP,playerHPMax,251)
                        # xsize 
                    null height 7
                    text "HP: [playerHP]/[playerHPMax]"
                    null height 10
    imagebutton idle "gui/rpgmenu/fai.png"     xanchor 0.5 xpos 0.62 yanchor 0.5 ypos 0.21 at pausetrans2 action Return("FAI")
    imagebutton idle "gui/rpgmenu/plugins.png" xanchor 0.5 xpos 0.62 yanchor 0.5 ypos 0.51 at pausetrans2 action Return("Plugins")
    imagebutton idle "gui/rpgmenu/items.png"   xanchor 0.5 xpos 0.85 yanchor 0.5 ypos 0.21 at pausetrans2 action Return("Items")
    imagebutton idle "gui/rpgmenu/saveload.png" xanchor 0.5 xpos 0.85 yanchor 0.5 ypos 0.51 at pausetrans2 action ShowMenu("save")
    imagebutton idle "gui/rpgmenu/return.png" xanchor 0.5 xpos 0.73 yanchor 0.5 ypos 0.81 at pausetrans2 action Return()


transform pausetrans1:
    alpha 0.0 xoffset -20 zoom 0.9
    on show:
        ease 0.3 alpha 1.0 xoffset 0
    alpha 1.0
transform pausetrans2:
    alpha 0.0 xoffset 20
    on show:
        ease 0.3 alpha 1.0 xoffset 0
    alpha 1.0
    on hide:
        ease 0.3 alpha 0.0 xoffset -20
transform pausetrans3:
    xanchor 1.0
    on show:
        linear 0.1 alpha 1.0 xanchor 0.0
transform pausetrans4:
    xanchor 0.0
    on show:
        linear 0.1 alpha 1.0 xanchor 1.0
transform pausedim:
    alpha 0.0
    on show:
        ease 0.3 alpha 0.77
    alpha 0.77
    
transform pauseshow:
    alpha 0.0
    on show:
        ease 0.3 alpha 1.0
    alpha 1.0