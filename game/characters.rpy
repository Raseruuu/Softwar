define narrator = Character(ctc="ctc", ctc_position="fixed", callback=speaker("N"))
define j = Character("John", color = '#0b99f4', image = "John_Side", callback = speaker("John"), ctc="ctc", ctc_position="fixed")

define h = Character("Hilbert",color = '#f7941d', image = "Hilbert_side", ctc="ctc", ctc_position="fixed",callback=speaker("Hilbert"))
define l = Character("Lisa",color = '#992e2c', image = "Lisa_side", callback=speaker("Lisa"), ctc="ctc", ctc_position="fixed")
define info = Character("INFO",callback=speaker("INFO"), color='#fff', ctc="ctc", ctc_position="fixed")

define i = Character("ILY",callback=speaker("ILY"), color='#f00', image = "ILY_side", ctc="ctc", ctc_position="fixed")
define v = Character("Vira",callback=speaker("Vira"), color ='#f00', ctc="ctc", ctc_position="fixed") 
define c = Character("Code Red",callback=speaker("CodeRed"), color='#f00', ctc="ctc", ctc_position="fixed") 
define a = Character("Ave",callback=speaker("Ave"), color='#ff8a00', image ="Ave_side", ctc="ctc", ctc_position="fixed") 
define cv = Character("Virus Boy",callback=speaker("CodeRed"), color='#f00', ctc="ctc", ctc_position="fixed") 
define aa = Character("Antivirus Girl",callback=speaker("Ave"), color='#202020', ctc="ctc", ctc_position="fixed") 

define hx = Character("Hacker X",color = '#088', image = "HackerX_side", ctc="ctc", ctc_position="fixed",callback=speaker("HackerX"))


define uc = Character("USB-chan",callback=speaker("USB-chan"),color='#d10', ctc="ctc", ctc_position="fixed") 
define uk = Character("USB-kun",callback=speaker("USB-kun"),color='#01d', ctc="ctc", ctc_position="fixed")
########
## Functions
########
init -1 python:
    ## Initialize variables
    globals()["stopblips"] = False
    globals()["direction"] = "down"
    globals()["pdirection"] = "down"
    globals()["bg"] = "1"
    globals()["anim_done"] = True
    globals()["jumping"] = False
    
    
    globals()["ILY_m"] = "happy"
    globals()["ILY_p"] = "1"
    globals()["ILY_e"] = "1"
    globals()["ILY_w"] = False

    globals()["John_e"] = "normal"
    globals()["John_m"] = "happy"

    globals()["Lisa_e"] = "normal"
    globals()["Lisa_m"] = "happy"
    globals()["Lisa_w"] = True

    globals()["Vira_m"] = "happy"
    globals()["Vira_e"] = "mad"

    globals()["Ave_e"] = "mad"
    globals()["Ave_m"] = "frown"
    globals()["Ave_w"] = True
    




    speaking = None
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
            
    curried_while_speaking = renpy.curry(while_speaking)
    
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    renpy.music.register_channel("blipsound", mixer="sfx", stop_on_mute=True, tight=False, buffer_queue=True, movie=False)     
    
    def speaker_callback(name, event, **kwargs):
        global speaking
        if event == "begin":
            speaking = name
            globals()["stopblips"]=False
            
            if (name == "John"):
               renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
            elif (name == "ILY"):
               renpy.sound.play("sound/character/high.ogg", channel="blipsound", loop=True)
            elif (name == "Lisa"):
               renpy.sound.play("sound/character/mid.ogg", channel="blipsound", loop=True)
            elif (name == 'N'):
               renpy.sound.play("sound/character/sfx-blipmale.wav", channel="blipsound", loop=True)
            elif (name == 'Hilbert'):
               renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
            elif (name == 'CodeRed'):
               renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
            elif (name == 'Vira'):
               renpy.sound.play("sound/character/high.ogg", channel="blipsound", loop=True)
            elif (name == 'Ave'):
               renpy.sound.play("sound/character/sfx-blipfemale.wav", channel="blipsound", loop=True)
            elif (name == 'USB-kun'):
               renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
            elif (name == 'USB-chan'):
               renpy.sound.play("sound/character/high.ogg", channel="blipsound", loop=True)
            elif (name == 'Hilbert'):
               renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
            elif (name == 'HackerX'):
               renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
            
        elif (event == "slow_done" or event == "end"):
            speaking = None
            renpy.sound.stop(channel="blipsound") 
        
            
    speaker = renpy.curry(speaker_callback)






    def ILYSprite(emotion="happy", pose=None):
        ## Only change pose if user input something
        if (pose != None):
            globals()["ILY_p"] = str(pose)
        
        ## Make everything lowercase
        emotion = emotion.lower()
        
        if (emotion == "happy"):
            globals()["ILY_m"] = "happy"
            globals()["ILY_e"] = '1'
            
        elif (emotion == "happy2"):
            globals()["ILY_m"] = "happy2"
            globals()["ILY_e"] = '1'
            
        elif (emotion == "happy3"):
            globals()["ILY_m"] = "happy3"
            globals()["ILY_e"] = '2'
            
        elif(emotion == "sad"):
            globals()["ILY_m"] = "sad"
            globals()["ILY_e"] = '1'
        elif(emotion == "mad"):
            globals()["ILY_m"] = "sad"
            globals()["ILY_e"] = '2'
        elif(emotion == "o"):
            globals()["ILY_m"] = "o"
            globals()["ILY_e"] = '1'
            
        else:
            raise ValueError("Unknown emotion entered: " + emotion)
            



    def JohnSprite(emotion="happy"):
        ## Make everything lowercase
        emotion = emotion.lower()
        
        if (emotion == "normal"):
            globals()["John_m"] = "happy"
            globals()["John_e"] = "normal"
            
        elif (emotion == "sad"):
            globals()["John_m"] = "sad"
            globals()["John_e"] = "up"
            
        elif (emotion == "mad"):
            globals()["John_m"] = "sad"
            globals()["John_e"] = "mad"
            
        else:
            raise ValueError("Unknown emotion entered: " + emotion)
            
    
    
    
    def LisaSprite(emotion="happy"):
        ## Make everything lowercase
        emotion = emotion.lower()
        
        if (emotion == "happy"):
            globals()["Lisa_m"] = "happy"
            globals()["Lisa_e"] = "normal"
            
        else:
            raise ValueError("Unknown emotion entered: " + emotion)
            
        
        
    def ViraSprite(emotion="happy"):
        ## Make everything lowercase
        emotion = emotion.lower()
        
        if (emotion == "happy"):
            globals()["Vira_m"] = "happy"
            globals()["Vira_e"] = "normal"
            
        elif (emotion == "sad"):
            globals()["Vira_m"] = "sad"
            globals()["Vira_e"] = "normal"
            
        elif (emotion == "mad"):
            globals()["Vira_m"] = "sad"
            globals()["Vira_e"] = "mad"
            
        else:
            raise ValueError("Unknown emotion entered: " + emotion)




#########
## ILY
#########
image ILYRpg="images/Characters/ILY/ILY[direction].png"

image ILYjumpRpg:
    "images/Characters/ILY/ILY[olddirection].png"
    xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.7
    linear 0.1 yoffset -80
    linear 0.05 yoffset 0


image side ILY_side:
    
    ConditionSwitch(
        "ILY_w==True","ILYside2",
        "ILY_w==False",Null(width=100)
    )
    zoom 0.38
image ILYside2:
    LiveCrop((240,100, 440,565), "ILYside3")

image ILYside3:
    "ILYFull"
    zoom 0.9

image Icon_ILY:
    LiveCrop((280,100, 440,565), "ILYFull")
    zoom 0.22


image ILY:
    "ILYFull"
    zoom 0.5
    yalign 0.1
    linear 1.0 yoffset -10
    linear 1.0 yoffset 10
    repeat
    
image ILY big:
    "ILYFull"
    zoom 0.75
    yalign 0.1
    linear 1.0 yoffset -10
    linear 1.0 yoffset 10
    repeat
    
image ILY small:
    "ILYFull"
    zoom 0.3
    yalign 0.3
    linear 1.0 yoffset -10
    linear 1.0 yoffset 10
    repeat

image ILYFull:
    LiveComposite(
    (0.75, 0.75), #(544,600),
    (0, 0), "images/Characters/ILY/ILY_p[ILY_p].png", #pose
    #(0, 0), "ILY_p[ILY_p].png",
    (0, 0), "images/Characters/ILY/ILY_e[ILY_p][ILY_e].png", #eyebrows
    (0, 0), "ILYEyes[ILY_p]",#eyes
    (0, 0), "images/Characters/ILY/ILY_heart[ILY_p].png",
    (0, 0), ConditionSwitch(
        "((ILY_p=='1') or (ILY_p=='0'))", WhileSpeaking(
            "ILY",
            ConditionSwitch(
                "('happy' in ILY_m)","ILYMouthHappy",
                "('happy' not in ILY_m)","ILYMouthSad"
                ),
            "images/Characters/ILY/ILY_m[ILY_m].png"
            ),
        "(ILY_p=='2')", WhileSpeaking(
                            "ILY",
                            ConditionSwitch(
                                "('happy' in ILY_m)","ILYMouthHappy2",
                                "('happy' not in ILY_m)","ILYMouthSad2"
                                ),
                            "images/Characters/ILY/ILY_m2[ILY_m].png"
                            )
        )
    )

