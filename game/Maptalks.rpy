
label whatactor:
    if actornum == '2':
      i"That's the virus!"
      $ John_m = "sad"
      $ John_e = "mad"
      j"Get Ready, Ily!"
      hide screen mapA
      hide screen mapB
      return
    elif len(actornum)>1:
      if actornum == 'Ave':
        if objectbelow=="Ave":
          $ILY_m='happy'
          $ILY_e='2'
          i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
        a"YOU'RE A VIRUS!! I MUST DESTROY YOU!"
        hide screen mapB
        hide screen mapA
        call battlev3(ILY,Ave)
        if playerHP<=0:
            return
        $ enemy_encounter=False
        $ map_active=True
        call mapresume
        return
      elif actornum == 'CodeRed':
        if objectbelow=="CodeRed":
          $ILY_m='happy'
          $ILY_e='2'
          i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
        $CodeRed_w=True
        c"I'm just doing my job!"
        hide screen mapB
        hide screen mapA
        call battlev3(ILY,CodeRed)
        if playerHP<=0:
            return
        $ enemy_encounter=False
        $ map_active=True
        call mapresume
        return
      elif actornum == 'Vira':
        if objectbelow=="Vira":
          $ILY_m='happy'
          $ILY_e='2'
          i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
        $Vira_w=True
        v"Uguu! What do you want!!"
        hide screen mapB
        hide screen mapA
        call battlev3(ILY,Vira)
        if playerHP<=0:
            return
        $ enemy_encounter=False
        $ map_active=True
        call mapresume
        return
      elif actornum == 'Heart':
        i"Would you like to restore HP?"
        menu:
          "Would you like to restore HP?"
          "Yes":
            $playerHP=playerHPMax
            play sound "sfx/heal.ogg"
            "[playerName]'s Health Points have been restored."
          "No":
            i"OK."
      elif actornum == 'Melissa':
         call script2
      show screen mapB
      call screen mapA
      call Returns
      return
    else:
      show screen mapB
      call screen mapA
      call Returns
    return
label PlatformTalk:
    "Uguu"
    return
label MapTalk:
    # if boxsheet == stagehome:
    if boxsheet:
      $ maptalks+=1
      if maptalks==1:
        i"I'd love to say something virtuous, but the demo is over."
        j"What's new?"
        i"Well, there's a new boss over to the north!"
        j"Already?"
        i"She's my sworn rival!"
        j"I just got you and you already have a rival?!"
      elif maptalks==2:
        i"Why are you still here?"
        j"There has to be more to this demo, right?"
        i"Sorry there isn't."
      elif maptalks==3:
        j"I'm curious what's on the other side."
        i"It's incomplete, but it has other things."
        j"Other things?"
        i"Classified Information."
      elif maptalks==4:
        j"Ily... This game is really getting boring."
        i"Blame Zan."
        j"Zan?"
        i"Zan Kizuna."
        j"Who's that?"
        i"Classified Information."
        j"Okay, I've had enough of that answer."
        i"Then why don't you go submit a complaint at {a=http://zankizuna.itch.io/Softwar}The Softwar game page?{/a}"
        j"I'll scold them for all this subpar programming skills."
        i"Just drop an e-mail if you wanna join team Kizuna."
      elif maptalks==5:
        j"What are we even waiting for here anymore?"
        i"The Full version of Softwar."
        j"Wait, you mean we downloaded an incomplete game?"
        i"I thought you knew that already!"
      elif maptalks==6:
        i"If you wanna experience more Softwars, let's go through the doors on the sides!"
        j"I'd rather not."
        i"Let's gooooo!"

      elif maptalks==7:
        j"Have you ever heard of the quote \"Make Love, Not War\"?"
        i"Yes."
        j"Then why were you built exactly to counter this quote?"
        i"I've come to spread that quote to all the warriors out in the battlefield."
        j"Hmmm.. Fair enough."
        $ maptalks = 0
    elif boxsheet == stage1:
      $ maptalks2+=1
      if maptalks2==1:
        j"Ily, what's this other room?"
        i"It's supposed to be the neighboring network to us."
        i"This room is full of viruses."
        j"You're one of them, you know?"
      elif maptalks2==2:
        j"What the heck! So many viruses!"
        i"They're all the same, though.."
        j"This demo is twisted."
        i"Post a complaint at {a=http://zankizuna.itch.io/Softwar}The Softwar game page{/a}!"

      elif maptalks2==3:
        j"Ily... There aren't any other doors here."
        i"Help us code more or be patient."
        j"What do you mean us?"
        i"Oops!"
      elif maptalks2==4:
        i"John! You should be a Patron of Softwar!"
        j"Sure, drop a link."
        i"I also suggest that you join their discord server too!"
        j"Drop a link of that too."
        i"Here it is!  {a=http://discord.gg/yuQfAx3}Team Kizuna Discord{/a} and {a=http://patreon.com/teamkizuna}Team Kizuna Patreon{/a}"
      elif maptalks2==5:
        i"John! Thanks for finishing up to this far."
        j"No problem."
        i"Did you enjoy?"
        j"I guess."
        menu:
          i"Do you want to see the credits now?"
          "YES":
            "See ya."
            $ map_active = False
            return
          "NO":
            "Stay around and play with me more!"
            $ maptalks2 = 0




      show screen mapB
      call screen mapA
      call Returns
      return
    else:
      show screen mapB
      call screen mapA
      call Returns
    return
