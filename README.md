[gaitech repo](https://github.com/aniskoubaa/gaitech_edu)  
All the relevant code seems to be in gaitech_edu/src/turtlebot/navigation/map_navigation/scripts/map_navigation.py

# robot-tour-guide
## Set-up
1. Create a new package.  
`cd ~/catkin_ws/src`  
`catkin_create_pkg gaitech_edu`
2. Clone this repo into new project  
  `cd ~/catkin_ws/src/gaitech_edu`  
  `rm *`  
  `git clone https://github.com/nbgraham/gaitech_edu.git .`  
3.
 - Update keys (maybe)  
`sudo sh -c 'echo "deb http://code.ros.org/packages/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list'`  
`wget http://code.ros.org/packages/ros.key -O - | sudo apt-key add -`  
`sudo apt-get update`
4. Move amcl.launch.xml from ros/indigo/share/turtlebot_navigation/launch/includes/amcl/ to                                        ros/indigo/share/turtlebot_navigation/launch/includes  (we need to reverse this step)
  `sudo mv /opt/ros/indigo/share/turtlebot_navigation/launch/includes/amcl/amcl.launch.xml /opt/ros/indigo/share/turtlebot_navigation/launch/includes`
5. Run the project  
    `roslaunch gaitech_edu map_navigation_stage_psu.launch`  
    `rosrun gaitech_edu control.py`

## Possible issues
If you get an issue about contacting X Display, try `ssh -X`  
If you get "no module gaitech_edu.msg" make sure to `source ~/catkin_ws/devel/setup.bash`  

## To Do
 - [ ] Create a world (probably need to create an actual environment and use the robot to map it
 - [ ] Choose new points as destinations and add those options to the command line options
 - [ ] Add an option to tour all of the destinations
 - [ ] Reduce status print statements and add print outs for options and description for each destination
 - [ ] Document everything we have done and pretend we did more





Gaitech ReadMe
---------

Welcome to Gaitech’s Education Portal!
================================
Gaitech is pround to provide you a comprehensive educational framework on Robot Operating System (ROS). We provide a series of online tutorials on ROS that will help you getting familiar with ROS.
Website: http://edu.gaitech.hk

FAQs about Gaitech EDU
=====================
What is Gaitech EDU?
-------------------
Gaitech EDU is an educational website on robotics and in particular on Robot Operating System (ROS). The objective is to provide an easy-to-follow educational content that helps in better mastering the concepts of ROS and promoting its use for developing robotics software. Gaitech company strives to contribute to the development of ROS and provides its customers and ROS users with technical support and an open education framework to learn ROS.

How does it differ from ROS Wiki documentation?
-----------------------------------------------
Gaitech Education website is NOT meant to be a substitue of ROS wiki documentation website, but a complementary website that is more oriented to providing education and teaching material. In principle, any ROS user should first go through the ROS wiki beginners tutorials, at least for installation, setting up the environment and understanding ROS framework. Gaitech EDU website provide high-quality tutorials in both textual and video format with open source code and instruction of usage. Some of the tutorials in ROS Wiki documentation were reproduced with more details and concrete illustration for faster introduction to the main concepts such as publisher/subscriber paradigm, topics, messages, etc. In addition, Gaitech EDU website provides a educational content on the Turtlebot robot for both simulated robots and real robots.

How Tutorials are designed?
--------------------------
As the primary objective of Gaitech EDU is to promote education of ROS, tutorials were designed with teaching objectives in mind. Each tutorial starts with Learning outcomes that the student or the learned is expected to know at the end of the tutorial. Then, the tutorial is provided in both textual format and/or video illustrations. Finally, a series of review questions are proposed so that the student self-evaluation his understanding about the concepts presented in the tutorial.

How to use Gaitech EDU?
-----------------------
Gaitech EDU can be helpful in diffent ways. First, it can be used by self-learners to consolidate their understanding of ROS and robotics by going through the different tutorials. Furthermore, it can be used by Turtlebot robot users as we provide a series of tutorials with illustration on how to test, use, and develop program for the turtlebot robot in both simulation and real robot, which is the defact-standard robot for ROS learned. Third, it can be used as a teaching resources by instructors of courses. If you are an instructor and would like to use the education content of the Gaitech EDU website, please contact us, and send us your comments. We will add instructors who are using Gaitech EDU website and link to their courses’ webpages.

Will the current content of the Gaitech EDU website be maintaned and updated?
-----------------------------------------------------------------------------
Yes. Gaitech EDU strives towards updating the educational content and maintaining it. Several tutorials will be added regularly and existing tutorials would also be updated when needed and based on feedback and comment of Gaitech EDU users. If you are interested to stay tuned with any content update, you can subscribe to this forum http://forum.gaitech.hk. However, there are no pre-defined periods of updates.

Subscribe to Gaitech EDU Mailing List
=====================================
For technical support and getting responses to queries related to Gaitech EDU website, you need to register to the forum http://forum.gaitech.hk.
You can also subscribe to Gaitech EDU Mailing List to receive latest news http://lists.gaitech.coins-lab.org/listinfo.cgi/gaitech_edu_users-gaitech.coins-lab.org
