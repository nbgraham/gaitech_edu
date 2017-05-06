#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from gaitech_edu.msg import goal
from std_msgs.msg import String


class map_navigation():

    def __init__(self):

        # declare the coordinates of ros
        self.goalReached = False

        # initiliaze
        rospy.init_node('map_navigation', anonymous=False)

        rospy.Subscriber("goals", goal, self.callback)
        self.pub = rospy.Publisher('result', String, queue_size=10)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

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
            self.pub.publish("Success")
            return True

        else:
            rospy.loginfo("The robot failed to reach the destination")
            self.pub.publish("Failure")
            return False

    def callback(self, data):
        rospy.loginfo("New goal: %s", data.name)
        self.moveToGoal(data.x, data.y)


if __name__ == '__main__':
    try:
        rospy.loginfo("You have reached the destination")
        map_navigation()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated.")
