
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from sound_play.libsoundplay import SoundClient

class highlight():
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y


class map_navigation():

	def choose(self):

		choice='q'

		rospy.loginfo("|-------------------------------|")
		rospy.loginfo("|PRESSE A KEY:")

		for index, item in enumerate(self.highlights):
			rospy.loginfo("|'" + index + "': " + item.name)

		rospy.loginfo("|'q': Quit ")
		rospy.loginfo("|-------------------------------|")
		rospy.loginfo("|WHERE TO GO?")

		choice = input()
		return choice

	def __init__(self):

		self.highlights = []
		self.highlights.append(highlight("Cafe", 7.31, 1.46))
		self.highlights.append(highlight("Office 1", 30.0, 20.0	))
		self.highlights.append(highlight("Office 2", -2.35, -0.95))
		self.highlights.append(highlight("Office 3", 35.20, 13.50))

		sc = SoundClient()
		path_to_sounds = "/home/ros/catkin_ws/src/gaitech_edu/src/sounds/"

		# declare the coordinates of interest
		self.goalReached = False

		# initiliaze
        rospy.init_node('map_navigation', anonymous=False)
		choice = self.choose()

		if (choice < len(highlights)):
			self.goalReached = self.moveToHighlight(self.highlights[choice])

		if (choice!='q'):

			if (self.goalReached):
				rospy.loginfo("Congratulations!")
				#rospy.spin()

				sc.playWave(path_to_sounds+"ship_bell.wav")

				#rospy.spin()

			else:
				rospy.loginfo("Hard Luck!")
				sc.playWave(path_to_sounds+"short_buzzer.wav")

		while choice != 'q':
			choice = self.choose()

			if (choice < len(highlights)):
				self.goalReached = self.moveToHighlight(self.highlights[choice])

			if (choice!='q'):

				if (self.goalReached):
					rospy.loginfo("Congratulations!")
					#rospy.spin()

					sc.playWave(path_to_sounds+"ship_bell.wav")

				else:
					rospy.loginfo("Hard Luck!")
					sc.playWave(path_to_sounds+"short_buzzer.wav")


	def shutdown(self):
        # stop turtlebot
        	rospy.loginfo("Quit program")
        	rospy.sleep()


	def moveToHighlight(self, highlight):
		moveToGoal(highlight.x, highlight.y)


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

		goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
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

if __name__ == '__main__':
    try:

	rospy.loginfo("You have reached the destination")
        map_navigation()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated.")
