#!/usr/bin/env python
# license removed for brevity
import rospy
import copy
from std_msgs.msg import String
from tour_bot.msg import goal

# Simple structure to store and pass highlights in the tour area (navigation goals)
class highlight():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class control():

    def __init__(self):
        # Initialize the node
        rospy.init_node('control', anonymous=False)

        # Set up a publisher to the 'goals' topic
        # Sends messages with the requested next highlight
        # map_navigation.py recieves these messages and acts on them
        self.goalPublisher = rospy.Publisher('goals', goal, queue_size=10)

        # Subscribe to the 'result' topc so this node knows when to prompt for next destination
        rospy.Subscriber('result', String, self.callback)

        # Creates the static list of highlights that the user can choose from
        self.highlights = self.createHighlightsList()

        # This stores the highlight the robot is currently navigating to
        self.currentHighlight = None
        # This stores a list of highlights to go to for the tour
        self.plannedHighlights = []

        self.promptUserForNextDestination()

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

    def createHighlightsList(self):
        result_highlights = []

        # Change or add desired highlights here
        # Getting the coordinates:
        # Run `rostopic echo move_base_simple/goal`
        # Set a 2d Nav Goal in RViz at your desired point
        result_highlights.append(highlight("A", 1.1523, -0.1251))
        result_highlights.append(highlight("B", 2.6137, 1.3885))
        result_highlights.append(highlight("C", -0.2931, 1.5051))
        result_highlights.append(highlight("D", 1.3457, 2.5117))

        return result_highlights

    def promptUserForNextDestination(self):
        # Default choice to quit
        self.choice = 'q'

        self.printUserOptions()

        # Accept user choice
        self.choice = input()

        if self.choice == 'q':
            self.callback("")
        else:
            if self.choice == 't':
                self.plannedHighlights = copy.deepcopy(self.highlights)
                rospy.loginfo("Starting tour")
                self.goToHighlight(self.plannedHighlights.pop())
            elif (choice < len(self.highlights)):
                self.goToHighlight(self.highlights[choice])
        # wait for map_navigation.py to finish moving

    def printUserOptions(self):
        rospy.loginfo("|-------------------------------|")
        rospy.loginfo("| Choose a destination or task:")

        # Print an option for each highilgh in the static highlights list
        for index, item in enumerate(self.highlights):
            rospy.loginfo("| " + str(index) + " : " + item.name)

        rospy.loginfo("| 't' : Tour ")
        rospy.loginfo("| 'q' : Quit ")
        rospy.loginfo("|-------------------------------|")
        rospy.loginfo("| PRESS A KEY:")

    def goToHighlight(self, highlightIn):
        # Set instdance currentHighlight so that status prinouts in callback can be descriptive
        self.currentHighlight = highlightIn

        rospy.loginfo("Going to " + highlightIn.name)
        new_goal = self.highlightToGoal(highlightIn)
        self.goalPublisher.publish(new_goal)

    def highlightToGoal(self, highlightIn):
        new_goal = goal()
        new_goal.name = highlightIn.name
        new_goal.x = highlightIn.x
        new_goal.y = highlightIn.y
        return new_goal

    def callback(self, data):
        if self.choice !='q':
            # User did not choose quit

            if str(data) == "data: Success":
                rospy.loginfo("Robot made it to " + self.currentHighlight.name + " !")
            else:
                rospy.logwarn("Robot failed to get to " + self.currentHighlight.name)

            if len(self.plannedHighlights) > 0:
                # There are still highlights left in the tour
                # So go to the next highlight
                self.goToHighlight(self.plannedHighlights.pop())
            else:
                # There are no planned highlights in the tour
                # So ask the user for the next option
                self.promptUserForNextDestination()
        else:
            # User chose quit
            rospy.loginfo("Quitting")
            rospy.signal_shutdown("User quit")


if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        rospy.logwarn("control node terminated.")
