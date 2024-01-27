welcome_message = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Kemo's Comic Store!

If you spend exactly $35 on comics, you'll win a role in an
upcoming movie version of one of our comics!

                  Good luck!
"""

comic_movie_prize = r""" 
 =ccccc,      ,cccc       ccccc      ,cccc,  ?$$$$$$$,  ,ccc,   -ccc        
:::"$$$$bc    $$$$$     ::`$$$$$c,  : $$$$$c`:"$$$$???'`."$$$$c,:`?$$c      
`::::"?$$$$c,z$$$$F     `:: ?$$$$$c,`:`$$$$$h`:`?$$$,` :::`$$$$$$c,"$$h,    
  `::::."$$$$$$$$$'    ..,,,:"$$$$$$h, ?$$$$$$c`:"$$$$$$$b':"$$$$$$$$$$$c   
     `::::"?$$$$$$    :"$$$$c:`$$$$$$$$d$$$P$$$b`:`?$$$c : ::`?$$c "?$$$$h, 
       `:::.$$$$$$$c,`::`????":`?$$$E"?$$$$h ?$$$.`:?$$$h..,,,:"$$$,:."?$$$c 
         `: $$$$$$$$$c, ::``  :::"$$$b `"$$$ :"$$$b`:`?$$$$$$$c``?$F `:: ":: 
          .,$$$$$"?$$$$$c,    `:::"$$$$.::"$.:: ?$$$.:.???????" `:::  ` ``` 
          'J$$$$P'::"?$$$$h,   `:::`?$$$c`::``:: .:: : :::::''   `          
         :,$$$$$':::::`?$$$$$c,  ::: "::  ::  ` ::'   ``                    
        .'J$$$$F  `::::: .::::    ` :::'  `                                 
       .: ???):     `:: :::::                                               
       : :::::'        `                                                    
        ``
"""

cost_marvel = 2
cost_dc = 3

print(welcome_message)

num_marvel = int(input("How many Marvel comics do you want? "))
num_dc = int(input("How many DC comics do you want? "))

marvel_total = num_marvel * cost_marvel
dc_total = num_dc * cost_dc

print(f"You spent ${marvel_total} on Marvel comics.")
print(f"You spent ${dc_total} on DC comics.")

order_total = marvel_total + dc_total
print(f"Your order total is: ${order_total}")

if order_total == 35:
    print("You won!")
    print(comic_movie_prize)
else:
    print("Not quite, better luck next time!")
print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
