#-- Developer: Thomas Farias
#-- Date: 6/13/2020
#-- Program Name: Growth Mindset Game

#Global imports
import random

#- Functions

def clear():
  print("\n" * 100)
#done
def intro():
  intro_options = ["1","2","3"]
  user_input = ""
  while user_input not in intro_options:
    print(r"""

                                   %%%%#     ,.,                                
                                   #%%%%%#.                                     
                                   %#########                                   
                                  (##########*                                  
                                 (###########/ (                                
                                ####      ###   ##                              
                              ,####       /##   /##                             
                            .#######*    ###     ((#                            
                          .#########((((#        ((((                           
                        *####                    /(((/                          
                      /#*    .((((((             .((((                          
                    ,##(#(((((((((((((            ((((  (                       
                   ###((((((((((((((((.           (((/ ((((                     
                  ##((((((((((((((((((            (// ((((((                    
                 ((((((((((((((((((((            ,///////////                   
                .((((((((((((((((((#      /.     ////////////.                  
                ,((((((((((((((((#    .////      /////////////                  
                .((((((((((((((, ./////////     /////////////*                  
                 (((((((((((((////////////#     /////////////                   
                 ,((((((((((((////////////*    /////////////*                   
                  ,(((((((((//////////////    /////////////*                    
                    ((((((((/////////////#   //*******////                      
                      (((((//////////////   /***********.                       
                        (((/////////////# .///******/*                          
                           ,///////////( //////**/*                             
                                 ,//////////,     
                                                   """)
    print(''' \n \n Welcome to The Growth Mindset Text Based Adventure Game.   
  
    1) Start 
    2) Instructions
    3) Credits
    ''')

    user_input = str(input(" What would you like to do? \n"))
    if user_input == intro_options[0]:
      thestart()
    if user_input == intro_options[1]:
      instructions()
    if user_input == intro_options[2]:
      credits()
  
#done
def instructions():
  instructions_options = ["r"]
  user_input = ""
  while user_input not in instructions_options:
    print(''' \n \n In this game, you take on the role of a recent high school graduate, and must use a growth mindset to navigate their life. Type a '1', '2', or '3' on every screen which corresponds to the path you'd like to take.
    ''')

    user_input = str(input("Type 'r' to return"))
  print ("You have selected option " + user_input + ".")
  if user_input == instructions_options[0]:
    intro()
#done
def credits():
  credits_options = ["r"]
  user_input = ""
  while user_input not in credits_options:
    print(''' 
    Creator: Thomas Farias
    Art: https://www.asciiart.eu/
         https://asciiart.website/
    ''')

    user_input = str(input("Type 'r' to return"))
  print ("You have selected option " + user_input + ".")
  if user_input == credits_options[0]:
    intro()
#done
def thestart():
  thestart_options = ["1","2","3"]
  user_input = ""
  while user_input not in thestart_options:
    print                 (r"""
                    
                       .odbo.
                  .od88888888bo.      
              .od8888888888888888bo.
          .od888888888888888888888888bo.
        od88888888888888888888888888888888bo
        `~888888888888888888888888888888~'
            `~888888888888888888888888~'|
               `~888888888888888888~'   |
                |`~888888888888~'|     |
                 \   `~888888~'   /     A
                  `-_   `~~'   _-'      H
                     `--____--
                     
                     """)
    print(''' \n \n    You have just graduated high school. You were never interested in excelling in your academics and made Cs and 
    Ds. It's now time to decide whether or not you want to go to college, but your limited academic performance 
    leaves you with very limited options.
  
    1) I can't go to college. I'm not good enough. I heard the local fast food joint has an opening.
    2) I'm going to try to enroll in the local community college. I’m not confident I can get into a four year 
    university, but maybe if I work hard enough I will eventually.
    3) I’m going to try to enroll in my local four year university. I’m confident that if I apply myself, I can succeed.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected option " + user_input + ".")
  if user_input == thestart_options[0]:
    fastfood()
  elif user_input == thestart_options[1]:
    comcol()
  elif user_input == thestart_options[2]:
    randomu()
#done
def theend():
  theend_options = ["e"]
  user_input = ""
  while user_input not in theend_options:
    print                 (r"""
                    
  ______ _            ___               
 (_) |  | |          / (_)           |  
     |  | |     _    \__   _  _    __|  
   _ |  |/ \   |/    /    / |/ |  /  |  
  (_/   |   |_/|__/  \___/  |  |_/\_/|_/

                     """)
    user_input = str(input("Type 'e' to exit"))
  print ("")
  if user_input == theend_options[0]:
    secret()
#done
def secret():
  ("This is here because I may not entirely know what I'm doing")
#done
def randomu():
    flip = random.randint(1,2)

    if flip == 1:
        random_options = ["1","2"]
        user_input = ""
        while user_input not in random_options:
          print(r"""
                                           
                                                  
      _____         _____                 
    ,'     `.     \/,---<                
   /         \    ( )@ @(      _         
  |           \    C __>/    |/ )       
  | What Now?  >--  \\//     |_/     
  |           /   ,- >o<-.__/ /        
   \         /   /   \/  ____/       
    `._____,'   / /|  | |            
               / '--/_| |             
               `----\_) |             
                   |____|              
                   |  | |                 
                   |  | |              
                   |  | |                  
                   |__|_|_                
                   (____)_)                
          
          """)
          print (''' \n Unfortunately, the university did not accept your application. You have been referred to the local community college, where you would spend two years before being accepted to the university.
        
          1) This was a bad idea. Maybe I should just get a job at the local fast food place.
          2) Community college it is.

          ''')

          user_input = str(input("What will you do?"))
        print ("You have selected" + user_input)
        if user_input == random_options[0]:
          fastfood()
        elif user_input == random_options[1]:
          comcol()
    elif flip == 2:
        uni()
#done
def random2():
    flip2 = random.randint(1,2)

    if flip2 == 1:
        random2_options = ["1","2"]
        user_input = ""
        while user_input not in random2_options:
          print(r"""
          
          
      _____         _____                 
    ,'     `.     \/,---<                
   /         \    ( )@ @(      _         
  |           \    C __>/    |/ )       
  |  Time to   >--  \  /     |_/     
  |  give up? /   ,- >o<-.__/ /        
   \         /   /   \/  ____/       
    `._____,'   / /|  | |            
               / '--/_| |             
               `----\_) |             
                   |____|              
                   |  | |                 
                   |  | |              
                   |  | |                  
                   |__|_|_                
                   (____)_)      
          
          """)
          print (''' \n Unfortunately, you did not get the job.
        
          1) This was a bad idea. I'm going to keep my current job.
          2) Community college doesn't sound too bad.

          ''')

          user_input = str(input("What will you do?"))
        print ("You have selected" + user_input)
        if user_input == random2_options[0]:
          ff03_1()
        elif user_input == random2_options[1]:
          comcol()
    elif flip2 == 2:
        ff03_3real()   
#done
def random3():
    flip3 = random.randint(1,2)

    if flip3 == 1:
        random3_options = ["1","2"]
        user_input = ""
        while user_input not in random3_options:
          print (r"""
          
      _____         _____                 
    ,'     `.     \/,---<                
   /         \    ( )@ @(      _         
  | What kind \    C __>/    |/ )       
  | of mindset >--  \\//     |_/     
  | do I have?/   ,- >o<-.__/ /        
   \         /   /   \/  ____/       
    `._____,'   / /|  | |            
               / '--/_| |             
               `----\_) |             
                   |____|              
                   |  | |                 
                   |  | |              
                   |  | |                  
                   |__|_|_                
                   (____)_)      
          
          """)
          print (''' \n Unfortunately, you didn't find a job.
        
          1) Maybe I wasn't really meant for this. I quit.
          2) This is alright. I'll stick with what I have.

          ''')

          user_input = str(input("What will you do?"))
        print ("You have selected" + user_input)
        if user_input == random3_options[0]:
         cc02_1() 
        elif user_input == random3_options[1]:
         cc02_2()
    elif flip3 == 2:
        cc02_3_good()
#done





def fastfood():
  fastfood_options = ["1","2","3"]
  user_input = ""
  while user_input not in fastfood_options:
    print                 (r""" 
                           
                            |\ /| /|_/|
                          |\||-|\||-/|/|
                           \\|\|//||///
          _..----.._       |\/\||//||||
        .'     o    '.     |||\\|/\\ ||
       /   o       o  \    | './\_/.' |
      |o        o     o|   |          |
      /'-.._o     __.-'\   |          |
      \      `````     /   |          |
      |``--........--'`|    '.______.'
       \              /
     `'----------'`
     
     """)
    print(''' \n \n You have gotten a job as a minimum wage employee at a local fast food chain. The pay is just barely enough to get by, and you have nothing to show for it but your shabby apartment. You  work there for a few years, hating your job and resenting the way your life is going. One day, you are offered a promotion to assistant manager.   
  
    1) I don't think I'm management material. Back to flipping burgers. 
    2) I think I made a mistake in not going to college. I'm gonna try again.
    3) I have to take advantage of this opportunity. I have no management experience,
    but I can learn, and I'm confident I'll do a great job.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == fastfood_options[0]:
    ff01()
  elif user_input == fastfood_options[1]:
    ff02()
  elif user_input == fastfood_options[2]:
    ff03()
