#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from gaitech_edu.msg import goal

class highlight():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class control():

    def __init__(self):
        self.highlights = []
        self.highlights.append(highlight("Cafe", 14, 13))
        self.highlights.append(highlight("Office 1", 28, 13))
        self.highlights.append(highlight("Office 2", 30.5, 14))
        self.highlights.append(highlight("Office 3", 35, 14))

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

        rospy.loginfo("|'q': Quit ")
        rospy.loginfo("|-------------------------------|")
        rospy.loginfo("| PRESS A KEY:")

        choice = input()

        if choice == 'q':
            self.choice = 'q'
            self.callback("Success")
        else:
            if (choice < len(self.highlights)):
                cur_highlight = self.highlights[choice]
                rospy.loginfo("Going to " + cur_highlight.name)
                new_goal = self.highlightToGoal(cur_highlight)
                self.pub.publish(new_goal)

                # wait for completing move

        return choice


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
            self.choice = self.choose()
        else:
            rospy.loginfo("Quitting")


if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass
