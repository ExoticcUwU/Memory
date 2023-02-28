# Memory

User can choose between 3 difficultys (Small, Medium, Big).
    -The only differenz is the number of pairs which has to be found (size of field)
Under the field, user can see a two live counters:
    -one for his tries
    -one for how many pairs are left
User can clicked a maximum of 2 Buttons, color of button is shown when clicked.
When max. of 2 Buttons where clicked, live counter of tries goes one up and a function is called which checks if both colors are the same.
    Colors are the same:
        -Buttons will always show their color
        -Buttons can not be clicked again
        -live Counter of pairs becomes one less
    
    Colors are different:
        -Button will not show its color again until it is clicked again
User has the option to save and load a game_file.
    following data is saved an loaded:
        -Counter of tries
        -Counter of pairs
        -Difficulty
    
    If game_file is loaded:
        -live counters are set to the saved value
        -found pairs are displayed on the field
Game is won, when user found all pairs.