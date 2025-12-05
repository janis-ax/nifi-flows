"""This is a Apache Nifi Python Processor"""
from nifiapi.flowfiletransform import FlowFileTransform, FlowFileTransformResult

class WriteHelloWorld(FlowFileTransform):
    """Class representing the the a Processor which write
    hello world to the attribute"""
    class Java:
        """extends the Java FlowFileTransform Processor"""
        implements = ['org.apache.nifi.python.processor.FlowFileTransform']
    class ProcessorDetails:
        """set up the details of the processor"""
        version = 'v.2025.3.6'

    def __init__(self, **kwargs):
        pass

    def transform(self, context, flowfile):
        """Function to transform the flowfile format"""
        return FlowFileTransformResult(relationship = "success",
                                       contents = "Hello World",
                                       attributes = {"greeting": "hello"})
