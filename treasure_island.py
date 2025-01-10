print(r'''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~____~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("You found a Treasure Island Map")
print("Lets start our Journey !!\nPlease select route to proceed")
direction = input("Right or Left: ").lower()
if direction == "right" or direction == "r":
    print("Game Over, You sink in a hole")
elif not (direction == "left" or direction == "l"):
    print ("Game Over, you choose wrong direction, please rerun the game")
else:
    print("Good Job, You reached the River")
    print("Do you want to Wait for a boat or Swim?")
    commute = input("Please choose Wait or Swim: ").lower()
    if commute == "swim" or commute == "s":
        print("Game Over, You were eaten by crocodiles")
        print(r'''
                     .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                      (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
                                   ''')
    elif  not (commute == "wait" or commute == "w"):
        print("Game Over, you choose wrong method, please rerun the game")
    else:
        print(r'''
         _
            /|\
           /_|_\
         ____|____
         \_o_o_o_/
        ~~ |     ~~~~~
        ___t_________ 
        ''')
        print("Good Job, You reached the Island")
        print("a head of you there is three roads, think wisely before picking")
        road_color = input("Please Choose in which road you wanna continue: Red or Yellow or Blue: ").lower()
        if road_color == "red" or road_color == "r":
            print("Game Over, you were caught in a fire")
            print(r'''
                                  (  .      )
                   )           (              )
                         .  '   .   '  .  '  .
                (    , )       (.   )  (   ',    )
                 .' ) ( . )    ,  ( ,     )   ( .
              ). , ( .   (  ) ( , ')  .' (  ,    )
             (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
        elif road_color == "blue" or road_color == "b":
            print("Game Over, You were lost in a mase")
        elif road_color == "yellow" or road_color == "y":
            print("Good Job, You found your treasure")
            print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
                    ''')
        else:
            print("Game Over, Wrong Option")
    
