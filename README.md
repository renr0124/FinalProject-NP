# FinalProject-NP

# Tic-Tac-Toe

# Description

What?
Tic-Tac-Toe is a classic game played by millions. It has a 3x3 grid by default and each player puts in their respective symbol (An x or an O) in one of the slots, until someone get's 3 of their symbols in a row. Otherwise, it's a tie.

Why?
Because there aren't enough tic-tac-toe multiplayer clones out there.

How?

We're going to use the power of python and networking to create an effective tic-tac-toe game that utilizes a central server to provide 2 clients with the ability to play against eachother in a high intensity multiplayer environment.

# Deliverables: 
1. 2 Clients (Computers) - Game is client sided so both computers will have identical code. Computers use Python to make game run and look good to x users.
2. 1 Windows Server to communicate between the 2 Clients - Only send/receive via socket, no game code involved Server will use Python for lightweight networking and ability to scale.

Plan: 
  * Week 1 
    - Research over topic and look into what our plan of action will be over the coming weeks. 
    - Created github project and start getting materials in place for server.
  * Week 2 
    - Work on UI of the game as that will be the quickest and easiest part of the project.
  * Week 3 
    - Work on backend and server-side and see how networking is going to work with the program. 
  * Week 4 
    - Work on code to get program running properly by itself (Make sure tic-tac-toe works locally).
  * Week 5 
    - Mesh all components (server, hosts, and program) together and make sure there are no issues with running across multiple computers and a server.
  * Week 6 
    - Go over demo and create presentation based behind it.

# Team members

* Raymond Ren - Back-End Game Programmer (Actual programming for the game)
* Jim Garrison - Networking and Server Engineer (Making sure game is available via network and is scalable to x users)
* Lee Gobin - Front-end Game (using Python tkinter to make game look nice)

# Comments
1. Be more specific about the deliverables. Think about what you are going to demo in the final presentation and complile a list of features to be delivered. (RESOLVED)
2. You should also think about a P2P architecture rather than having a dedicated server, unless you want more than 1 pair to play together at the same time. This might be a good extension of the game. (RESOLVED)

# Getting Started

## How to Install

1. Download Python from [here](https://www.python.org/downloads/).
2. Download zip of github and create a Pycharm project. (Download PyCharm [Here](https://www.jetbrains.com/pycharm/download/).)
3. Make sure Python is working with PyCharm so that code can be run. 
4. Run Program and Client 1 should receive an input to start the game.

## How to Play

1. Run Program via How to install tutorial.
2. Hit Play Game and the interface will pop up in a 3x3 grid.
3. Play Tic-Tac-Toe by clicking a box in the 3x3 grid.
4. First player to get a diagnol of their mark wins the game.

## Features

1. Ability to replay.
2. Game is scalable to x amount of pairs.
3. Retro style (Looks like it's from the 90's, when Dr. Pham went to school.)

## Demo of Gameplay

Watch the Demo [here](https://youtu.be/33ZqmQRGa0M)
