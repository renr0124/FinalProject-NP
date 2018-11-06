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
        
# Comments
1. Make sure the formatting is not off
2. Regarding the design, Both 1D and 2D would work and not much different in terms of design complexity and efficiency, thou 2D array on client might be easier and cleaner to manipulate. The more important thing to think about is the message exchanged between client and server and I don't see a clear solution for it.
3. I would expect to see some codes pushed to master this week.
