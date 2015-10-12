import rospy

def gen_server(service_name, service_class, node_name=None):
    if node_name is None:
        _node_name = service_name + "_node"
    else:
        _node_name = node_name
    def _server(handler):
        rospy.init_node(_node_name)
        s = rospy.Service(service_name, service_class, handler)
        rospy.spin()
    return _server
