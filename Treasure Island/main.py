#as in the flowchart build the game
#https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

import time
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Ahoy pirates, How are ye feeling today?")
time.sleep(2)
print("G'yaaaarrrrrrr. looke here....")
time.sleep(1)
print('I just got me a treasure map!!!')
time.sleep(1)
print('Are you up for the journey then say with me...')
time.sleep(2)
print('Aye Aye Aye Captain')
time.sleep(1)
print('Lets gooooooo...')
time.sleep(1)
print("Okay pirates let's test your luck")
time.sleep(1)
print("Me brought U here on the 'Treasure Island' and Your mission is to find the BOOTY")
time.sleep(2)
print("Here comes the First point ")
time.sleep(1)
lor = input("LEFT or RIGHT choose wise, cause not every RIGHT is right : ")
time.sleep(3)
if(lor == 'right') or (lor == 'RIGHT'):
  print(''' ********          **  **       **                                **      **   *******   **       ********
            /**/////          /** /**      //                                /**     /**  **/////** /**      /**///// 
            /**        *****  /** /**       ** *******         ******        /**     /** **     //**/**      /**      
            /*******  **///** /** /**      /**//**///**       //////**       /**********/**      /**/**      /******* 
            /**////  /******* /** /**      /** /**  /**        *******       /**//////**/**      /**/**      /**////  
            /**      /**////  /** /**      /** /**  /**       **////**       /**     /**//**     ** /**      /**      
            /**      //****** *** ***      /** ***  /**      //********      /**     /** //*******  /********/********
            //        ////// /// ///       // ///   //        ////////       //      //   ///////   //////// //////// ''')
  time.sleep(2)
  print('Game Over Pirate. Have some GROG and come back...Aye Aye...')
elif(lor == 'left') or (lor == 'LEFT'):
  print("Yo ho ho! forward and onward.... reached a lake with a Island in middle, to the second point")
  time.sleep(2)
  print("The Water's calm and clear for the swin but be aware of the creatures lurking deep or near U")
  time.sleep(2)
  sow = input("Will U WAIT for a boat or SWIM, choose wisely cause the competion is not thin : ") 
  time.sleep(3)
  if(sow == 'SWIM') or (sow == 'swim'):
    print('''  ******** **      **     **     *******   **   **       ********   *******     *******   *******  
           **////// /**     /**    ****   /**////** /**  **       /**/////   **/////**   **/////**  /**////** 
          /**       /**     /**   **//**  /**   /** /** **        /**       **     //** **     //**/**      /**
          /*********/**********  **  //** /*******  /****         /******* /**      /**/**      /**/**      /**
          ////////**/**//////** **********/**///**  /**/**        /**////  /**      /**/**      /**/**      /**
                 /**/**     /**/**//////**/**  //** /**//**       /**      //**     ** //**     ** /**      ** 
           ******** /**     /**/**     /**/**   //**/** //**      /**       //*******   //*******   /*******  
          ////////  //      // //      // //     // //   //       //         ///////     ///////    ///////   ''')
    time.sleep(2)
    print("Well that's a sad one...., fear not anyone next....")
  elif(sow == 'WAIT') or (sow == 'wait'):
    print("Yo ho ho! forward and onward.... reached the ISLAND, to the last point")
    time.sleep(2)
    print("There are 3 door's color's viz: 'RED', 'BLUE', 'GOLD'")
    time.sleep(2)
    col = input("Only a TRUE Pirate can know its bounty colour : ")
    time.sleep(3)
    if (col == 'RED') or (col == 'red'):
      print(''' ******   **     ** *******   ****     **       ** ****     **       ******** **   *******   ********
                /*////** /**    /**/**////** /**/**   /**      /**/**/**   /**      /**///// /**/**////**   /**///// 
                /*   /** /**    /**/**   /** /**//**  /**      /**/**//**  /**      /**      /**/**   /** /**        
                /******  /**    /**/*******  /** //** /**      /**/** //** /**      /******* /**/*******    /******* 
                /*//// **/**    /**/**///**  /**  //**/**      /**/**  //**/**      /**////  /**/**///**    /**////  
                /*    /**/**    /**/**  //** /**   //****      /**/**   //****      /**      /**/**  //** /**        
                /******* //******* /**   //**/**    //***      /**/**    //***      /**      /**/**     //**/********
                ///////   ///////  //     // //      ///       // //      ///       //       // //     //   //////// 
                ''')
      time.sleep(2)
      print("Well that's a sad one...., fear not anyone next....")
    elif (col == 'BLUE') or (col == 'blue'):
      print(''' 
               *******   *******     *****) or (col == **   **       ** ****     ** ******** *******  
              /**////** /**////**   **/////** /**      /**/**/**   /**/**///// /**////** 
              /**    /**/**   /**  **     //**/**   *  /**/**//**  /**/**      /**    /**
              /**    /**/*******  /**      /**/**  *** /**/** //** /**/******* /**    /**
              /**    /**/**///**  /**      /**/** **/**/**/**  //**/**/**////  /**    /**
              /**    ** /**  //** //**     ** /**** //****/**   //****/**      /**    ** 
              /*******  /**   //** //*******  /**/   ///**/**    //***/********/*******  
              ///////   //     //   ///////   //       // //      /// //////// ///////   ''')
      time.sleep(2)
      print("Well that's a sad one...., fear not anyone next....")
    elif(col == 'GOLD') or (col == 'gold'):
      print('''
      *******************************************************************************
                |                   |                  |                     |
       _________|________________.=""_;=.______________|_____________________|_______
      |                   |  ,-"_,=""     `"=.|                  |
      |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
       _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
      |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
      |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
       _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
      |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
      |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
      ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
      /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
      ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
      /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
      ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
      /______/______/______/______/______/______/______/______/______/______/______/_
      *******************************************************************************
      ''')
      print('Yo ho ho! The BOOTY sure is GOLD')
    else:
      print("Here no BOOTY for yee")
  else:
    print("Here no BOOTY for yee")
else:
  print("Here no BOOTY for yee")

