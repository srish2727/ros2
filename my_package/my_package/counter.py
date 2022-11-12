import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64     
     
     
class NumberCounterNode(Node): # Write Class Name Here
    def __init__(self):
        super().__init__("   ") # Write Node Name Here
        self.counter = 0
        # TODO
        # create a subscriber node to subscribe the number
        # create a publisher to publish the count value
        
        self.get_logger().info("Number Counter Node Started")
   
   
    def callback_number(self, msg):
        # TODO 
        # increment the counter as the msg is received
        # initialise the new message of type Int64 to publish the counter value
        # publish the counter value 
        self.get_logger().info(str(self.counter))    
        
        
def main(args=None):
        rclpy.init(args=args)
        node = NumberCounterNode() # Write Class Name Here
        rclpy.spin(node)
        rclpy.shutdown()
     
if __name__ == "__main__":
	main()