image ILYEyes0:
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.0
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 8.0
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 4.0      
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.5
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07 
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.5
    repeat
        
image ILYEyes1:
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.0
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 8.0
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 4.0      
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.5
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07 
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.5
    repeat
        
image ILYEyes2:
    choice:
        "images/Characters/ILY/ILY_2eyes.png"
        pause 1.0
        "images/Characters/ILY/ILY_2eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_2eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_2eyesmclosed.png"
        pause 0.07
    choice:
        "images/Characters/ILY/ILY_2eyes.png"
        pause 8.0
    choice:
        "images/Characters/ILY/ILY_2eyes.png"
        pause 4.0      
    choice:
        "images/Characters/ILY/ILY_2eyes.png"
        pause 1.5
        "images/Characters/ILY/ILY_2eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_2eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_2eyesmclosed.png"
        pause 0.07 
        "images/Characters/ILY/ILY_2eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_2eyes.png"
        pause 1.5
    repeat
        
image ILYMouthHappy:
    "images/Characters/ILY/ILY_mmidopen.png"
    pause .08
    "images/Characters/ILY/ILY_mhappy2.png"
    pause .05
    "images/Characters/ILY/ILY_mhappy.png"
    pause .08
    "images/Characters/ILY/ILY_mhappy2.png"
    pause .05
    "images/Characters/ILY/ILY_mmidopen.png"
    pause .08
    "images/Characters/ILY/ILY_mhappy3.png"
    pause .08
    "images/Characters/ILY/ILY_mmidopen.png"
    pause .05
    "images/Characters/ILY/ILY_mO2.png"
    pause .08
    "images/Characters/ILY/ILY_mO.png"
    pause .1
    "images/Characters/ILY/ILY_mO2.png"
    pause .08
    "images/Characters/ILY/ILY_mmidopen.png"
    pause .05
    "images/Characters/ILY/ILY_mhappy3.png"
    pause .08
    repeat 
        
image ILYMouthHappy2:
    "images/Characters/ILY/ILY_m2happy2.png"
    pause .08
    "images/Characters/ILY/ILY_m2happy2.png"
    pause .05
    "images/Characters/ILY/ILY_m2happy.png"
    pause .08
    "images/Characters/ILY/ILY_m2happy2.png"
    pause .05
    "images/Characters/ILY/ILY_m2happy2.png"
    pause .08
    "images/Characters/ILY/ILY_m2happy3.png"
    pause .08
    "images/Characters/ILY/ILY_m2happy2.png"
    pause .05
    "images/Characters/ILY/ILY_m2O2.png"
    pause .08
    "images/Characters/ILY/ILY_m2O.png"
    pause .1
    "images/Characters/ILY/ILY_m2O2.png"
    pause .08
    "images/Characters/ILY/ILY_m2happy2.png"
    pause .05
    "images/Characters/ILY/ILY_m2happy3.png"
    pause .08
    repeat 
        
image ILYMouthSad:
    "images/Characters/ILY/ILY_mO2.png"
    pause .08
    "images/Characters/ILY/ILY_mO.png"
    pause .1
    "images/Characters/ILY/ILY_mO2.png"
    pause .08
    "images/Characters/ILY/ILY_msad.png"
    pause .08
    repeat 
        
image ILYMouthSad2:
    "images/Characters/ILY/ILY_m2O2.png"
    pause .08
    "images/Characters/ILY/ILY_m2O.png"
    pause .1
    "images/Characters/ILY/ILY_m2O2.png"
    pause .08
    "images/Characters/ILY/ILY_m2sad.png"
    pause .08
    repeat

#########
## John
#########
image side John_Side:
    "JohnFull"
    zoom 0.4

#image John:
#    "JohnFull"

image John eyeszoom:
    LiveCrop((0,200,440,100),"JohnFull")
    zoom 2.0 yalign 0.5 xalign 0.5

image JohnFull:
    LiveComposite(
        (440,565),
        (0, 0), "images/Characters/John/Johnb.png",
        (0, 0), WhileSpeaking(
            "John",ConditionSwitch(
                "('happy' in John_m)","JohnMouthHappy",
                "('happy' not in John_m)","JohnMouthSad"
                ),
            "images/Characters/John/John_m[John_m].png"
            ),
        (0, 0), "images/Characters/John/John_e[John_e].png", 
        (0, 0), "JohnEyes",#eyes
        (0, 0), "images/Characters/John/John_glasses.png")

