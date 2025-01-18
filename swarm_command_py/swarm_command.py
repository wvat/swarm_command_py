import rclpy
from rclpy.node import Node 
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
import textual
from .interface import Interface

class Command(Node):
    def __init__(self):
        super().__init__('command')
        self.get_logger().info('Command node started')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        app = Interface()
        app.run()

def main(args=None):
    rclpy.init(args=args)
    command_node = Command()

    rclpy.spin(command_node)
    command_node.destroy_node()
    rclpy.shutdown()

