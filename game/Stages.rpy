

init -2 python:
    def digital_root(a):
        while a>=10:
            b = int(a/10) #the rest of the other digits
            c = a-(b*10) #the rightmost digit
            a = b+c
        return a

    # import numpy
  
    def nextlocation(destinationstage,Door):
        newX=0
        newY=0
        founddoor=False
        if Door=="a":
            #d
            # search and get indexes of letter d
            gridmap = destinationstage
            for maprows in gridmap:

                if "d" in maprows:
                    newX=maprows.index("d")
                    founddoor=True
                if not founddoor:
                    newY+=1
            newY-=1
        elif Door=="b":
            #c
            # search and get indexes of letter c
            gridmap = destinationstage
            for maprows in gridmap:
                if "c" in maprows:
                    newX=maprows.index("c")
                    founddoor=True
                if not founddoor:
                    newY+=1
            newX+=1
        elif Door=="c":
            #b
            # search and get indexes of letter b
            gridmap = destinationstage
            for maprows in gridmap:
                if "b" in maprows:
                    newX=maprows.index("b")
                    founddoor=True
                if not founddoor:
                    newY+=1
            newX-=1
        elif Door=="d":
            #a
            # search and get indexes of letter a
            gridmap = destinationstage
            for maprows in gridmap:
                if "a" in maprows:
                    newX=maprows.index("a")
                    founddoor=True
                if not founddoor:
                    newY+=1
            newY+=1    
            # newX 
            # newY
        # renpy.say("test","("+str(newX)+","+str(newY)+")")  

        return (newX,newY)
    def map_token(mapsheet):
      newmap = []
      for rows in mapsheet:
        newmap.append([ch for ch in rows])

      return (newmap)
    # def map_token(mapsheet):
    #   newmap = []
    #   for rows in mapsheet:
    #     newmap.append([ch for ch in rows])

    #   return (newmap)
    
    # stage
    


    # class Place:
    #     def __init__(self,name,mapbox,safe)
    #         self.name = name
    #         self.mapbox = mapbox
    #         self.safe = safe
            


    # stageproto = [
    #     "1111111111111111",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1111111111111111"
    #     ]
    # stage1 = tokenize(stage)
    stage0 = [
     #0  0     1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17
        '1111111',
        '1000001',
        '1000001',
        '1002001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1110111',
        'nn111nn'
        ]
    stage0=map_token(stage0)
    stagea = [
     #0  0     1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17
        '111111111111111111',
        '100000100020000001',
        '10d000102000000001',
        '1110111010d0000001',
        'nn1010001010000001',
        'nn1010111010000001',
        'nn1000000010000001',
        '111001111010000001',
        '100001nn1011110101',
        '100001nn1000000101',
        '111111nn1111111111'
        ]
    stagea=map_token(stagea)
    stagehome = [
     #0  0     1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17
        '111111111111111',
        '1000000a0000001',
        '100000000000001',
        '100011111110001',
        '100010000010001',
        '1c00000000000b1',
        '100010000010001',
        '100011101110001',
        '100000000000001',
        '1000000d0000001',
        '111111111111111'
        ]
    stagehome=map_token(stagehome)
    stage1 = [
        
        'nnn11111111111',
        'n1110000000001',
        'n1000000000001',
        '11000000000001',
        '1c000000000001',
        '11000000000001',
        'n1000000000001',
        'n1110000000001',
        'nnn11111111111',
        ]
    stage1=map_token(stage1)    
    stageemptyroom = [
        'nnn111nnn',
        'n111a111n',
        'n1000001n',
        '110000011',
        '1c00000b1',
        '110000011',
        'n1000001n',
        'n111d111n',
        'nnn111nnn',
        ]
    stageemptyroom=map_token(stageemptyroom)
    stage3 = [
        'nnn111nnn',
        'n111a111n',
        'n1000001n',
        '110000011',
        '1c00000b1',
        '110000011',
        'n1000001n',
        'n111d111n',
        'nnn111nnn'
        ]
    stage3=map_token(stage3)
    stagek=[
        'nnnnnnnnn111nnnnnnnnn',
        'nnnnnnnnn1a1nnnnnnnnn',
        'nnnnnnnnn101nnnnnnnnn',
        'nnnnnnnnn101nnnnnnnnn',
        'nnnn1111110111111nnnn',
        'nnnn1000000000001nnnn',
        '111110000000000011111',
        '1c00000000100000000b1',
        '111110000000000011111',
        'nnnn1000000000001nnnn',
        'nnnn1111110111111nnnn',
        'nnnnnnnnn101nnnnnnnnn',
        'nnnnnnnnn101nnnnnnnnn',
        'nnnnnnnnn1d1nnnnnnnnn',
        'nnnnnnnnn111nnnnnnnnn'
        ]
    stagek=map_token(stagek)
    stage124578=[
        'nnnnnn111nnnnnn',
        'nnnnnn1a1nnnnnn',
        'nnnnnn101nnnnnn',
        'nnn111101111nnn',
        'nnn100000001nnn',
        'nnn100000001nnn',
        '111100000001111',
        '1c00000000000b1',
        '111100000001111',
        'nnn100000001nnn',
        'nnn100000001nnn',
        'nnn111101111nnn',
        'nnnnnn101nnnnnn',
        'nnnnnn1d1nnnnnn',
        'nnnnnn111nnnnnn'
        ]
    stage124578=map_token(stage124578)
    stage369=[
        'nnnnnnnnnn1nnnnnnnnnn',
        'nnnnnnnnn1a1nnnnnnnnn',
        'nnnnnnnn10001nnnnnnnn',
        'nnnnnnn1000001nnnnnnn',
        'nnnnnn100000001nnnnnn',
        'nnnnn10000000001nnnnn',
        'nnnn1000000000001nnnn',
        'nnn100000000000001nnn',
        'nn10000000000000001nn',
        'n1000000000000000001n',
        '1c00000000000000000b1',
        'n1000000000000000001n',
        'nn10000000000000001nn',
        'nnn100000000000001nnn',
        'nnnn1000000000001nnnn',
        'nnnnn10000000001nnnnn',
        'nnnnnn100000001nnnnnn',
        'nnnnnnn1000001nnnnnnn',
        'nnnnnnnn10001nnnnnnnn',
        'nnnnnnnnn1d1nnnnnnnnn',
        'nnnnnnnnnn1nnnnnnnnnn'
        ]
    stage369=map_token(stage369)
    # stagek=[
    #     '1111101111111111111111111nnnnn',
    #     '1000001000000000000000001nnnnn',
    #     '1000001000000000000000001nnnnn',
    #     '1c0001000011111110000000111111',
    #     '100000000100000000000000000001',
    #     '111110d01000000000000000000001',
    #     '100001111000010000100000000001',
    #     '100000000000010000111111111111',
    #     '100000000000010000000000000001',
    #     '100000000000010000000000000001',
    #     '100000000000011111111111111111',
    #     '100000000000000000000000000001',
    #     '100000000000000000000001111001',
    #     '10b001111111111111111111000001',
    #     '111110000000000000000001000001',
    #     '100000000000000000000000000001',
    #     '100000000000000000000001000001',
    #     '100000000000000000000001000001',
    #     '111111111111111111111111111111'
    # ]
    # stagek=map_token(stagek)
    # stagek=[
    #     'nnnnnnnnnnn0n0n',
    #     'nnnnnnnnn1000nn',
    #     '111111110n0n0nn',
    #     '10000000n0n0n01',
    #     '10000000010n0n1',
    #     '100000000000001',
    #     '10000000000010n',
    #     '100000000000n1n',
    #     '10000000000001n',
    #     '10000000000001n',
    #     '11111111111111n'
    # ]
    # stagek=map_token(stagek)
    stagebroken=[
        'nnnnnnnnnnn0n0n',
        'nnnnnnn1n1000nn',
        '1111111a0n0n0nn',
        '10000000n0n0n01',
        '10000000010n0n1',
        '100000000000001',
        '1c00000000000bn',
        '100000000000nn1',
        '100000000000001',
        '1000000d0000001',
        '111111111111111'
    ]
    stagebroken=map_token(stagebroken)
    stageAD=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageAD=map_token(stageAD)
    stageABD=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        'n1000000011',
        'n10000000b1',
        'n1000000011',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageABD=map_token(stageABD)
    stageABC=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        '11000000011',
        '1c0000000b1',
        '11000000011',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageABC=map_token(stageABC)
    stageAB=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        'n1000000011',
        'n10000000b1',
        'n1000000011',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageAB=map_token(stageAB)
    stageAC=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        '1100000001n',
        '1c00000001n',
        '1100000001n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageAC=map_token(stageAC)
    stageBD=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n1000000011',
        'n10000000b1',
        'n1000000011',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]

    stageBD=map_token(stageBD)
    stageCD=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        '1100000001n',
        '1c00000001n',
        '1100000001n',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageCD=map_token(stageCD)
    stageACD=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        '1100000001n',
        '1c00000001n',
        '1100000001n',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageACD=map_token(stageACD)
    stageD=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageD=map_token(stageD)

    Connecht_square=[
        'nnnnnn1111111111nnnnnnnn',
        'nnnn1100000000000010000nn',
        'nnn10000000000000000000nn',
        'nn100000000000000000000nn',
        'n100000nnnn000nnnn0000001',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'nn111100000000011100000nn',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n11111111111111111111111n'
    ]
    Connecht_square=map_token(Connecht_square)



    
    globals()["GRID"] ={
        #x y
        (192,168):stagehome,
        # (193,168):stagebroken,
        (192,167):stageAD,
        (192,166):stageAD,
        (191,166):stageAD,
        (191,167):stageAD,
        (193,166):stageAD,
        (193,167):stageAD,
        (191,168):stageABD,
        (191,169):stageAB,
        
        (192,169):stageABC,
        (193,169):stageAC,
        (193,168):stageACD,

        (193,165):stageCD,
        (192,165):stage124578,
        (191,165):stageBD,
        (192,164):stageD,
        
        }
    
    mapspritesdict={
        (192,168):[Heartsprite],
        (192,164):[Avesprite,CodeRedsprite]  
          
        }
    mapwheredict={
        (192,168):"Home"    
        }





