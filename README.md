Ping Pong Game - Lab 4 (Software Engineering, Sem 5, PES University)


Overview

A real-time Ping Pong game built with Python and Pygame.
Human vs AI paddle
Smooth AI movement, predictive ball collision
Score tracking with game over screen
Replay with Best-of 3, 5, 7 rounds
Sound effects for paddle hits, wall bounce, and scoring
Winner text: Green for Player, Red for AI

Folder Structure
pygame-pingpong/
├── main.py
├── requirements.txt
├── README.md
├── assets/           # .wav sound files (paddle_hit, wall_bounce, score)
└── game/
    ├── game_engine.py
    ├── paddle.py
    └── ball.py 

Installation & Run

Install dependencies:
pip install -r requirements.txt

Run the game:
python main.py


Controls:

W → Move up
S → Move down

Game Over / Replay:

After a player reaches the winning score, press 3, 5, or 7 to replay (Best-of rounds)
Press ESC to exit
Changes / Features
Fixed ball collision for high-speed accuracy
Added game over and replay functionality
Smoothed and made AI more competitive
Added sound effects for paddle hit, wall bounce, and scoring
Conditional winner text colors (Green: Player, Red: AI)