#done
def ff01():
  ff01_options = ["1","2"]
  user_input = ""
  while user_input not in ff01_options:
    print                 (r""" 
                           
                             
              _.-"''-._
           /.-......-.\
          //          \\
          ||          ||
          ||.--    --.||
          /| (.)||(.) |\
          \    (__)    /
           |   ____   |
            \ /____\  /
         _./`'.____.'`\._
     _.::::|  |    |  |::::._
   .::::::::\  \  /  /::::::::.
  /::::::::::|/:\/:\|::::::::::\    

     """)
    print(''' \n \n You decided to decline the promotion to assisstant manager, and are not sure where to go from here.   
  
    1) I don't think I can take this anymore. I'm done! 
    2) There's always community college.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff01_options[0]:
    cc02_1()
  elif user_input == ff01_options[1]:
    comcol()
#done

def ff02():
  comcol()
#done

def ff03():
  ff03_options = ["1","2","3"]
  user_input = ""
  while user_input not in ff03_options:
    print                 (r""" 
     
     /:""|       
     |: 66|_     
     C     _)    
      \ ._|      
       ) /        
      /`\\        
     || |Y|           
     :| |=:     
     ||_|,|    
     \)))||    
  |~~~`-`~~~|  
  |         |    
  |_________|      
  |_________|       
      | ||         
      |_||__      
   (____))    

                            """)
    print(''' \n \n You have accepted a position as the assistant manager at the restuarant. The pay is not minimum wage, but you still feel like this is not the way your life is supposed to be. After a couple years in the position, you feel like you want something more.

    1) I'm doomed. I'm going to stay where I am. 
    2) I feel like maybe I made a mistake in deciding not to go to college. I'm going to try to enroll in community college.
    3) There's a position open in the corporate offices. It doesn't seem likely, but maybe I can get it. 
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff03_options[0]:
    ff03_1()
  elif user_input == ff03_options[1]:
    comcol()
  elif user_input == ff03_options[2]:
    ff03_2()
#done
def ff03_1():
  ff03_1_options = ["1","2"]
  user_input = ""
  while user_input not in ff03_1_options:
    print                 (r""" 
     
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
        \      _/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|             

                            """)
    print(''' \n \n You decide you're doomed to stay where you are, as you're fixed mindset takes over again. 

    1) This just proves my point. I'm trapped here forever. 
    2) Maybe I've made a mistake. Community college is always an option.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff03_1_options[0]:
    ff03_11()
  elif user_input == ff03_1_options[1]:
    comcol()
#done  
def ff03_11():
  ff03_11_options = ["1","2"]
  user_input = ""
  while user_input not in ff03_11_options:
    print                 (r""" 
     
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
        \ /___\_/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|             

                            """)
    print(''' \n \n You reinforce your old fixed mindset, and as retirement approaches you have one last chance. 

    1) I can't do this anymore. I quit! 
    2) Maybe it's time I take responsiblity for my life, and believe in myself again.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff03_11_options[0]:
    cc02_1()
  elif user_input == ff03_11_options[1]:
    ff03_12()
#done
def ff03_12():
  ff03_12_options = ["1","2"]
  user_input = ""
  while user_input not in ff03_12_options:
    print                 (r""" 
                                    
        .-'--.
      .'      '.
     /     _    `-.
    /      .\-     \,  ,
   ;       .-|-'    \####,
   |,       .-|-'    ;####
  ,##         `     ,|###"
    #,####, "#,        ,#|^;#
  `######  `#####,|##" |`)|
  `#####    ```o\`\o_.| ;\
   (-`\#,    .-'` |`  : `;
    `\ ;\#,         \   \-'
      )( \#    C,_   \   ;
     (_,  \  /   `'./   |
       \  / | .-`'--'`. |
     | ( \   ,  /_,  |
         \    `   ``     /
          '-.__     // .'
              `'`.__.'   
 
                           """)
    print(''' \n \n Despite you're life-long fixed mindset, a final push at the end of your career allows you to retire a bit mroe satisfied with your career.   
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff03_12_options[0]:
    intro()
  elif user_input == ff03_12_options[1]:
    theend()
#done 
def ff03_2():
  random2()
#done
def ff03_3real():
  ff03_3real_options = ["1","2"]
  user_input = ""
  while user_input not in ff03_3real_options:
    print                 (''' 
      
            ;c =\
          __|  _/
        .'-'-._/-'-._
       /..   ____    \
      /' _  [<_->] )  \
     (  / \--\_>/-/'._ )
      \-;_/\__;__/ _/ _/
       '._}|==o==\{_\/
        /  /-._.--\  \_
       // /   /|   \ \ \
      / | |   | \;  |  \ \
     / /  | :/   \: \   \_\
    /  |  /.'|   /: |    \ \
    |  |  |--| . |--|     \_\
    / _/   \ | : | /___--._) \
   |_(---'-| >-'-| |       '-'
          /_/     \_\

 ''')
    print(''' \n \n Congratulations! You have gotten a job in the corporate offices of the fast food chain. You will go on to hold this steady job for a number of years.  
    1) Time to coast. This is as good as it's gonna get. 
    2) I feel like I can climb even higher!
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff03_3real_options[0]:
    ff03_3real_1()
  elif user_input == ff03_3real_options[1]:
    ff03_3real_2()