image JohnMouthHappy:
    "images/Characters/John/John_mspeak1.png"
    pause .05
    "images/Characters/John/John_mspeak2.png"
    pause .05
    "images/Characters/John/John_mspeak4.png"
    pause .08
    "images/Characters/John/John_mspeak2.png"
    pause .05
    "images/Characters/John/John_mspeak1.png"
    pause .05
    "images/Characters/John/John_mhappy.png"
    pause .05
    repeat
        
image JohnMouthSad:
    "images/Characters/John/John_mspeak1.png"
    pause .08
    "images/Characters/John/John_mspeak2.png"
    pause .05
    "images/Characters/John/John_mspeak3.png"
    pause .05
    "images/Characters/John/John_mspeak2.png"
    pause .05
    "images/Characters/John/John_mspeak1.png"
    pause .08
    "images/Characters/John/John_msad.png"
    pause .05
    repeat
        
image JohnEyes:
    choice:
        "images/Characters/John/John_eyes.png"
        pause 1.0
        "images/Characters/John/John_eyesmclosed.png"
        pause 0.07
        "images/Characters/John/John_eyesclosed.png"
        pause 0.1
        "images/Characters/John/John_eyesmclosed.png"
        pause 0.07
    choice:
        "images/Characters/John/John_eyes.png"
        pause 8.0
    choice:
        "images/Characters/John/John_eyes.png"
        pause 4.0      
    choice:
        "images/Characters/John/John_eyes.png"
        pause 1.5
        "images/Characters/John/John_eyesmclosed.png"
        pause 0.07
        "images/Characters/John/John_eyesclosed.png"
        pause 0.1
        "images/Characters/John/John_eyesmclosed.png"
        pause 0.07 
        "images/Characters/John/John_eyesclosed.png"
        pause 0.1
        "images/Characters/John/John_eyes.png"
        pause 1.5
    repeat



#########
## Lisa
#########
# image Lisa:
#     "Lisafull"
#     zoom 0.5
        
image Lisafull:

        LiveComposite(
        (507,730),
        (0, 0), "images/Characters/Lisa/Lisabase.png",
        (0, 0), WhileSpeaking(
            "Lisa",
            # ConditionSwitch(
            ConditionSwitch(
                "('happy' in Lisa_m)","LisaMouthHappy",
                "('happy' not in Lisa_m)","LisaMouthSad"
                ),
            "images/Characters/Lisa/Lisa_m[Lisa_m].png"
            ),
        (0, 0), "images/Characters/Lisa/Lisa_e[Lisa_e].png", 
        (0, 0), "LisaEyes",#eyes
        )
image Lisa:
    "Lisafull"
    # yanchor 0.0 ypos 0.01
    # linear 1.0 yoffset 0
    # pause .5
    # linear 1.0 yoffset 5
    # pause .5
    # repeat

image Lisa sidew:
    LiveCrop((150,40, 300,385), "Lisafull")
    zoom 0.56
image side Lisa_side:
    ConditionSwitch(
        "Lisa_w==True","Lisa sidew",
        "Lisa_w==False",Null(width=100))
    
    
 
image LisaEyes:
    choice:
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 1.0
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
        "images/Characters/Lisa/Lisa_eclose2.png"
        pause 0.1
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
    choice:
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 5.0
    choice:
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 4.0      
    choice:
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 1.5
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
        "images/Characters/Lisa/Lisa_eclose2.png"
        pause 0.1
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07 
        "images/Characters/Lisa/Lisa_eclose2.png"
        pause 0.1
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 1.5
    repeat
        
image LisaMouthHappy:
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen3.png"
    pause .08
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .05
    "images/Characters/Lisa/Lisa_mhappy.png"
    pause .05
    "images/Characters/Lisa/Lisa_mhappy2.png"
    pause .08
    "images/Characters/Lisa/Lisa_mhappy3.png"
    pause .1
    "images/Characters/Lisa/Lisa_mhappy2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mhappy.png"
    pause .08
    repeat

image LisaMouthSad:
    "images/Characters/Lisa/Lisa_mhappy2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen3.png"
    pause .08
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mhappy2.png"
    pause .05
    "images/Characters/Lisa/Lisa_msad.png"
    pause .05
    repeat
#########
## Vira
#########

image Vira large:
    "ViraFull"
    yalign 0.05
    linear 1.0 yoffset -5
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat
    
image Vira:
    "Vira large"
    # zoom 0.25

