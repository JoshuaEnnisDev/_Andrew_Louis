
# flake8: noqa

title = r"""


 _  __ _____ _      ____  _ ____    _____  ____ ___  _   ____  _____  ____  ____  _____
/ |/ //  __// \__/|/  _ \|// ___\  /__ __\/  _ \\  \//  / ___\/__ __\/  _ \/  __\/  __/
|   / |  \  | |\/||| / \|  |    \    / \  | / \| \  /   |    \  / \  | / \||  \/||  \
|   \ |  /_ | |  ||| \_/|  \___ |    | |  | \_/| / /    \___ |  | |  | \_/||    /|  /_
\_|\_\\____\\_/  \|\____/  \____/    \_/  \____//_/     \____/  \_/  \____/\_/\_\\____\
"""

prize = r""" 
              _.--''`-._
            ,'          `.
          ,'          __  `.
         /|          " __   \
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         ''       `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\
   -" /`.         _,'     | _  _  _.|
    ""--'---''''''      `' '! |! /
                            `" " -' mh
"""

print(title)

welcome_message = """
Welcome to my toy store! If you spend exactly $50 on toys, you will
win an awesome prize!
"""

print(welcome_message)

pokemon_cost = 3
lego_cost = 5

num_pokemon = int(input("How many pokemon would you like? "))
num_lego = int(input("How many legos would like? "))

pokemon_total_cost = pokemon_cost * num_pokemon
lego_total_cost = lego_cost * num_lego
total_cost = pokemon_total_cost + lego_total_cost

subtotal = f"""
====================================================
    Total cost of pokemon: ${pokemon_total_cost}
    Total cost of legos: ${lego_total_cost}

    You spent ${total_cost} on toys.
====================================================
"""

print(subtotal)

if total_cost == 50:
    print(prize)
else:
    print("Sorry, better luck next time!!")


# last line of code
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