label doorjump:
     
    $ doordirection = Here #abcd
    # a =North
    # b =East
    # c =West
    # d =South
    if doordirection == "a":
        $gridpos[1] = gridpos[1] - 1
    elif doordirection == "b":
        $gridpos[0] = gridpos[0] + 1
    elif doordirection == "c":
        $gridpos[0] = gridpos[0] - 1
    elif doordirection == "d":
        $gridpos[1] = gridpos[1] + 1
    
    $ GRIDX= gridpos[0] 
    $ GRIDY= gridpos[1]

    $ Grid_D_root=digital_root(GRIDX+GRIDY)

    # globals()["GRID"][GRIDX,GRIDY] in 
    # if thereisaroom on this position

    if (GRIDX,GRIDY) in globals()["GRID"]:
        $ griddestination = globals()["GRID"][(GRIDX,GRIDY)]
        $ transfercoordinates = nextlocation(griddestination,doordirection)
        call maptransfer(transfercoordinates,griddestination)
    
    elif (((((Grid_D_root==1) or (Grid_D_root==2)) or (Grid_D_root==4)) or (Grid_D_root==5)) or (Grid_D_root==7)) or (Grid_D_root==8):
        $griddestination = stage124578
        $transfercoordinates = nextlocation(griddestination,doordirection)
        call maptransfer(transfercoordinates,griddestination)
    
    elif ((Grid_D_root==3) or (Grid_D_root==6)) or (Grid_D_root==9):
        $griddestination = stage369
        $transfercoordinates = nextlocation(griddestination,doordirection)
        call maptransfer(transfercoordinates,griddestination)
    else:
        $griddestination = stageemptyroom
        $transfercoordinates = nextlocation(griddestination,doordirection)
        call maptransfer(transfercoordinates,stageemptyroom)
    # if boxsheet == stage0:

    #   call maptransfer([4,2],stage1)
    # elif Where =="Home":
      
    #   $ destination = stage1

    #   if Here=='b':
    #     $ spritelist = []
    #     $ gridpos[0] = gridpos[0] + 1
    #     $ Where = "stage1"
    #     call maptransfer([2,4],destination)
    # elif Where == "stage1":
    #   $ destination = stagehome
    #   if Here=='c':
    #     $ spritelist = [Heartsprite]
    #     $ gridpos[0] = gridpos[0] - 1
    #     $ Where = "Home"
    #     call maptransfer([12,5],destination)
    
    # elif boxsheet == stage3:
    #   call maptransfer([3,14],stage1)
    
    return