image ViraFull:
    LiveComposite(
        (680,961),
        (0, 0), "images/Characters/Vira/Vira_p.png",
        (0, 0), "images/Characters/Vira/Vira_e[Vira_e].png", #eyebrows
        (0, 0), "images/Characters/Vira/Vira_eopen.png",#eyes
        (0, 0), WhileSpeaking(
            "Vira",
            ConditionSwitch(
                "('happy' in Vira_m)","ViraMouthHappy",
                "('happy' not in Vira_m)","ViraMouthSad"
            ),
            "images/Characters/Vira/Vira_m[Vira_m].png"
        )
    )


image ViraMouthHappy:
    "images/Characters/Vira/Vira_mhappy2.png"
    pause .08
    "images/Characters/Vira/Vira_mhappy.png"
    pause .05
    "images/Characters/Vira/Vira_mhappy2.png"
    pause .1
    "images/Characters/Vira/Vira_mhappy.png"
    pause .05
   
    repeat
        
image ViraMouthSad:
    "images/Characters/Vira/Vira_mO2.png"
    pause .08
    "images/Characters/Vira/Vira_mO.png"
    pause .1
    "images/Characters/Vira/Vira_mO2.png"
    pause .08
    "images/Characters/Vira/Vira_msad.png"
    pause .08
    repeat 

















#########
## Code Red
#########

image CodeRed:
    "CodeRedFull"
    yanchor 0.0 ypos 0.01
    linear 1.0 yoffset 0
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat

image CodeRedFull:
    LiveComposite(
        (714,1025),
        (0, 0), "images/Characters/Code Red/CODE RED_base.png",
        (0, 0), WhileSpeaking(
            "CodeRed",
            "CodeRed mouth",
            "images/Characters/Code Red/CODE RED_mclosed.png"
        )
    )   

image CodeRed mouth:
    "images/Characters/Code Red/CODE RED_mopen1.png"
    pause .08
    "images/Characters/Code Red/CODE RED_mopen2.png"
    pause .1
    "images/Characters/Code Red/CODE RED_mopen1.png"
    pause .08
    "images/Characters/Code Red/CODE RED_mclosed.png"
    pause .08
    repeat
        
     
image ModeRed:
    "ModeRedFull"
    linear 0.25 alpha 0.8 yoffset 20
    linear 0.25 alpha 1.0 xoffset -20
    repeat 

image ModeRedFull:
    "images/Characters/Code Red/MODE RED3.png" 
    pause .05
    "images/Characters/Code Red/MODE RED4.png"
    pause .05
    "images/Characters/Code Red/MODE RED5.png"
    pause .05
    "images/Characters/Code Red/MODE RED6.png"
    pause .05
    repeat


#########
## Ave
#########
image Ave:
    "Avefull"
    yanchor 0.9 ypos 1.0 zoom 0.9
    linear 1.0 yoffset 0
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat
        

image Avefull:
    LiveComposite(
        (486,861),
        (0, 0), "images/Characters/Ave/Avebase.png",
        (0, 0), WhileSpeaking(
            "Ave",
            "Ave mouth",
            "images/Characters/Ave/Ave_m[Ave_m].png"
            ),
        (0, 0), "images/Characters/Ave/Ave_e[Ave_e].png", 
        (0, 0), "AveEyes",#eyes
        (0, 0), "images/Characters/Ave/Aveshades.png",
        )
image AveEyes:
    "images/Characters/Ave/Ave_eyes.png"

image Ave mouth:
    "images/Characters/Ave/Ave_mspeak1.png"
    pause .08
    "images/Characters/Ave/Ave_mspeak2.png"
    pause .1
    "images/Characters/Ave/Ave_mspeak1.png"
    pause .08
    "images/Characters/Ave/Ave_mfrown.png"
    pause .08
    repeat
image Ave sidew:
    LiveCrop((140,40, 300,385), "Avefull")
    zoom 0.56
image side Ave_side:
    ConditionSwitch(
        "Ave_w==True","Ave sidew",
        "Ave_w==False",Null(width=100))
    
    
    

#########
## Hilbert
#########
# image Lisa sidew:
#     LiveCrop((150,45, 300,350), "Lisafull")
#     zoom 0.59
image side Hilbert_side:
    "images/Characters/Hilbert/Hilbertb.png"
    zoom 0.38
    # ConditionSwitch(
    #     "Lisa_w==True","Lisa sidew",
    #     "Lisa_w==False",Null(width=100))
    
    
#########
## Hacker X
#########
image side HackerX_side:
    "images/Characters/HackerX/HackerX.png"
    zoom 0.38
    # ConditionSwitch(
    #     "Lisa_w==True","Lisa sidew",
    #     "Lisa_w==False",Null(width=100))
    






