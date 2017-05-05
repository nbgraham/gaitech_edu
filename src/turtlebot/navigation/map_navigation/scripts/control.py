#!/usr/bin/env python
# license removed for brevity
import rospy
import copy
from std_msgs.msg import String
from gaitech_edu.msg import goal

class highlight():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class control():

    def __init__(self):
        self.plannedHighlights = []

        self.highlights = []
        self.highlights.append(highlight("A", 1.1523, -0.1251))
        self.highlights.append(highlight("B", 2.6137, 1.3885))
        self.highlights.append(highlight("C", -0.2931, 1.5051))
        self.highlights.append(highlight("D", 1.3457, 2.5117))

        rospy.init_node('control', anonymous=False)
        self.pub = rospy.Publisher('goals', goal, queue_size=10)
        rospy.Subscriber('result', String, self.callback)

        self.choice = self.choose()

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()


    def choose(self):
        choice = 'q'

        rospy.loginfo("|-------------------------------|")
        rospy.loginfo("| Choose a destination:")

        for index, item in enumerate(self.highlights):
            rospy.loginfo("|'" + str(index) + "': " + item.name)

        rospy.loginfo("|'t': Tour ")
        rospy.loginfo("|'q': Quit ")
        rospy.loginfo("|-------------------------------|")
        rospy.loginfo("| PRESS A KEY:")

        choice = input()

        if choice == 'q':
            self.choice = 'q'
            self.callback("Success")
        else:
            if choice == 't':
                self.plannedHighlights = copy.deepcopy(self.highlights)
                rospy.loginfo("Starting tour")
                self.goToHighlight(self.plannedHighlights.pop())
            elif (choice < len(self.highlights)):
                self.goToHighlight(self.highlights[choice])
            # wait for completing move

        return choice

    def goToHighlight(self, highlightIn):
        cur_highlight = highlightIn
        rospy.loginfo("Going to " + cur_highlight.name)
        new_goal = self.highlightToGoal(cur_highlight)
        self.pub.publish(new_goal)

    def highlightToGoal(self, highlightIn):
        new_goal = goal()
        new_goal.name = highlightIn.name
        new_goal.x = highlightIn.x
        new_goal.y = highlightIn.y
        return new_goal

    def callback(self, data):
        if (self.choice !='q'):
            if str(data) == "data: Success":
                rospy.loginfo("Congratulations!")
            else:
                rospy.loginfo("Hard Luck!")

            if len(self.plannedHighlights) > 0:
                self.goToHighlight(self.plannedHighlights.pop())
            else:
                self.choice = self.choose()
        else:
            rospy.loginfo("Quitting")
            rospy.signal_shutdown("User quit")


if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass
