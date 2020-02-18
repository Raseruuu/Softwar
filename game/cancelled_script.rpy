
    scene blue with dissolve
    j"I'm baack~!"
    show Folders with dissolve:
        xpos 0.5 xalign 0.5 ypos 0.1
    show Ily at center with dissolve:
     zoom 0.5

    i"Welcome back, John! {w}Assistant Virus ILOVEYOU at your service!"
    $ John_m='sad'
    $ John_e = "up"
    $ Ily_p = "0"
    
    i"How was work today?"
    j"Work is alright."
    $ John_m='happy'
    $ John_e = "normal"
    j"I'm a little excited about something else."
    $ Ily_m = 'O'
    $ Ily_e = '1'
    i"What could that be?"
    $ Ily_m = 'frown'
    $ Ily_e = '1'
    j"There's an upcoming hackathon next month.\nI gotta join."
    $ Ily_m = 'happy'

    i"That's great news!"
    $ Ily_m = 'frown'
    i"You should start studying then!"
    j"Yeah. I should."
    i"You wouldn't want to lose against those guys from PH-U!"
    $ John_e = "mad"
    j"There's still a lot of time to prepare."
    i"Next month is a short amount of time. PH-U's gonna win again!!"
    j"Give me a break. {w}Also, stop mentioning PH-U. They hosted the last Hack, and rigged the results."
    $ Ily_m = 'happy'
    $ Ily_e = '1'
    i"PH-U PH-U PH-U PH-U PH-U PH-U PH-U PH-U PH-U PH-U PH-U PH-U PH-U PH-U PH-U {nw}"
    $ John_m = "speak3"
    j"Stoooooop!{w} I've had enough of that University. I'm still bitter that we lost last Hack."
    $ Ily_m = 'frown'
    $ Ily_e = '2'
    i"Are you sure they rigged the results?"
    $ John_m='sad'
    j"There's this girl from the winning team that had an evil look on her face."
    $ Ily_m = 'O'
    $ Ily_e = '1'
    show Ily at bounce
    i"But that doesn't mean anything!{w}\nCould it be that you guys just suck?"
    $ John_m = 'speak3'
    $ John_e = 'mad'
    j"We don't suck!"
    $ Ily_m = 'happy3'
    $ Ily_p = '1'
    i"It's OK, John, I understand."
    $ John_m = 'sad'
    $ John_e = 'mad'
    $ Ily_p = '0'
    j"..."
    $ Ily_m = 'frown'
    $ Ily_e = '2'
    i"I'll say!{w} You better bring me along when you get to hack again!"
    $ Ily_m = 'happy'
    $ Ily_e = '2'
    i"I'll show them some real hacking!"
    $ John_m = 'sad'
    j"No."
    i"Pass me on to your lappy!"
    j"Never! You'll destroy everything."
    $ Ily_m = 'O'
    i"So you can't bring me to the hackathon?"
    ""
    j"I'm afraid not."
    $ Ily_p = '2'
    $ Ily_m = 'happy'
    i"Me being incompatible to every other computer but yours means..."
    $ Ily_p = '2'
    extend"That we're meant to be!{w} It's perfect!{w} The Algorithm of Love!"
    $ Ily_p = '2'
    $ Ily_m = 'frown'
    j"No. I have no interest in cyber-people."
    $ Ily_p = '0'
    $ Ily_e = '1'
    $ Ily_m = 'happy'
    i"I love you, John."
    i"ILOVEYOU-ILOVEYOU-ILOVEYOU-ILOVEYOU-ILOVEYOU-ILOVEYOU-ILOVEYOU-ILOVEYOU-{nw}"
    $ John_m = "speak3"
    j"Stoooooop!"
    $ John_m = "sad"
    j"I refuse to accept love as something people can script or code."
    j"It's more complex than that."
    $ Ily_m = 'midopen'
    i"Oohh, John's talking love~! "
    $ Ily_m = 'happy3'
    $ Ily_p = '1'
    i"Let's get real. {w}Pay no attention to me."
    $ Ily_p = '0'
    i"You should pick someone of the same wavelength. "
    $ Ily_m = 'happy'
    $ Ily_e = '1'
    extend"Like, you know,{w} Lisa."
    $ Ily_m = 'frown'
    $ Ily_e = '2'
    j"Lisa's just a friend.{w} Case closed."
    i"But she's your closest--{nw}"
    j"Let's not talk about this, ok?"
    i"..."
    j"Ily."
    $ Ily_e = '1'

    i"What is it?"
    $ Ily_m = 'O'
    show Mouse:
        xanchor 0.0 yanchor 0.0 xpos 1.0 ypos 0.0
        linear 0.8 xpos 0.5 ypos 0.5
    $ John_m = "happy"
    $ John_e = "mad"    
    j"I need you to move."
    show Mouse:
        linear 0.4 xpos 0.57
    show Ily at rsurprise
    i"wha-- wait!! ee-- You need to studyyyyyy---{nw}"
    show Mouse:
        linear 0.8 xpos 1.0 ypos 0.0
    show Ily at kickedaway
    j"There.{w} Nice.{w} Clear.{w} Screen."
    j"Now I can play."
    "It's always like this.{w} Ever since I downloaded Ily. \n{w}Sure she's a friend, but she's too caring for me."
    "Ily is a Virus.{w} The \"ILOVEYOU\" Virus. An A.I. Virus that has infected my computer.{w} I didn't know such a kind of Virus existed until I met her."
    "I got her through this really shady e-mail last month,{w} whose subject read \"I Love You\".{w} I was a fool,{w} so I opened it."
    "Ily has destroyed countless other computers but spared mine.{w} Maybe because she \"Loves\" me.{w} Or my computer."
    "At first I was scared,{w} but after a while, I've grown to appreciate it.{w} To appreciate her."
    $ Ily_e = '2'
    $ Ily_m = 'frown'
    #$ Ily_p = '0'
    show Ily:
        xpos 1.4 xanchor 0.0 zoom 0.5 rotate -20 yalign 1.0
        linear 15.0 xpos 0.85 
    "I can't delete her after all. She kind of controls the computer now."
    "I don't know what occured upon her maker, that they chose to spare my computer."
    "I don't know if they're supposed to be terrorists that are actually good guys."
    "I don't know if I'm being trapped or set up for something really sinister to happen in the future."
    "I don't know a lot of things."
    i"Hey John!"
    $ Ily_p = '1'
    i"How long are you gonna play?"
    hide Ily with dissolve
    $ Ily_p = '0'
    $ Ily_m = 'O'
    $ Ily_e = '1'
    show Ily at center with dissolve:
     zoom 0.5
    i"I'm bored.{w} You always waste your time playing this same game."
    $ Ily_m = 'frown'
    i"Go talk with me or something."
    $ John_e = "normal" 
    $ John_m = "sad" 
    j"..."
    $ Ily_m = 'happy3'
    j"Ok.{w} I'll stop playing."
    j"Tell me something I don't know." 
    $ Ily_m = 'happy'
    i"Fire away!"
    $ read0 = False
    $ read1 = False
    $ read2 = False
    $ read3 = False
    $ read4 = False
    $readall = False
    $ Else = ""
    label menu1:
        $ John_m = "sad"
        $ John_e = "normal"
        $ Ily_e = "1"
        $ Ily_m = "frown"
        i"What [Else]would you like to know about?"        
        menu:
            "What [Else]would you like to know about?"
            "ILOVEYOU Virus" if not read0:
                $ read0 = True
                $ Else = "else "
                j"Tell me about you, Ily."
                i"Okay. Like, what part of me?"
                j"Your creator.{w} Who are they,{w} where are they from, and why did they make you?"
                $ Ily_m='frown'
                i"I am currently incapable of producing an answer."
                j"I have to know!"
                i"I am currently incapable of producing an answer."
                j"They're definitely terrorists, right?"
                i"I am currently incapable of producing an answer."
                j"Okay, I give up."
                j"Viruses are troublesome."
                i"Of course! lol"
            
            "John Doe" if not read1:
                $ read1 = True
                $ Else = "else "
                j"Tell me something about myself."
                $ Ily_m = 'happy3'
                i"You tell me.{w} Why are you named with such a random name?"
                j"I'm an orphan. That's why."
                $ Ily_m = 'O'
                $ Ily_e = '2'
                i"Orphan...{w} You mean you have no parents?"
                j"Yeah. At some point in my childhood, I lost my memories."
                j"An orphanage person took me in and gave me a regular name."
                $ Ily_m = 'frown'
                $ Ily_e = '2'
                i"Sounds like some drive reformatting happened in you."
                $ Ily_m = 'O'
                $ Ily_e = '2'
                i"We've been together for over a month and you haven't told me this.{w} I thought your parents wer overseas or something."
                j"Nobody ever asks me about my past."
                i"Must be hard being alone.{w=.3}.{w=.3}."
                i"If you need a parent, I can be a mom!"
                j"No thanks.{w} You're a pretty loud mom already."
                j"Hey, it's been over a month already?{w} Since we met?"
                i"Yeah, since my birthday.{w} Do you remember?{w} My debut?"
                j"I'm not a fan of flashbacks, but I thought it was the worst day of my life."
                i"You're so mean!"
                j"Moving on..."

            "Lisa Fairfield" if not read2:
                $ read2 = True
                $ Else = "else "
                j"Since you mentioned her earlier... How has Lisa been lately?"
                $ Ily_e = "2"
                $ Ily_m = "happy"
                i"Hey! You care about her! That's a huge development, John!"
                $ Ily_m = "happy3"
                j"We're just friends, okay?"
                $ Ily_e = "1"
                $ Ily_m = "frown"
                i"Lisa e-mailed you something earlier."
                j"You read it?"
                i"She wanted to remind you about the hackathon, so she sent over some study materials."
                $ Ily_p = '2'
                $ Ily_e = '2'
                $ Ily_m = 'happy'
                i"I'm telling you, John! {w}She's the best gril!{w}\nYou have to trust my Love Algorithm!"
                $ Ily_p = '0'
                j"Show me the e-mail."
            "Softwar" if read3:
                $ read5 = True
                $ Ily_m = 'frown'
                $ Ily_e = '2'
                $ John_e = 'mad'
                j"What is this about \"Softwar\"? {w}Aside from it being a super-pun for Software and War?"
                i"Well you see, my developer made me for 3 main purposes."
                j"..."
                i"1.{w} I'll be a Virus that destroys target computers.{w}\n2.{w} I'll be an Artificial Intelligence Relay Interface (AIRI) for a chosen user."
                i"And 3.{w} I'll be a software battle program, participating in Softwars."
                j"This is new. This Softwar...{w} It's more than just a hackathon?"
                i"The term is defined in my database, as a battle system for software versus software."
                i"There are two Softwars. The hackathon, and the battle system."
                j"What does the battle system do?"
                i"The battle system decides the fate of the computer.{w} Losing softwares get deleted."
                j"Ok. That's harsh.{w} Why does it exist?"
                
                i"As a Virus, My main foe is the Antivirus.{w} My life's purpose after all is to destroy computers."
                j"...{w} Why would I even want to destroy anyone's computer?{w} It's bad."
                i"Well, you could say it's a game..."
                j"It's serious. I don't want to participate in any of these Softwars."
                j"I feel that I'm being set up."
                i""
            "The Hackathon"  if not read3:
                $ read3 = True
                $ Else = "else "
                j"Tell me about the next Hackathon."
                i"Of course."
                $ Ily_m = 'O'
                extend" Aside from your job,{w} hackathons are all you have at gaining your own money."
                $ Ily_m = 'happy'
                i"Just like every hackathon, contestant teams of 2-5 will be programming apps on the spot. {w}\nEach team of \"Hackers\" are to present their app to 3-4 judges every hackathon."
                $ Ily_m = 'O'
                i"If you disappoint the judges, then you lose, and won't be part of the top 3 winning teams."
                i"Your past team, representing ANA University, lost last Hack."
                $ Ily_m = 'happy3'
                j"You didn't have to remind me about that."
                $ Ily_m = 'happy'
                $ Ily_e = '2'
                i"I was just here, but I knew most of what happened!"
                $ Ily_m = 'happy3'
                $ Ily_e = '1'
                j"Back to the topic, Ily." 
                i"I'll get to all the details."
                j"I'd prefer to hear the most important ones, if you may."
                i"Alright."
                $ Ily_e = '2'
                i"The next Hack is entitled \"Softwar\", held in your Alma Mater, ANA Computer University."
                j"The one I'm in is just a college. The university is quite far away."
                i"It's like a home-court battle."
                $ Ily_m = 'frown'
                i"John.{w} This hackathon.{w} The title is kind of familiar to me.{w} It bothers me a little bit."
                j"\"Softwar\"? What about it?"
                i"It's kinda huge to discuss. Let's talk about it later."
                j"Alright."
                $ Ily_m = 'happy3'
                j"Back to the hack..."
                i"You will be facing other teams from many different universities, including PH-U. I'm sure they're looking forward to face you guys again!"
                j"Again with PH-U. What else?"
                i"Well, there are teams from DNSU,{w} STU,{w} ATMU,{w} EU,{w} iUniversity,{w} and so many others."
                i"Top-class universities, if you ask me.{w} Schools for people with lots of money."
                i"I really do admire how popular these other schools are, too.{w} They specialize in many different fields."
                i"STU is known for their long-standing history as the oldest university,{w} iU specializes in graphics and animation,{w} ATMU is all around for the rich kids."
                $ Ily_m = 'happy'
                i"DNSU is--{nw}"
                j"OK, I get it already.{w} They're some really great schools."
                $ Ily_m = 'O'
                i"Meanwhile, despite it being and existing for computers,{w} your college doesn't even support game development,{w} and lacks so much in mobile and web development education.{w} The most important fields!!"
                j"You've already made it clear that our college is--{nw}"
                $ Ily_m = 'frown'
                i"That's why you left school for now, right?"
                j"... {w}I guess you could say that."
                $ Ily_m = 'happy3'
                i"Don't lose hope! There's plenty more time to study!"
                j"... {w}Sure."
                $ Ily_m = 'happy'
                i"Oh!{w} Oh!{w} This is the best part!"
                $ Ily_m = 'happy3'
                extend" The prize for the winner's teams is as follows:{w}\nFor the Third place:{w} 20,000 PHP.{w} \nFor the Second place:{w} 30,000 PHP."
                $ Ily_m = 'happy'
                i"Aaaaand, for the First place:{w} 50,000 PHP!"
                $ Ily_m = 'happy3'
                $ John_m = 'happy'
                j"Big money whichever place we drop into. {w} I didn't know ANA had this much under their sleeves.{w} They're finally giving out some riches."
                $ Ily_m = 'O'
                i"I hope that motivates you enough!"
                show Ily:
                  block:
                    linear 0.2 xoffset 20
                    linear 0.2 xoffset -20
                    repeat 5
                  pause 0.05
                  linear 0.15 xoffset 0     
                i"{size=+10} M O T I V A T I O N ! ! ! ! !{/size}"
                $ John_m = 'sad'
                j"How do we win?{w} Do you have any clues about what kind of apps they're gonna let us make?"
                $ Ily_m = 'frown'
                i"Well, the theme will be announced on the event itself."
                $ Ily_m = 'midopen'
                i"So... We can either try to predict the future, "
                $ Ily_m = 'happy'
                extend"or {i}literally{/i} hack them and skim their database for the event plan.{w} It's a hackathon, right?"
                $ John_e = 'up'
                j"That's{w=.3}.{w=.3}.{w=.3}.{w=.3}"
                $ John_e = 'mad'
                $ John_m = 'sad'
                extend" You can do that?!"
                show Ily at sway
                i"Well of course!"
                j"That's cheating. Your suggestions are ridiculous."
                i"I love ridiculous!"
        if (read0 and read1) and (read2 and read3):         
            $ readall = True
        if not readall: 
            jump menu1
    j"I guess that finishes our short discussion."
    i"Thank you for your time, John! We should do this more often."
    