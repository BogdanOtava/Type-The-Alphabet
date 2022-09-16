## Description
A simple instrument I created when I first started learning Python. I had bought a new keyboard and wanted to get used to it so after trying a few similar games on Google, I tried making something myself.

## How It Works
After running the program, you'll need to add your username. A menu will pop up that has four options: play game, see scoreboard, change username and exit menu. Choosing the first option will start a countdown, and then you can start typing the alphabet. Press 'Enter' after you're done and if you typed it correctly it will tell you the time. Also, every correct attempt will be saved in a .txt file. You can see the top 10 best scores by choosing the second option, see scoreboard. The third option will simply change the username and the fourth will close the program.

It uses a few modules such as: 
  * pathlib module to create the .txt file which saves the scores in the working directory;
  * the alphabet string is taken from the string module;
  * the time is measured using datetime module;
  * from time, used sleep function before reprinting the menu.