#done
def ff03_3real_1():
  ff03_3real_1_options = ["1","2"]
  user_input = ""
  while user_input not in ff03_3real_1_options:
    print                 (r""" 
      
         ____________________________\`-._
                                     /.-'

 """)
    print(''' \n \n You decide you're done advancing, and are content to stick with your current job.  
    1) I'm done. Just a few more years. 
    2) I think I might have been wrong. I want to go higher.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff03_3real_1_options[0]:
    ff03r1()
  elif user_input == ff03_3real_1_options[1]:
    ff03r2()
#done
def ff03r1():
  ff03r1_options = ["1","2"]
  user_input = ""
  while user_input not in ff03r1_options:
    print                 (r"""     
         
        ,%&& %&& %
       ,%&%& %&%& %&
      %& %&% &%&% % &%
     % &%% %&% &% %&%&,
     &%&% %&%& %& &%& %
    %%& %&%& %&%&% %&%%&
    &%&% %&% % %& &% %%&
    && %&% %&%& %&% %&%'
     '%&% %&% %&&%&%%'%
      % %& %& %&% &%%
        `\%%.'  /`%&'
          |    |            /`-._           _\\/
          |,   |_          /     `-._ ..--~`_
          |;   |_`\_      /  ,\\.~`  `-._ -  ^
          |;:  |/^}__..-,@   .~`    ~    `o ~
          |;:  |(____.-'     '.   ~   -    `    ~
          |;:  |  \ / `\       //.  -    ^   ~
          |;:  |\ /' /\_\_        ~. _ ~   -   //-
     \\/;:   \'--' `---`           `\\//-\\///
                       
                           """)
    print(''' \n \n You have reached retirement. You have enough money to live off of, and despite being stagnant late in your career, you're glad you didn't resign yourself to flipping burgers. 
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff03r1_options[0]:
    intro()
  elif user_input == ff03r1_options[1]:
    theend()
#done
def ff03r2():
  ff03r2_options = ["1","2"]
  user_input = ""
  while user_input not in ff03r2_options:
    print                 (r"""     
         
           ////////\\\  
         // __   __ \\ 
        // (()) (()) \\
       (_    (___)    _)
         \  \_____/  /
          `-._   _.-'
          __.-)_(-,__ 
       ./'  \_\_/_/  `\.
      / >   | //\ |   < \
     /  \   | |/| |   /  \
    /   |\  | |/| |  /|   \
   /   /| \ | |/| | / |\   \
  (   ( |  \| |/| |/  | )   )
   \   \|   Y |/| Y   |/   /
    \   |  o| |/| |-  |   /
     `\ |   | `^` |   | /'
       `|  o|=[Ll=|-  |'
        |   /     \   |
        ~~|`  \    `|~~
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |____|____|
          /   / \   \
         /   /   \   \
        `---'     `---`  
                       
                           """)
    print(''' \n \n You decide to try an climb a bit higher in the company, and it works. You retire a bit unsatisfied with your career choices, but satisfied you used your growth mindset to go far. 
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff03r2_options[0]:
    intro()
  elif user_input == ff03r2_options[1]:
    theend()
#done
def ff03_3real_2():
  ff03_3real_2_options = ["1","2"]
  user_input = ""
  while user_input not in ff03_3real_2_options:
    print                 (r""" 
      
                        i i'
                         \~;\
                          \; \
                           \ ;\    ====
                            \ ;\  ==== \
                       __,--';;;\-' (  0
                 __,--';;; ;;; ;;\      >
          __,--'\\ ;;; ;;; ;;; ;;;\--__<
   _ _,--' __,--'\\  ;;; __,~~' \ ;\
  (_)|_,--' __,--'\\;,~~'        \ ;\
  |(_)|_,--'       ~~             \; \
  || |                             \ ;\
   |_/                              !~!,
                                .---'''---.
                                |         |
                                |         |
                                |         |
                                `---------'

 """)
    print(''' \n \n You decide you want to continue to climb the ladder at your company, and it has gone well. You are approaching retirement.  
    1) I'm done! I've done all I can. 
    2) I'm not stopping until the end!
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff03_3real_2_options[0]:
    ff033r1()
  elif user_input == ff03_3real_2_options[1]:
    ff033r2()
#done
def ff033r1():
  ff033r1_options = ["1","2"]
  user_input = ""
  while user_input not in ff033r1_options:
    print                 (r"""     
         
        ,%&& %&& %
       ,%&%& %&%& %&
      %& %&% &%&% % &%
     % &%% %&% &% %&%&,
     &%&% %&%& %& &%& %
    %%& %&%& %&%&% %&%%&
    &%&% %&% % %& &% %%&
    && %&% %&%& %&% %&%'
     '%&% %&% %&&%&%%'%
      % %& %& %&% &%%
        `\%%.'  /`%&'
          |    |            /`-._           _\\/
          |,   |_          /     `-._ ..--~`_
          |;   |_`\_      /  ,\\.~`  `-._ -  ^
          |;:  |/^}__..-,@   .~`    ~    `o ~
          |;:  |(____.-'     '.   ~   -    `    ~
          |;:  |  \ / `\       //.  -    ^   ~
          |;:  |\ /' /\_\_        ~. _ ~   -   //-
     \\/;:   \'--' `---`           `\\//-\\///
                       
                           """)
    print(''' \n \n You have reached retirement. You have enough money to live off of, and despite being stagnant in the middle of your career, you're glad you didn't resign yourself to flipping burgers. 
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff033r1_options[0]:
    intro()
  elif user_input == ff033r1_options[1]:
    theend()
#done
def ff033r2():
  ff033r2_options = ["1","2"]
  user_input = ""
  while user_input not in ff033r2_options:
    print                 (r"""     
         
           ////////\\\  
         // __   __ \\ 
        // (()) (()) \\
       (_    (___)    _)
         \  \_____/  /
          `-._   _.-'
          __.-)_(-,__ 
       ./'  \_\_/_/  `\.
      / >   | //\ |   < \
     /  \   | |/| |   /  \
    /   |\  | |/| |  /|   \
   /   /| \ | |/| | / |\   \
  (   ( |  \| |/| |/  | )   )
   \   \|   Y |/| Y   |/   /
    \   |  o| |/| |-  |   /
     `\ |   | `^` |   | /'
       `|  o|=[Ll=|-  |'
        |   /     \   |
        ~~|`  \    `|~~
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |____|____|
          /   / \   \
         /   /   \   \
        `---'     `---`  
                       
                           """)
    print(''' \n \n You decide to try an climb a bit higher in the company, and it works. You retire a bit unsatisfied with your career choices, but satisfied you used your growth mindset to go so far. 
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ff033r2_options[0]:
    intro()
  elif user_input == ff033r2_options[1]:
    theend()
#done


def comcol():
  comcol_options = ["1","2","3"]
  user_input = ""
  while user_input not in comcol_options:
    print                 (r"""                       
       _______________________
      |\_____________________/|
      ||                     ||
      ||  _       _          ||
      || / )     / ) __  |_| ||
      ||  /  -|-  /  --    | ||
      || `==     `==       ' ||
      ||              _____  ||
      ||______________#####__||
      |/_____________________\|              
                           
                           """)
    print(''' \n \n You have just enrolled in the local community college. You are here seeking a better life with the hope of getting into a four-year university.    
  
    1) Time to coast! Community College should be a breeze. Go Human Beings! 
    2) I'm gonna try a bit, but I'm upset about my situation, and won't try as hard as I can.
    3) I'm gonna work hard to get into the university. I may not have succeeded in school in the past, but I can do it if I apply myself.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == comcol_options[0]:
    cc01()
  elif user_input == comcol_options[1]:
    cc02()
  elif user_input == comcol_options[2]:
    cc03()
#done
def cc01():
  print ("\n Your mindset held you back, and you eventually wind up falling out of school. Minimum wage it is. \n")
  fastfood()
#done
def cc02():
  cc02_options = ["1","2","3"]
  user_input = ""
  while user_input not in cc02_options:
    print                 (r"""     
           
               .---[[__]]----.
              ;-------------.|       ____
              |             ||   .--[[__]]---.
              |             ||  ;-----------.|
              |             ||  |           ||
              |_____________|/  |           ||
                                |___________|/
                           
                           """)
    print(''' \n \n You have just graduated community college barely scraping by, and you decide you're done and that it's time to get a job. You manage to get a job that you hate, but it pays the bills.   
  
    1) I can't do this. I quit!  
    2) I hate this career, but I cant do any better. Time to double down and try to make it where I am.
    3) This isn't what I want to do with my life. I'm going to look for a better job.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == cc02_options[0]:
    cc02_1()
  elif user_input == cc02_options[1]:
    cc02_2()
  elif user_input == cc02_options[2]:
    cc02_3()
#done
def cc02_1():
  cc02_1_options = ["1","2"]
  user_input = ""
  while user_input not in cc02_1_options:
    print(r"""
                      ,____
                      |---.\
              ___     |    `
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
     /         \  |
       (_.-.__.__./  /

  """)
    print(''' \n \n You quit your job, and never really manage to find anything better, mostly on account of your aversion to even trying. You live out the rest of your days without a permanent home, bouncing from place to place and cursing your bad luck, instead of your fixed mindset.   
  
    1) Restart  
    2) End Game
    ''') 

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == cc02_1_options[0]:
    intro()
  elif user_input == cc02_1_options[1]:
    theend()
#done
def cc02_2():
  cc02_2_options = ["1","2"]
  user_input = ""
  while user_input not in cc02_2_options:
    print                 (r""" 
                               
    ____________________________\`-._
                                /.-'
                   
                           """)
    print(''' \n \n You have decided to double down and hold your job. You aren't the happiest, but you manage to make a good income. As the years fly by, you're offered yet again another opportunity to advance.  
  
    1) I've made it this far, might as well stay. 
    2) Maybe it's time I started to believe in myself.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == cc02_2_options[0]:
    cc02_2_1()
  elif user_input == cc02_2_options[1]:
    cc02_2_2()
#done
def cc02_2_1():
  cc02_2_1_options = ["1","2"]
  user_input = ""
  while user_input not in cc02_2_1_options:
    print                 (''' 
                           
        .-'--.
      .'      '.
     /     _    `-.
    /      .\-     \,  ,
   ;       .-|-'    \####,
   |,       .-|-'    ;####
  ,##         `     ,|###"
    #,####, "#,        ,#|^;#
  `######  `#####,|##" |`)|
  `#####    ```o\`\o_.| ;\
   (-`\#,    .-'` |`  : `;
    `\ ;\#,         \   \-'
      )( \#    C,_   \   ;
     (_,  \  /   `'./   |
       \  / | .-`'--'`. |
     | ( \   ,  /_,  |
         \    `   ``     /
          '-.__     // .'
              `'`.__.'
          
                           ''')
    print(''' \n \n You have reached retirement. You have enough money to live off of, but you find yourself regretting all the decisions you've made.  
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == cc02_2_1_options[0]:
    intro()
  elif user_input == cc02_2_1_options[1]:
    theend()
#done
def cc02_2_2():
  cc02_2_2_options = ["1","2"]
  user_input = ""
  while user_input not in cc02_2_2_options:
    print                 (r"""     
         
        ,%&& %&& %
       ,%&%& %&%& %&
      %& %&% &%&% % &%
     % &%% %&% &% %&%&,
     &%&% %&%& %& &%& %
    %%& %&%& %&%&% %&%%&
    &%&% %&% % %& &% %%&
    && %&% %&%& %&% %&%'
     '%&% %&% %&&%&%%'%
      % %& %& %&% &%%
        `\%%.'  /`%&'
          |    |            /`-._           _\\/
          |,   |_          /     `-._ ..--~`_
          |;   |_`\_      /  ,\\.~`  `-._ -  ^
          |;:  |/^}__..-,@   .~`    ~    `o ~
          |;:  |(____.-'     '.   ~   -    `    ~
          |;:  |  \ / `\       //.  -    ^   ~
          |;:  |\ /' /\_\_        ~. _ ~   -   //-
     \\/;:   \'--' `---`           `\\//-\\///
                       
                           """)
    print(''' \n \n You have reached retirement. You have enough money to live off of, and despite your insatisfaction with your career, you're glad you at least got to make it far in your field. Time to relax. 
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == cc02_2_2_options[0]:
    intro()
  elif user_input == cc02_2_2_options[1]:
    theend()
#done
def cc02_3():
  random3()
#done
def cc02_3_good():
  ccgood_options = ["1","2"]
  user_input = ""
  while user_input not in ccgood_options:
    print                 (r""" 
                           
              _.-"''-._
           /.-......-.\
          //          \\
          ||          ||
          ||.--    --.||
          /| (.)||(.) |\
          \    (__)    /
           |  ,____,  |
            \  `--'  /
         _./`'.____.'`\._
     _.::::|  |    |  |::::._
   .::::::::\  \  /  /::::::::.
  /::::::::::|/:\/:\|::::::::::\    
                           
                           """)
    print(''' \n \n You've managed to find another a job that you like. You're happier, and find so much more satisfaction from this job than from your other one. What's left?
  
    1) I'm happy, and don't think I can do much more. I'm sticking with this. 
    2) Time to continue climbing. I can do it!
    ''')
    
    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == ccgood_options[0]:
    ccgood_1()
  elif user_input == ccgood_options[1]:
    ccgood_2()
#done
def ccgood_1():
  cc02_2_2_options = ["1","2"]
  user_input = ""
  while user_input not in cc02_2_2_options:
    print                 (r""" 
                                 
          ////////\\\  
         // __   __ \\ 
        // (()) (()) \\
       (_    (___)    _)
         \  \_____/  /
          `-._   _.-'
          __.-)_(-,__ 
       ./'  \_\_/_/  `\.
      / >   | //\ |   < \
     /  \   | |/| |   /  \
    /   |\  | |/| |  /|   \
   /   /| \ | |/| | / |\   \
  (   ( |  \| |/| |/  | )   )
   \   \|   Y |/| Y   |/   /
    \   |  o| |/| |-  |   /
     `\ |   | `^` |   | /'
       `|  o|=[Ll=|-  |'
        |   /     \   |
        ~~|`  \    `|~~
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |____|____|
          /   / \   \
         /   /   \   \
        `---'     `---`  
                           
                           """)
    print(''' \n \n You have reached retirement. You were satisfied with the way you're life turned out, and though you're retirement isn't as big as it could be you're happy. 
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == cc02_2_2_options[0]:
    intro()
  elif user_input == cc02_2_2_options[1]:
    theend()
#done
def ccgood_2():
  cc02_2_2_options = ["1","2"]
  user_input = ""
  while user_input not in cc02_2_2_options:
    print                 (r"""                     
                  
                       \_\
                      /`  )
                     /   (
                    /      \
                   /
                  /
                 /
                /
               /
              /
         (}  /
        /|\_/
        \|
         |\
         / |
                           
                           """)
    print(''' \n \n You have reached retirement. You were satisfied with the way you're life turned out, you have a really nice retirement, and you're happy. 
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == cc02_2_2_options[0]:
    intro()
  elif user_input == cc02_2_2_options[1]:
    theend()
#done
def cc03():
  print ("\n Congrats! The University has accepted you \n")
  uni()
#done




def uni():
  uni_options = ["1","2","3"]
  user_input = ""
  while user_input not in uni_options:
    print                 (''' 
                                      
                                                  .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
                           
                           ''')
    print(''' \n \n Congratulations! You have just been accepted into the local university. What happens next depends on you.    
  
    1) Maybe I really wasn't meant for this. I'm gonna try to coast, and maybe I'll make it through. 
    2) I don't know if I can do it or not, so I'm gonna do the bare minimum to stay afloat in my classes.
    3) It's time to pursue my dream major. I know I can do it, and I'm gonna work as hard as I can to get there.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == uni_options[0]:
    u01()
  elif user_input == uni_options[1]:
    u02()
  elif user_input == uni_options[2]:
    u03()
#done
def u01():
  print('''
  You didn't apply yourself and dropped out of school. The Golden Arches await. \n
  ''')
  fastfood()
#done

def u02():
  u02_options = ["1","2","3"]
  user_input = ""
  while user_input not in u02_options:
    print                 (r""" 
                           
         |""-..._____
     '-.____    _````''''''`|
         \  ``` ``"---... _ |
         |              /  /#\
         }--..______..-{   ###
        }}}}} _   _ {{{{{
        }}}}  6   6  {{{{
       {{{{{    ^    }}}}}
      {{{{{{\  -=-  /}}}}}}
      {{{{{{{;.___.;}}}}}}}
       {{{{{{{)   (}}}}}}}'
        `""'"':   :'"'"'`
                           
                           """)
    print(''' \n \n Congratulations! You graduated from university, and despite the fact that you didn't really apply yourself, you still have some good job opportunities.    
  
    1) Of course I barely graduated! That's just how I am! Time to take a job I can actually do! 
    2) It's not gonna get any better than this. Might as well stick with it and find a mediocre job.
    3) Maybe I didn't apply myself in college, but you can be sure I'm gonna do it at my job.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_options[0]:
    fastfood()
  elif user_input == u02_options[1]:
    u02_1()
  elif user_input == u02_options[2]:
    u02_2()
#done

def u02_1():
  u02_1_options = ["1","2","3"]
  user_input = ""
  while user_input not in u02_1_options:
    print                 (r""" 
             __-----__
       ..;;;--'~~~`--;;;..
     /;-~IN GOD WE TRUST~-.\
    //      ,;;;;;;;;      \\
  .//      ;;;;;    \       \\
  ||       ;;;;(   /.|       ||
  ||       ;;;;;;;   _\      ||
  ||       ';;  ;;;;=        ||
  ||LIBERTY | ''\;;;;;;      ||
   \\     ,| '\  '|><| 1995 //
    \\   |     |      \  A //
     `;.,|.    |      '\.-'/
       ~~;;;,._|___.,-;;;~'
           ''=--'                
                           """)
    print(''' \n \n You stick to your plan and find a mediocre job. You aren't too happy, but it's enough to live comfortably.    
  
    1) I can't take this job. I quit! 
    2) Well I've worked here for this long. I've already peaked, time to double down.
    3) I may not have gotten the job I've always wanted, but I'm going to work hard to climb the ladder.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_1_options[0]:
    cc02_1()
  elif user_input == u02_1_options[1]:
    u02_1_1()
  elif user_input == u02_1_options[2]:
    u02_1_2()
#done
def u02_1_1():
  u02_1_1_options = ["1","2","3"]
  user_input = ""
  while user_input not in u02_1_1_options:
    print                 (r""" 
     
   +8-=-=-=-=-=-8+
   | ,.-'"'-., |
   |/         \|
   |\:.     .:/|
   | \:::::::/ |
   |  \:::::/  |
   |   \:::/   |
   |    ):(    |
   |   / . \   |
   |  /  .  \  |  
   | /   .   \ |
   |/   .:.   \|
   |\.:::::::./|
   | '--___--' |
   +8-=-=-=-=-=-8+
                           
                           """)
    print(''' \n \n You have decided to stick to your current job, and you're approaching retirement, though with a fairly low life satisfaction.    
  
    1) Almost there! 
    2) I think it's time I adopted a growth mindset.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_1_1_options[0]:
    u02_r1()
  elif user_input == u02_1_1_options[1]:
    u02_r2()
#done
def u02_r1():
  u02_r1_options = ["1","2"]
  user_input = ""
  while user_input not in u02_r1_options:
    print                 (r""" 
     
        .-'--.
      .'      '.
     /     _    `-.
    /      .\-     \,  ,
   ;       .-|-'    \####,
   |,       .-|-'    ;####
  ,##         `     ,|###"
    #,####, "#,        ,#|^;#
  `######  `#####,|##" |`)|
  `#####    ```o\`\o_.| ;\
   (-`\#,    .-'` |`  : `;
    `\ ;\#,         \   \-'
      )( \#    C,_   \   ;
     (_,  \  /   `'./   |
       \  / | .-`'--'`. |
     | ( \   ,  /_,  |
         \    `   ``     /
          '-.__     // .'
              `'`.__.'   

                           """)
    print(''' \n \n You have reached retirement. You have enough money to live on, but you have many regrets regarding your career path.    
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_r1_options[0]:
    intro()
  elif user_input == u02_r1_options[1]:
    theend()
#done
def u02_r2():
  u02_r2_options = ["1","2"]
  user_input = ""
  while user_input not in u02_r2_options:
    print                 (r""" 
     
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        | \___/ |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|  

                           """)
    print(''' \n \n You have reached retirement. Though it happened late in your career, you managed to climb the ladder a little bit and secure good retirement benefits, even if you weren't very satisfied with your career.    
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_r2_options[0]:
    intro()
  elif user_input == u02_r2_options[1]:
    theend()
#done    
def u02_1_2():
  u02_1_2_options = ["1","2"]
  user_input = ""
  while user_input not in u02_1_2_options:
    print                 (r""" 

               .---[[__]]----.
              ;-------------.|       ____
              |             ||   .--[[__]]---.
              |             ||  ;-----------.|
              |             ||  |           ||
              |_____________|/  |           ||
                                |___________|/
                           
                           """)
    print(''' \n \n You have decided to try to climb the ladder at your job, and it hasn't gone too bad. You're quickly approaching retirement though, and not sure what's next.    
  
    1) I'm satisfied with where I am. I'm gonna coast from here. 
    2) I'm gonna try to climb even higher!
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_1_2_options[0]:
    u02_r11()
  elif user_input == u02_1_2_options[1]:
    u02_r22()
