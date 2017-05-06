# Robot Tour Guide
## Set-up
1. Create a new package.  
`cd ~/catkin_ws/src`  
`catkin_create_pkg gaitech_edu`  

2. Clone this repo into new project  
  `cd ~/catkin_ws/src/gaitech_edu`  
  `rm *`  
  `git clone https://github.com/nbgraham/gaitech_edu.git .`  


### Run on real robot
3. Setup in real world  
  Start it at position C because that is the initial pose in turtlebot_stage_psu.launch

3. Setup on turtlebot through ssh (use USB to move entire gaitech_edu package onto turtlebot)  
  `roslaunch gaitech_edu actual_turtlebot.launch`  
  Make sure to remove the Gmapping from the end of 3dsensor.launch if its still there or else the planned map will be overridden by the map that slam mapping is creating  
  ```xml
  <!-- Gmapping -->
  <arg name="custom_gmapping_launch_file" default="$(find turtlebot_navigation)/launch/includes/gmapping/$(arg 3d_sensor)_gmapping.launch.xml"/>
  <include file="$(arg custom_gmapping_launch_file)"/>
  ```

4. Run the project on rowork  
  `rosrun gaitech_edu actual_navigation.py` This is the actual planning that sends velocity commands  
  `rosrun gaitech_edu control.py` This is just a user interface that send goals to map_navigation

  Open rviz on rowork `rviz`  
  Re-open RVIZ every time you run the launch file

### Run in simulation
Run the project  
`roslaunch gaitech_edu map_navigation_stage_psu.launch`  
`rosrun gaitech_edu control.py`

## Possible issues
 - If you get an issue about contacting X Display, try `ssh -X turtlebot@<host>`  
 - If you get "no module gaitech_edu.msg" make sure to `catkin_make` and `source ~/catkin_ws/devel/setup.bash`  
 - If you get "could not find executable <name>.py", make sure it has executable permissions `chmod +x <name>.py`

## To Do
 - [x] Create a world (probably need to create an actual environment and use the robot to map it
 - [x] Choose new points as destinations and add those options to the command line options
 - [x] Add an option to tour all of the destinations
 - [x] Reduce status print statements and add print outs for options and description for each destination
 - [ ] Document everything we have done


 [Original gaitech_wdu repo](https://github.com/aniskoubaa/gaitech_edu)  
