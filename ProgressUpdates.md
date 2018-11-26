# Progress Update (Week 1)
Group: Raymond Ren, Jim Garrison, Lee Gobin. 
Project: Multiplayer Tic-Tac-Toe

--Progress made this week:--

1. Windows Server set up offsite and made to be open to connections from outside clients.
2. Tested chat program with server to verify chat's can be seen on both ends.
3. Started work on modifying code to allow for multiple clients and have server be middleman only.

--Progress to be made in the coming week:--

1. Get started on UI and actual Tic-Tac-Toe game.
2. Finish work on getting multiple clients and one server only middleman.
3. Work out networking kinks associated with a game such as tic-tac-toe where there is going to be a buffer between messages.

# Progress Update (Week 2)

1) Further discussed the choice between Python vs Java
2) Discussed possible implementations
    >2D array. Row x Column.
        Pros: Cleaner
        Cons: More difficult to desige
    >1D array. 
        Pros: Easier to code.
              Less Work
        Cons: Seems to be inefficient
        
  Progress to be made in the coming week:
  1)Write the method for the server to take in inputs and evaluate it
  2)Maybe discuss the idea of a leader board system that stores Names and Points

# Progress Update (Week 4)

Progress Made this week:

1. Got Server fully functioning and ready to be used as a buffer between x amounts of players using different sockets.
2. Added some functionality to client program to further ability to scale game to x amount of players.
3. Started work on basic functionality of the program itself for the user.

Progress to be made in the coming week:

1. Get basic functionality for the game finished and ready to be played in console.
2. Make sure that networking for game is fully functional and has no glitches.
3. Start looking into setting up GUI for the game to make it look pretty.

# Progress Update (Week 5)

Progress Made this week:

1. Server is fully functional and available to have multiple games running at once with some tweaking.
2. Game is fully functional and networked via console input.
3. Both client have no issues with running and playing the game, as well as replaying the game over and over again without closing socket.

Progress to be made in the coming week:

1. Get game to be fully graphical instead of through the console so as to make the game look nice.
2. Run error checking to verify that nothing is going wrong on the networking side.
3. Start getting demo ready for next week.
        
# Comments
1. Make sure the formatting is not off (Done)
2. Regarding the design, Both 1D and 2D would work and not much different in terms of design complexity and efficiency, thou 2D array on client might be easier and cleaner to manipulate. The more important thing to think about is the message exchanged between client and server and I don't see a clear solution for it. (Good Insight, will look into it.)
3. I would expect to see some codes pushed to master this week. (Done)