#done
def u02_r11():
  u02_r11_options = ["1","2"]
  user_input = ""
  while user_input not in u02_r11_options:
    print                 (r"""
                       
          ////////\\\  
         // __   __ \\ 
        // (()) (()) \\
       (_    (___)    _)
         \  \_____/  /
          `-._   _.-'
          __.-)_(-,__ 
       ./'  \_\_/_/  `\.
      / >   | //\ |   < \
     /  \   | |/| |   /  \
    /   |\  | |/| |  /|   \
   /   /| \ | |/| | / |\   \
  (   ( |  \| |/| |/  | )   )
   \   \|   Y |/| Y   |/   /
    \   |  o| |/| |-  |   /
     `\ |   | `^` |   | /'
       `|  o|=[Ll=|-  |'
        |   /     \   |
        ~~|`  \    `|~~
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |____|____|
          /   / \   \
         /   /   \   \
        `---'     `---`  

                           """)
    print(''' \n \n You have reached retirement. You got pretty far, until you decided to coast, and despite your unsatisfying career choice, you're still happy in retirement.    
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_r11_options[0]:
    intro()
  elif user_input == u02_r11_options[1]:
    theend()
#done
def u02_r22():
  u02_r22_options = ["1","2"]
  user_input = ""
  while user_input not in u02_r22_options:
    print                 (r"""
           
        ,%&& %&& %
       ,%&%& %&%& %&
      %& %&% &%&% % &%
     % &%% %&% &% %&%&,
     &%&% %&%& %& &%& %
    %%& %&%& %&%&% %&%%&
    &%&% %&% % %& &% %%&
    && %&% %&%& %&% %&%'
     '%&% %&% %&&%&%%'%
      % %& %& %&% &%%
        `\%%.'  /`%&'
          |    |            /`-._           _\\/
          |,   |_          /     `-._ ..--~`_
          |;   |_`\_      /  ,\\.~`  `-._ -  ^
          |;:  |/^}__..-,@   .~`    ~    `o ~
          |;:  |(____.-'     '.   ~   -    `    ~
          |;:  |  \ / `\       //.  -    ^   ~
          |;:  |\ /' /\_\_        ~. _ ~   -   //-
     \\/;:   \'--' `---`           `\\//-\\///

                           """)
    print(''' \n \n You have reached retirement. You nearly climbed to the top of your field, even if it wasn't your passion, and you're prrtty happy in retirement.    
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_r22_options[0]:
    intro()
  elif user_input == u02_r22_options[1]:
    theend()
#done

def u02_2():
  u02_2_options = ["1","2","3"]
  user_input = ""
  while user_input not in u02_2_options:
    print                 (r""" 

               .---[[__]]----.
              ;-------------.|       ____
              |             ||   .--[[__]]---.
              |             ||  ;-----------.|
              |             ||  |           ||
              |_____________|/  |           ||
                                |___________|/         

                           """)
    print(''' \n \n Despite your lack of motivation and confidence in college, you adopt a growth mindset heading into the workplace and get off to a good start.    
  
    1) I can't take this job. I quit! 
    2) I probably wasn't right for this. I might just try to coast.
    3) I got a good job that I don't hate, and I'm going to continue to take advantage of every opportunity I possibly can.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_2_options[0]:
    cc02_1()
  elif user_input == u02_2_options[1]:
    u02_2_1()
  elif user_input == u02_2_options[2]:
    u02_2_2()
#done
def u02_2_1():
  u02_2_1_options = ["1","2","3"]
  user_input = ""
  while user_input not in u02_2_1_options:
    print                 (r""" 
     
   +8-=-=-=-=-=-8+
   | ,.-'"'-., |
   |/         \|
   |\:.     .:/|
   | \:::::::/ |
   |  \:::::/  |
   |   \:::/   |
   |    ):(    |
   |   / . \   |
   |  /  .  \  |  
   | /   .   \ |
   |/   .:.   \|
   |\.:::::::./|
   | '--___--' |
   +8-=-=-=-=-=-8+
                           
                           """)
    print(''' \n \n You have decided to stick to what you have, and you're approaching retirement, though with a fairly low life satisfaction.    
  
    1) Almost there! 
    2) I think it's time I readopted a growth mindset.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_2_1_options[0]:
    u022_r1()
  elif user_input == u02_2_1_options[1]:
    u022_r2()
#done
def u022_r1():
  u022_r1_options = ["1","2"]
  user_input = ""
  while user_input not in u022_r1_options:
    print                 (r""" 
     
             .-'--.
      .'      '.
     /     _    `-.
    /      .\-     \,  ,
   ;       .-|-'    \####,
   |,       .-|-'    ;####
  ,##         `     ,|###"
    #,####, "#,        ,#|^;#
  `######  `#####,|##" |`)|
  `#####    ```o\`\o_.| ;\
   (-`\#,    .-'` |`  : `;
    `\ ;\#,         \   \-'
      )( \#    C,_   \   ;
     (_,  \  /   `'./   |
       \  / | .-`'--'`. |
     | ( \   ,  /_,  |
         \    `   ``     /
          '-.__     // .'
              `'`.__.'   

                           """)
    print(''' \n \n You have reached retirement. You have enough money to live on, but you have many regrets regarding your career path.    
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u022_r1_options[0]:
    intro()
  elif user_input == u022_r1_options[1]:
    theend()
#done
def u022_r2():
  u022_r2_options = ["1","2"]
  user_input = ""
  while user_input not in u022_r2_options:
    print                 (r""" 
     
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        | \___/ |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|  

                           """)
    print(''' \n \n You have reached retirement. Though it happened late in your career, you managed to readopt your growth mindset and climb the ladder a little bit and secure good retirement benefits, even if you weren't very satisfied with your career.    
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u022_r2_options[0]:
    intro()
  elif user_input == u022_r2_options[1]:
    theend()
#done
def u02_2_2():
  u02_2_2_options = ["1","2"]
  user_input = ""
  while user_input not in u02_2_2_options:
    print                 (r""" 
        
        ////^\\\\
        | ^   ^  |
       @ (o) (o)  @
        |   <    |
        | \____/ |
        \  ___ __/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|             

                           """)
    print(''' \n \n You have decided to continue to climb the ladder at your job, and it hasn't gone too bad. You're quickly approaching retirement though, and not sure what's next.    
  
    1) I'm satisfied with where I am. I'm gonna coast from here. 
    2) I'm gonna try to climb even higher!
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u02_2_2_options[0]:
    u022_r11()
  elif user_input == u02_2_2_options[1]:
    u022_r22()
#done
def u022_r11():
  u022_r11_options = ["1","2"]
  user_input = ""
  while user_input not in u022_r11_options:
    print                 (r"""
                       
          ////////\\\  
         // __   __ \\ 
        // (()) (()) \\
       (_    (___)    _)
         \  \_____/  /
          `-._   _.-'
          __.-)_(-,__ 
       ./'  \_\_/_/  `\.
      / >   | //\ |   < \
     /  \   | |/| |   /  \
    /   |\  | |/| |  /|   \
   /   /| \ | |/| | / |\   \
  (   ( |  \| |/| |/  | )   )
   \   \|   Y |/| Y   |/   /
    \   |  o| |/| |-  |   /
     `\ |   | `^` |   | /'
       `|  o|=[Ll=|-  |'
        |   /     \   |
        ~~|`  \    `|~~
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |____|____|
          /   / \   \
         /   /   \   \
        `---'     `---`  

                           """)
    print(''' \n \n You have reached retirement. You got pretty far, until you decided to coast, and you're happy in retirement.    
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u022_r11_options[0]:
    intro()
  elif user_input == u022_r11_options[1]:
    theend()
#done
def u022_r22():
  u022_r22_options = ["1","2"]
  user_input = ""
  while user_input not in u022_r22_options:
    print                 (r"""
           
        ,%&& %&& %
       ,%&%& %&%& %&
      %& %&% &%&% % &%
     % &%% %&% &% %&%&,
     &%&% %&%& %& &%& %
    %%& %&%& %&%&% %&%%&
    &%&% %&% % %& &% %%&
    && %&% %&%& %&% %&%'
     '%&% %&% %&&%&%%'%
      % %& %& %&% &%%
        `\%%.'  /`%&'
          |    |            /`-._           _\\/
          |,   |_          /     `-._ ..--~`_
          |;   |_`\_      /  ,\\.~`  `-._ -  ^
          |;:  |/^}__..-,@   .~`    ~    `o ~
          |;:  |(____.-'     '.   ~   -    `    ~
          |;:  |  \ / `\       //.  -    ^   ~
          |;:  |\ /' /\_\_        ~. _ ~   -   //-
     \\/;:   \'--' `---`           `\\//-\\///

                           """)
    print(''' \n \n You have reached retirement. You nearly climbed to the top of your field, and you're prrtty happy in retirement.    
  
    1) Restart 
    2) End Game
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u022_r22_options[0]:
    intro()
  elif user_input == u022_r22_options[1]:
    theend()
#done

def u03():
  u03_options = ["1","2","3"]
  user_input = ""
  while user_input not in u03_options:
    print                 (''' 
                                     
                                                          /
  _o    o/     \o_          \ /    __ __o   |o  \__/o  |   o____  _o    o/
  __|-   |__  __/    \__/o    |    /     |   /          o\  /        \   |  
     >   |      >    /  \    /o\  o|    <<  |                       <<  < \
                
                           ''')
    print(''' \n \n Congratulations! You applied yourself at the university, and you have graduated with a degree in your dream field and a strong possiblity of finding a job.    
  
    1) Maybe I've made a mistake. I can't actually do this! 
    2) I've made it to where I want to be in life. I'll take a "safe" job and coast.
    3) It's time to pursue my dream job. My growth mindset will help me along the way.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03_options[0]:
    fastfood()
  elif user_input == u03_options[1]:
    u03_1()
  elif user_input == u03_options[2]:
    u03_2()
