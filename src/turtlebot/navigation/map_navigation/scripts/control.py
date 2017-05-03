#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from gaitech_edu.msg import goal

def talker():
    pub = rospy.Publisher('goals', goal, queue_size=10)
    rospy.init_node('control', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    c_goal = goal()
    c_goal.x = 5
    c_goal.y = 10
    c_goal.name = "asdg"
    while not rospy.is_shutdown():
        pub.publish(c_goal)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
