#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from gaitech_edu.msg import goal

class highlight():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class map_navigation():

    def choose(self):

        choice = 'q'

        rospy.loginfo("|-------------------------------|")
        rospy.loginfo("| Choose a destination:")

        for index, item in enumerate(self.highlights):
            rospy.loginfo("|'" + str(index) + "': " + item.name)

        rospy.loginfo("|'q': Quit ")
        rospy.loginfo("|-------------------------------|")
        rospy.loginfo("| PRESS A KEY:")

        choice = input()
        return choice

    def __init__(self):

        self.highlights = []
        self.highlights.append(highlight("Cafe", 14, 13))
        self.highlights.append(highlight("Office 1", 28, 13))
        self.highlights.append(highlight("Office 2", 30.5, 14))
        self.highlights.append(highlight("Office 3", 35, 14))

        # declare the coordinates of ros
        self.goalReached = False

        # initiliaze
        rospy.init_node('map_navigation', anonymous=False)
        choice = self.choose()

        if (choice < len(self.highlights)):
            self.goalReached = self.moveToHighlight(self.highlights[choice])

        if (choice!='q'):

            if (self.goalReached):
                rospy.loginfo("Congratulations!")
                #rospy.spin()

            else:
                rospy.loginfo("Hard Luck!")

        while choice != 'q':
            choice = self.choose()

            if (choice < len(self.highlights)):
                self.goalReached = self.moveToHighlight(self.highlights[choice])

            if (choice!='q'):

                if (self.goalReached):
                    rospy.loginfo("Congratulations!")
                    #rospy.spin()

                else:
                    rospy.loginfo("Hard Luck!")

    def shutdown(self):
        # stop turtlebot
            rospy.loginfo("Quit program")
            rospy.sleep()


    def moveToHighlight(self, highlight):
        self.moveToGoal(highlight.x, highlight.y)


    def moveToGoal(self,xGoal,yGoal):

        #define a client for to send goal requests to the move_base server through a SimpleActionClient
        ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

        #wait for the action server to come up
        while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
            rospy.loginfo("Waiting for the move_base action server to come up")


        goal = MoveBaseGoal()

        #set up the frame parameters
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        # moving towards the goal*/

        goal.target_pose.pose.position = Point(xGoal,yGoal,0)
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0

        rospy.loginfo("Sending goal location ...")
        ac.send_goal(goal)

        ac.wait_for_result(rospy.Duration(60))

        if(ac.get_state() ==  GoalStatus.SUCCEEDED):
            rospy.loginfo("You have reached the destination")
            return True

        else:
            rospy.loginfo("The robot failed to reach the destination")
            return False

def callback(data):
    result = str(data.x) + ", " + str(data.y) + " N: " + data.name
    rospy.loginfo("I heard %s", result)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("goals", goal, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

'''
if __name__ == '__main__':
    try:
        rospy.loginfo("You have reached the destination")
        map_navigation()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated.")
'''