#done

def u03_1():
  u03_1_options = ["1","2","3"]
  user_input = ""
  while user_input not in u03_1_options:
    print                 (r"""        
              
             __-----__
       ..;;;--'~~~`--;;;..
     /;-~IN GOD WE TRUST~-.\
    //      ,;;;;;;;;      \\
  .//      ;;;;;    \       \\
  ||       ;;;;(   /.|       ||
  ||       ;;;;;;;   _\      ||
  ||       ';;  ;;;;=        ||
  ||LIBERTY | ''\;;;;;;      ||
   \\     ,| '\  '|><| 1995 //
    \\   |     |      \  A //
     `;.,|.    |      '\.-'/
       ~~;;;,._|___.,-;;;~'
           ''=--'         
               
                           """)
    print(''' \n \n Despite your regent graduation in your dream major, you faltered in your growth mindset and decided to take a "safe job".    
  
    1) I'm not worth anything, and that's just the way I am.  
    2) I managed to get this job, and I don't really like it, but can I really do any better?
    3) Maybe I made a mistake coming out of college. I can do whatever I set my mind to.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03_1_options[0]:
    fastfood()
  elif user_input == u03_1_options[1]:
    u03stagnant()
  elif user_input == u03_1_options[2]:
    u03climb()
#done
def u03stagnant():
  u03stagnant_options = ["1","2"]
  user_input = ""
  while user_input not in u03stagnant_options:
    print                 (r""" 
                           
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
        \ /___\_/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|             
                           
                           """)
    print(''' \n \n Your fixed mindset leads you to believe you can't really do any better than your current job. Retirement approaches.    
  
    1) I can't take this anymore. I quit!  
    2) Maybe I was wrong. I may not like this job but I am more than capable of climbing the ladder.
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03stagnant_options[0]:
    u03stagnants()
  elif user_input == u03stagnant_options[1]:
    u03stagnantl()
#done
def u03stagnants():
  u03stagnants_options = ["1","2"]
  user_input = ""
  while user_input not in u03stagnants_options:
    print                 (r""" 
            
      .'      '.
     /     _    `-.
    /      .\-     \,  ,
   ;       .-|-'    \####,
   |,       .-|-'    ;####
  ,##         `     ,|###"
    #,####, "#,        ,#|^;#
  `######  `#####,|##" |`)|
  `#####    ```o\`\o_.| ;\
   (-`\#,    .-'` |`  : `;
    `\ ;\#,         \   \-'
      )( \#    C,_   \   ;
     (_,  \  /   `'./   |
       \  / | .-`'--'`. |
     | ( \   ,  /_,  |
         \    `   ``     /
          '-.__     // .'
              `'`.__.'   
                           
                           """)
    print(''' \n \n You're at the point of retirement, and you're dissapointed with the way your life has gone. You have one final option, work two more at a higher position or retire.    
  
    1) It's more than time I retire!  
    2) Two more years at a better salary doesn't sound too bad.
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03stagnants_options[0]:
    u03stagnantsr()
  elif user_input == u03stagnants_options[1]:
    u03stagnantswm()
#done
def u03stagnantsr():
  u03stagnantsr_options = ["1","2"]
  user_input = ""
  while user_input not in u03stagnantsr_options:
    print                 (r""" 
                                    
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
    \ \|
                           
                           """)
    print(''' \n \n You've retired...with really poor benefits and without a very high life satisfaction.    
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03stagnantsr_options[0]:
    intro()
  elif user_input == u03stagnantsr_options[1]:
    theend()
#done
def u03stagnantswm():
  u03stagnantswm_options = ["1","2"]
  user_input = ""
  while user_input not in u03stagnantswm_options:
    print                 (r"""
                                     
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        | \___/ |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|    
                    
                           """)
    print(''' \n \n You've retired...with really poor benefits though you are satisfied you gave that push at the end.    
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03stagnantswm_options[0]:
    intro()
  elif user_input == u03stagnantswm_options[1]:
    theend()
#done
def u03stagnantl():
  u03stagnantl_options = ["1","2"]
  user_input = ""
  while user_input not in u03stagnantl_options:
    print                 (r""" 
                                
                           .--.
                        |  |
          ______________ ||
       .-"______________"-.
     ." ."              ". ".
    /  /    __________   |\  \
   |  |  .-'__ _ _ _ _'-.|||  |
   |  |.'  /__/_/_/_/_/  '.|  |
   |  ||  _____________   ||  |
   |  ;|__________________|;  |
   '--|o .--------------. o|--'
     (|  |   .-.  .-.   |  |)
      |  |  ( ())( ())  |  |
     /   |   '-'  '-'   |   \
    |    '--------------'    |
    |   ,_      /\      _,   |
    |   |=="'--------'"==|   |
    |   |================|   |
    |    \==============/    |
    |     `-.________.-`     |
     `-.__________________.-'
 /)))))/'         ___     `\
  ((    /  .-------' | :.     \
   \)))>-=<|   ===)  | ::------'
           '-------._|_:'
                  
                           """)
    print(''' \n \n Despite your original hiccup, you adopt a growth mindset and advance in your company. Retirement approaches.   
  
    1) I was wrong. I quit!  
    2) I'm gonna make sure I never make that mistake again. Time to go even higher!
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03stagnantl_options[0]:
    u03stagnantls()
  elif user_input == u03stagnantl_options[1]:
    u03stagnantll()
#done
def u03stagnantls():
  u03stagnantls_options = ["1","2"]
  user_input = ""
  while user_input not in u03stagnantls_options:
    print                 (r"""
                                   
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|
                           
                           """)
    print(''' \n \n You've hit retirement, and your abandomment of your growth mindset has led to a poor retirement.   
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03stagnantls_options[0]:
    intro()
  elif user_input == u03stagnantls_options[1]:
    theend()
#done
def u03stagnantll():
  u03stagnantll_options = ["1","2"]
  user_input = ""
  while user_input not in u03stagnantll_options:
    print                 (r""" 
                                    
          .=.,
            ;c =\
          __|  _/
        .'-'-._/-'-._
       /..   ____    \
      /' _  [<_->] )  \
     (  / \--\_>/-/'._ )
      \-;_/\__;__/ _/ _/
       '._}|==o==\{_\/
        /  /-._.--\  \_
       // /   /|   \ \ \
      / | |   | \;  |  \ \
     / /  | :/   \: \   \_\
    /  |  /.'|   /: |    \ \
    |  |  |--| . |--|     \_\
    / _/   \ | : | /___--._) \
   |_(---'-| >-'-| |       '-'
          /_/     \_\
                  
                           """)
    print(''' \n \n Things go really well career-wise, and you retire near the top of your company with good benefits.   
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03stagnantll_options[0]:
    intro()
  elif user_input == u03stagnantll_options[1]:
    theend()
#done
def u03climb():
  u03climb_options = ["1","2"]
  user_input = ""
  while user_input not in u03climb_options:
    print                 (r""" 
                           
        ////^\\\\
        | ^   ^  |
       @ (o) (o)  @
        |   <    |
        | \____/ |
        \  ___ __/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|             
             
                           """)
    print(''' \n \n Your growth mindset helps you get back on top. You've set your mind to trying to climb the ladder at your current job, and it's gone well!    
  
    1) I should take it easy from here. It's not gonna get any better.  
    2) I knew I could do it, and I'm not stopping here!
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03climb_options[0]:
    u03climbs()
  elif user_input == u03climb_options[1]:
    u03climbc()
#done
def u03climbs():
  u03climbs_options = ["1","2"]
  user_input = ""
  while user_input not in u03climbs_options:
    print                 (r"""                     
             
      /////\\
      -O-O-||
      |/   @|
       \-  /
      __| |__
    .'       `.
    |         |
    | |     | |
    | |     | |
    | |     | |
    |_|     |_|
    \/|_____|\/
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
     _|__|__|
    (__(____]

                           """)
    print(''' \n \n After you abadoned your growth mindset, you approach retirement without much change.     
  
    1) Steady!  
    2) Maybe I made the wrong decision. Time to work.
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03climbs_options[0]:
    u03climbss()
  elif user_input == u03climbs_options[1]:
    u03climbsc()
#done
def u03climbss():
  u03climbss_options = ["1","2"]
  user_input = ""
  while user_input not in u03climbss_options:
    print                 (r""" 
                           
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|

                           """)
    print(''' \n \n You stayed steady in your job, without much ambition to advance and in the end finished with barely enough to get by and a lot of disatisfaction.     
  
    1) Restart 
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03climbss_options[0]:
    intro()
  elif user_input == u03climbss_options[1]:
    theend()
#done
def u03climbsc():
  u03climbsc_options = ["1","2"]
  user_input = ""
  while user_input not in u03climbsc_options:
    print                 (r""" 
          
          ////////\\\  
         // __   __ \\ 
        // (()) (()) \\
       (_    (___)    _)
         \  \_____/  /
          `-._   _.-'
          __.-)_(-,__ 
       ./'  \_\_/_/  `\.
      / >   | //\ |   < \
     /  \   | |/| |   /  \
    /   |\  | |/| |  /|   \
   /   /| \ | |/| | / |\   \
  (   ( |  \| |/| |/  | )   )
   \   \|   Y |/| Y   |/   /
    \   |  o| |/| |-  |   /
     `\ |   | `^` |   | /'
       `|  o|=[Ll=|-  |'
        |   /     \   |
        ~~|`  \    `|~~
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |____|____|
          /   / \   \
         /   /   \   \
        `---'     `---`                

                           """)
    print(''' \n \n Despite your initial lack of ambition, you gave a slight push at the end of your career and made some progress. You're retirement isn't much, put at least it was satisfying to work at your full potential, even if it only lasted a few years.     
  
    1) Restart 
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03climbsc_options[0]:
    intro()
  elif user_input == u03climbsc_options[1]:
    theend()
#done
def u03climbc():
  u03climbc_options = ["1","2"]
  user_input = ""
  while user_input not in u03climbc_options:
    print                 (r""" 
                           
                         i i'
                         \~;\
                          \; \
                           \ ;\    ====
                            \ ;\  ==== \
                       __,--';;;\-' (  0
                 __,--';;; ;;; ;;\      >
          __,--'\\ ;;; ;;; ;;; ;;;\--__<
   _ _,--' __,--'\\  ;;; __,~~' \ ;\
  (_)|_,--' __,--'\\;,~~'        \ ;\
  |(_)|_,--'       ~~             \; \
  || |                             \ ;\
   |_/                              !~!,
                                .---'''---.
                                |         |
                                |         |
                                |         |
                                `---------'

                           """)
    print(''' \n \n You've made it far in your career, and as you approach retirement it's time to decide how you're going to finish!    
  
    1) Time to slow down!  
    2) One final push!
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03climbc_options[0]:
    u03climbcs()
  elif user_input == u03climbc_options[1]:
    u03climbcc()
#done
def u03climbcs():
  u03climbcs_options = ["1","2"]
  user_input = ""
  while user_input not in u03climbcs_options:
    print                 (r""" 
                               
              _.-"''-._
           /.-......-.\
          //          \\
          ||          ||
          ||.--    --.||
          /| (.)||(.) |\
          \    (__)    /
           |  ,____,  |
            \  `--'  /
         _./`'.____.'`\._
     _.::::|  |    |  |::::._
   .::::::::\  \  /  /::::::::.
  /::::::::::|/:\/:\|::::::::::\    

                           """)
    print(''' \n \n Despite not living up your full potential, you did a good job overall and are happy with a good retirement.     
  
    1) Restart 
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03climbcs_options[0]:
    intro()
  elif user_input == u03climbcs_options[1]:
    theend()
#done
def u03climbcc():
  u03climbcc_options = ["1","2"]
  user_input = ""
  while user_input not in u03climbcc_options:
    print                 (r""" 
                               
            .=.,
            ;c =\
          __|  _/
        .'-'-._/-'-._
       /..   ____    \
      /' _  [<_->] )  \
     (  / \--\_>/-/'._ )
      \-;_/\__;__/ _/ _/
       '._}|==o==\{_\/
        /  /-._.--\  \_
       // /   /|   \ \ \
      / | |   | \;  |  \ \
     / /  | :/   \: \   \_\
    /  |  /.'|   /: |    \ \
    |  |  |--| . |--|     \_\
    / _/   \ | : | /___--._) \
   |_(---'-| >-'-| |       '-'
          /_/     \_\
                   

                           """)
    print(''' \n \n You managed to put the hiccup at the start of your career behind you, and never stopped succeeding until the very end. You have a lot to look forward to in retirement.     
  
    1) Restart 
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03climbcc_options[0]:
    intro()
  elif user_input == u03climbcc_options[1]:
    theend()
#done

def u03_2():
  u03_2_options = ["1","2","3"]
  user_input = ""
  while user_input not in u03_2_options:
    print                 (r"""        
                                                   
     /:""|       
     |: 66|_     
     C     _)    
      \ ._|      
       ) /        
      /`\\        
     || |Y|            
     :| |=:     
     ||_|,|    
     \)))||    
  |~~~`-`~~~|  
  |         |    
  |_________|      
  |_________|       
      | ||         
      |_||__      
   (____))    

                           """)
    print(''' \n \n Coming out of the university, you're set to secure a job in your dream field. To think you thought you were a failure in high school.    
  
    1) I'm not worth anything, and that's just the way I am. What was I thinking?  
    2) I'm confident I can get a job, but how good can I really be? Should I even work hard? Do I even have it in me?
    3) I don't doubt myself even for a second. Nothing can stand in my way.
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03_2_options[0]:
    fastfood()
  elif user_input == u03_2_options[1]:
    u032stagnant()
  elif user_input == u03_2_options[2]:
    u032climb()
#done
def u032stagnant():
  u032stagnant_options = ["1","2"]
  user_input = ""
  while user_input not in u032stagnant_options:
    print                 (r""" 
                           
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
        \ /___\_/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|             
                           
                           """)
    print(''' \n \n Despite your previous growth mindset and success, you begin to doubt yourself and your career suffers as a result.    
  
    1) I can't take this anymore. I quit!  
    2) I can take a minor setback. Time to get back on track.
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032stagnant_options[0]:
    u032stagnants()
  elif user_input == u032stagnant_options[1]:
    u032stagnantl()
#done
def u032stagnants():
  u032stagnants_options = ["1","2"]
  user_input = ""
  while user_input not in u032stagnants_options:
    print                 (r""" 
            
      .'      '.
     /     _    `-.
    /      .\-     \,  ,
   ;       .-|-'    \####,
   |,       .-|-'    ;####
  ,##         `     ,|###"
    #,####, "#,        ,#|^;#
  `######  `#####,|##" |`)|
  `#####    ```o\`\o_.| ;\
   (-`\#,    .-'` |`  : `;
    `\ ;\#,         \   \-'
      )( \#    C,_   \   ;
     (_,  \  /   `'./   |
       \  / | .-`'--'`. |
     | ( \   ,  /_,  |
         \    `   ``     /
          '-.__     // .'
              `'`.__.'   
                           
                           """)
    print(''' \n \n You're approaching retirement, and though things were going at well first, it's been all downhill since and you blame everyone except yourself. Time for a final push?
  
    1) It's more than time I retire!  
    2) Two more years at a better salary doesn't sound too bad.
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032stagnants_options[0]:
    u032stagnantsr()
  elif user_input == u032stagnants_options[1]:
    u032stagnantswm()
