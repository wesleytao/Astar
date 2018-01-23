# Update 1/22/2018 #
* load_data has not been organized
* has built a 3D space-time configuration space by extending 2D maps across time

## Solutions with Astar ##
* brute force: loop over destination with time = 1:end, run astar
* add an artificial terminal node that connects destination at all time, run astar from start to terminal

# Tianchi Future Challenge #

* This repo contains the information for [Helping Balloons Navigate the Weather](https://tianchi.aliyun.com/competition/introduction.htm?spm=5176.100066.0.0.9c2f5d8JyVMlI&raceId=231622)

* /src contains the code for load data, and A star algorithm

* /data folder is ignored and can be downloaded from above link, change the local path your /data

* A star in known, time-varying map can be solved by augmenting the state/configuration space 

# Reference #
* [A star introduction](http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html)
* Time-varing problems: Lavalle, [Planning Algorithms](http://planning.cs.uiuc.edu/), Chapter 7.1 

