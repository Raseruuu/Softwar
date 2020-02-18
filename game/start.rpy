

#########
label start:
    jump demo
    # jump debug_menu
image logo = "gui/logo.png"
image white = Solid("#fff")
image Credits = "gui/Credits.png"
image Maoudamashii = "Maoudamashii.png"
label credits:
    scene white with pixellate
    play music "bgm/Credits_bgm_maoudamashii_8bit08.mp3"

    show logo:
        zoom 0.0 xalign 0.5 yalign 0.5
        linear 0.3 zoom 1.5
        linear 0.3 zoom 1.4
    pause 1.0
    scene Credits with pixellate
    voice "voice/ILY10E - Thank you for playing demo.mp3"
    i"Thank you for playing the Softwar Demo!"
    scene blue with dissolve
    show Folders
    $ direction = 'down'
    show IlyRpg:
        xalign 0.5 yalign 0.4

    show text "We hope you had at least {size=32}a bit{/size} of fun!!":
        xalign 0.5 yalign 0.6
    pause 3.0
    show text "Softwar Demo - End" with dissolve
    pause 3.0
    show text "Say hello to the Softwar Team!" with dissolve
    pause 3.0
    show text "Raseruuu/Zan Kizuna\n\nStory, Programming and Character Art" with dissolve
    pause 3.0
    show text "Arsym\n\nProject Manager, Programmer, GUI, Co-writer" with dissolve
    pause 3.0
    show text "Opa\n\nStory, Co-writer" with dissolve
    pause 3.0
    show text "Kiora001/Julian\n\nCharacter Art, Logo, and Cover Art" with dissolve
    pause 3.0
    show text "patricio_hue2\n\nPromotional Art, CG Art" with dissolve
    pause 3.0
    show text "Gelopsychedelico\n\nPromotional Art, Virus designs" with dissolve
    pause 3.0
    show text "Sayaka Mashiro\n\nIly's Voice" with dissolve
    pause 3.0
    show text "Bunnyvoid\n\n3D Background Art" with dissolve
    pause 3.0
    show text "Maoudamashii.jokersounds.com\n\nBackground Music" with dissolve
    pause 3.0
    show text "The Essential Retro Video Game Sound - Juhani Junkala\n\nSound Effects" with dissolve
    pause 3.0
    show text "Ren'py Visual Novel Engine\n\nVersion "+renpy.version() with dissolve
    pause 3.0
    show text "Tom Rothamel aka Pytom\n\nRen'py Visual Novel Engine" with dissolve
    pause 3.0
    show text "Ren'py Discord Server\n\nSpecial Thanks" with dissolve
    pause 3.0
    show text "AMA Computer College Fairview, Philippines\n\nSpecial Thanks" with dissolve
    pause 3.0
    show text "The original ILOVEYOU VIRUS by Reonel Ramones, Onel De Guzman\n\nSpecial Thanks" with dissolve
    pause 3.0
    hide text
    hide IlyRpg
    $ Ily_p='1'
    $ IlySprite('happy')
    show Ily
    i"Have a Lovely Day, User!"
    # *knock knock*
    # “Mmh…--”
    # *knock knock* 
    # You stand up from your bed. You`re sure that you heard knocks.
    # “What the--
    # Is someone at the door…?”
    # No one.
    # Nor the window. 
    # Or the bathroom. 
    # Or anywhere else.
    # *knock knock* 
    # The knocks were coming from your computer.
    # “Inside...the screen..? *yawn*”
    # *knock knock*
    # You shake your mouse around your mousepad a little to bring your PC to life from sleep mode.
    # The screen lights up, but immediately you notice that something is very wrong. Your desktop background has changed. 
    # “I always kept it on default, the heck is this…?”
    # “Hello, you!”
    # “Aaah! What!?”
    # A...girl?
    # A girl just popped out onto my screen.
    # In panic, I try to press every button on my keyboard, click rapidly with the mouse, shake the screen, but nothing happens.
    # *knock knock*
    # The...girl? The girl inside my monitor knocked against the screen. This makes no sense.
    # “Hey, you.”
    # “W-who are you?
    # “A virus.”
    # Such a nonchalant response. It’s not almost worthy of my dumbstruck reaction.
    # “A virus to destroy my computer? How on Earth did you get past my firewall?”
    # “It was easy. Anyways, I’m not here to destroy your computer. I’m a virus that only spreads one thing.”
    # “What do you--"
    # “Bye bye, remember to spread the love!”
    # *YOU GOT MAIL*
    # I sigh. The girl disappeared. The virus. Malware. Whatever she was.
    # After doing a quick scan with your antivirus, seemingly unharmed, you notice that your computer was back to normal. The only thing out of place was an e-mail you’d received earlier.
    # “What is this? ILOVEYOU? Is this some kind of joke?”
    # As you opened the mail… a happy message greeted you. It said:
    # Hello, you! 
    # This is the Softwar development team!
    # Sorry about that invasion. We made sure that ILY wouldn’t hurt the antivirus too badly! After all, she only spreads love with all her might!
    # Thank you for being interested in Softwar! We truly appreciate your support and wish you all the best! 
    # We sincerely hope that you will keep on supporting us in the future as well.
    # All of us enjoy what we do and hope that that enjoyment is visible through the product known as Softwar!
    # ILY,
    # -Raseruuu
    # -Arsym
    # -Patrick
    # -Opa
    return

