#done
def u032stagnantsr():
  u032stagnantsr_options = ["1","2"]
  user_input = ""
  while user_input not in u032stagnantsr_options:
    print                 (r""" 
                                    
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|
                           
                           """)
    print(''' \n \n You've retired...with really poor benefits and without a very high life satisfaction.    
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032stagnantsr_options[0]:
    intro()
  elif user_input == u032stagnantsr_options[1]:
    theend()
#done
def u032stagnantswm():
  u03stagnantswm_options = ["1","2"]
  user_input = ""
  while user_input not in u03stagnantswm_options:
    print                 (r"""
                                     
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        | \___/ |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|    
                    
                           """)
    print(''' \n \n You've retired...with really poor benefits though you are satisfied you gave that push at the end.    
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u03stagnantswm_options[0]:
    intro()
  elif user_input == u03stagnantswm_options[1]:
    theend()
#done
def u032stagnantl():
  u032stagnantl_options = ["1","2"]
  user_input = ""
  while user_input not in u032stagnantl_options:
    print                 (r""" 
                                
                           .--.
                        |  |
          ______________ ||
       .-"______________"-.
     ." ."              ". ".
    /  /    __________   |\  \
   |  |  .-'__ _ _ _ _'-.|||  |
   |  |.'  /__/_/_/_/_/  '.|  |
   |  ||  _____________   ||  |
   |  ;|__________________|;  |
   '--|o .--------------. o|--'
     (|  |   .-.  .-.   |  |)
      |  |  ( ())( ())  |  |
     /   |   '-'  '-'   |   \
    |    '--------------'    |
    |   ,_      /\      _,   |
    |   |=="'--------'"==|   |
    |   |================|   |
    |    \==============/    |
    |     `-.________.-`     |
     `-.__________________.-'
 /)))))/'         ___     `\
  ((    /  .-------' | :.     \
   \)))>-=<|   ===)  | ::------'
           '-------._|_:'
                  
                           """)
    print(''' \n \n Despite a quick hiccup, you readopt a growth mindset and advance in your company. Retirement approaches.   
  
    1) I was wrong. I quit!  
    2) I'm gonna make sure I never make that mistake again. Time to go even higher!
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032stagnantl_options[0]:
    u032stagnantls()
  elif user_input == u032stagnantl_options[1]:
    u032stagnantll()
#done
def u032stagnantls():
  u032stagnantls_options = ["1","2"]
  user_input = ""
  while user_input not in u032stagnantls_options:
    print                 (r"""
                                   
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|
                           
                           """)
    print(''' \n \n You've hit retirement, and your abandomment of your growth mindset has led to a poor retirement.   
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032stagnantls_options[0]:
    intro()
  elif user_input == u032stagnantls_options[1]:
    theend()
#done 
def u032stagnantll():
  u032stagnantll_options = ["1","2"]
  user_input = ""
  while user_input not in u032stagnantll_options:
    print                 (r""" 
                                    
            .=.,
            ;c =\
          __|  _/
        .'-'-._/-'-._
       /..   ____    \
      /' _  [<_->] )  \
     (  / \--\_>/-/'._ )
      \-;_/\__;__/ _/ _/
       '._}|==o==\{_\/
        /  /-._.--\  \_
       // /   /|   \ \ \
      / | |   | \;  |  \ \
     / /  | :/   \: \   \_\
    /  |  /.'|   /: |    \ \
    |  |  |--| . |--|     \_\
    / _/   \ | : | /___--._) \
   |_(---'-| >-'-| |       '-'
          /_/     \_\
                  
                           """)
    print(''' \n \n Things go really well career-wise, and you retire near the top of your company with good benefits.   
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032stagnantll_options[0]:
    intro()
  elif user_input == u032stagnantll_options[1]:
    theend()
#done
def u032climb():
  u032climb_options = ["1","2"]
  user_input = ""
  while user_input not in u032climb_options:
    print                 (r""" 
                           
                         i i'
                         \~;\
                          \; \
                           \ ;\    ====
                            \ ;\  ==== \
                       __,--';;;\-' (  0
                 __,--';;; ;;; ;;\      >
          __,--'\\ ;;; ;;; ;;; ;;;\--__<
   _ _,--' __,--'\\  ;;; __,~~' \ ;\
  (_)|_,--' __,--'\\;,~~'        \ ;\
  |(_)|_,--'       ~~             \; \
  || |                             \ ;\
   |_/                              !~!,
                                .---'''---.
                                |         |
                                |         |
                                |         |
                                `---------'

                           """)
    print(''' \n \n Your continued growth mindset works wonders for your career, and you find yourself near the top very early on.    
  
    1) Time to hit the breaks! it's a miracle I made it this far.  
    2) It's hard to believe what I though about myself in high school. Onward!
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032climb_options[0]:
    u032climbs()
  elif user_input == u032climb_options[1]:
    u032climbc()
#done
def u032climbs():
  u032climbs_options = ["1","2"]
  user_input = ""
  while user_input not in u032climbs_options:
    print                 (r"""                     
             
      /////\\
      -O-O-||
      |/   @|
       \-  /
      __| |__
    .'       `.
    |         |
    | |     | |
    | |     | |
    | |     | |
    |_|     |_|
    \/|_____|\/
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
     _|__|__|
    (__(____]

                           """)
    print(''' \n \n Despite your whopping early success, you've decided to pump the breaks. Retirement approaches!     
  
    1) Steady!  
    2) Maybe I made the wrong decision. Time to work.
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032climbs_options[0]:
    u032climbss()
  elif user_input == u032climbs_options[1]:
    u032climbsc()
#done
def u032climbss():
  u032climbss_options = ["1","2"]
  user_input = ""
  while user_input not in u032climbss_options:
    print                 (r""" 
                           
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|

                           """)
    print(''' \n \n You stayed steady in your job, without much ambition to advance and in the end finished with an average retirement plan and little self-satisfaction.     
  
    1) Restart 
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032climbss_options[0]:
    intro()
  elif user_input == u032climbss_options[1]:
    theend()
#done
def u032climbsc():
  u032climbsc_options = ["1","2"]
  user_input = ""
  while user_input not in u032climbsc_options:
    print                 (r""" 
          
          ////////\\\  
         // __   __ \\ 
        // (()) (()) \\
       (_    (___)    _)
         \  \_____/  /
          `-._   _.-'
          __.-)_(-,__ 
       ./'  \_\_/_/  `\.
      / >   | //\ |   < \
     /  \   | |/| |   /  \
    /   |\  | |/| |  /|   \
   /   /| \ | |/| | / |\   \
  (   ( |  \| |/| |/  | )   )
   \   \|   Y |/| Y   |/   /
    \   |  o| |/| |-  |   /
     `\ |   | `^` |   | /'
       `|  o|=[Ll=|-  |'
        |   /     \   |
        ~~|`  \    `|~~
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |____|____|
          /   / \   \
         /   /   \   \
        `---'     `---`                

                           """)
    print(''' \n \n Despite your fall in ambition, you gave a slight push at the end of your career and made some progress. You're retirement is still pretty good, put at least it was satisfying to work at your full potential again, even if it only lasted a few years.     
  
    1) Restart 
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032climbsc_options[0]:
    intro()
  elif user_input == u032climbsc_options[1]:
    theend()
#done
def u032climbc():
  u032climbc_options = ["1","2"]
  user_input = ""
  while user_input not in u032climbc_options:
    print                 (r""" 
                           
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        | \___/ |
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|    

                           """)
    print(''' \n \n Your career is going great, you've pursued your dream, and above all are happy. As retirement approaches, what's left?   
  
    1) Time to slow down!  
    2) One final push!
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032climbc_options[0]:
    u032climbcs()
  elif user_input == u032climbc_options[1]:
    u032climbcc()
#done
def u032climbcs():
  u032climbcs_options = ["1","2"]
  user_input = ""
  while user_input not in u032climbcs_options:
    print                 (r""" 
                                    
         ////////\\\  
         // __   __ \\ 
        // (()) (()) \\
       (_    (___)    _)
         \  \_____/  /
          `-._   _.-'
          __.-)_(-,__ 
       ./'  \_\_/_/  `\.
      / >   | //\ |   < \
     /  \   | |/| |   /  \
    /   |\  | |/| |  /|   \
   /   /| \ | |/| | / |\   \
  (   ( |  \| |/| |/  | )   )
   \   \|   Y |/| Y   |/   /
    \   |  o| |/| |-  |   /
     `\ |   | `^` |   | /'
       `|  o|=[Ll=|-  |'
        |   /     \   |
        ~~|`  \    `|~~
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |    |    |
          |____|____|
          /   / \   \
         /   /   \   \
        `---'     `---`                

                  
                           """)
    print(''' \n \n Things go really well career-wise, and you retire near the top of your company with good benefits.   
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032climbcs_options[0]:
    intro()
  elif user_input == u032climbcs_options[1]:
    theend()
#done
def u032climbcc():
  u032climbcc_options = ["1","2"]
  user_input = ""
  while user_input not in u032climbcc_options:
    print                 (r""" 
                                    
            .=.,
            ;c =\
          __|  _/
        .'-'-._/-'-._
       /..   ____    \
      /' _  [<_->] )  \
     (  / \--\_>/-/'._ )
      \-;_/\__;__/ _/ _/
       '._}|==o==\{_\/
        /  /-._.--\  \_
       // /   /|   \ \ \
      / | |   | \;  |  \ \
     / /  | :/   \: \   \_\
    /  |  /.'|   /: |    \ \
    |  |  |--| . |--|     \_\
    / _/   \ | : | /___--._) \
   |_(---'-| >-'-| |       '-'
          /_/     \_\
                  
                           """)
    print(''' \n \n After high school, your growth mindset never failed you, and you retire with a high life-satisfaction, for having always believed in what you could do and making your life your own.   
  
    1) Restart  
    2) End Game
   
    ''')

    user_input = str(input("What will you do?"))
  print ("You have selected " + user_input)
  if user_input == u032climbcc_options[0]:
    intro()
  elif user_input == u032climbcc_options[1]:
    theend()
#done

#- Main Program
intro()
