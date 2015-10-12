import rospy

def client_proxy(service_name, service_class):
    def _proxy(fn):
        proxy = get_client(service_name, service_class)
        def __proxy(*args, **kwargs):
            return proxy(*args, **kwargs)
        return __proxy
    return _proxy

def get_client(service_name, service_class):
    rospy.wait_for_service(service_name)
    try:
        return rospy.ServiceProxy(service_name, service_class)
    except rospy.ServiceException as se:
        rospy.logfatal("ROSVendor.core.generator.client_proxy: cannot found service \"%s\".", service_name)
        raise se
    

