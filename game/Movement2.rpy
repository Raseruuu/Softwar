init -3 python:
    class SpriteinMap:
        def __init__(self,name,position,direction,dialogue):
            self.name=name
            self.position = position
            self.direction = direction
            self.dialogue = dialogue
    Avesprite = SpriteinMap("Ave",[5,3],'down',"Ave")
    Heartsprite = SpriteinMap("Heart",[7,5],'down',"Heart")
    CodeRedsprite = SpriteinMap("CodeRed",[7,3],'down',"CodeRed")
    Virasprite = SpriteinMap("Vira",[3,3],'down',"Vira")
    Melissasprite = SpriteinMap("Vira",[3,3],'down',"Vira")

    spritelist = []

label addsprites(gridplace):
    python:
        gridplace = (gridplace[0],gridplace[1])
        if gridplace in mapwheredict:
            Where = mapwheredict[gridplace]
        else:
            Where = "Road"
        # renpy.say("",str(gridplace))
        if gridplace in mapspritesdict:
            for key in mapspritesdict:
                if gridplace == key:
                    for sprite in mapspritesdict[gridplace]:
                        spritelist.append(sprite)
            # else:
            #     spritelist = []
                #
        else:
            # renpy.say("","nosprites")
            spritelist=[]



    return
