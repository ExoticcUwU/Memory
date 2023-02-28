# Memory

Users can choose between 3 difficulties (Small, Medium, Big).
    -The only difference is the field size, with the amount of pairs contained in

Under the game field the users can see two live counters:
    -one for his tries
    -one for how many pairs are left

User can click a maximum of 2 buttons, when the buttons are clicked the colors will be visible
When a max. of 2 buttons were clicked, the live counter of tries goes one up and a function is called, which checks if:

    Colors are the same:
        -Buttons will always show their color
        -Buttons can not be clicked again
        -live Counter of pairs becomes one less
    
    Colors are different:
        -Button will not show its color again until it is clicked again
        
Users have the options to save and load a game_file.
    following data is saved an loaded:
        -Counter of tries
        -Counter of pairs
        -Difficulty
    
    If game_file is loaded:
        -live counters are set to the saved value
        -found pairs are displayed on the field

If all Pairs are found the game is won!, dear peru the color :)