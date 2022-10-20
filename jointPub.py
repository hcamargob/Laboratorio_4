import rospy
import math
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
        point = JointTrajectoryPoint()
  

        #
        point.positions = [math.radians(0),math.radians(0),math.radians(0),math.radians(0),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('1')
        rospy.sleep(3)

	#
        point.positions = [math.radians(-20),math.radians(20),math.radians(-20),math.radians(20),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('2')
        rospy.sleep(4)

	#
        point.positions = [math.radians(30),math.radians(-30),math.radians(30),math.radians(-30),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('3')
        rospy.sleep(5)
	
        
        #
        point.positions = [math.radians(-90),math.radians(15),math.radians(-55),math.radians(17),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('4')
        rospy.sleep(6)
        
        #
        point.positions = [math.radians(-90),math.radians(45),math.radians(-55),math.radians(45),math.radians(0)]    
        point.time_from_start = rospy.Duration(0.3)
        state.points.append(point)
        pub.publish(state)
        #
        print('5')
        rospy.sleep(4)
        
        print('published command')
        rospy.sleep(2)

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass
