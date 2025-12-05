"""This is a Apache Nifi Python Processor"""
from nifiapi.flowfiletransform import FlowFileTransform, FlowFileTransformResult
import json

@use_case(
    description="Schaut in eine JSON und sagt wohin geloggt wird."
    notes="Das ist ein toller Prozessor"
)

class LoggerTest(FlowFileTransform):
    """Class representing the the a Processor which write
    hello world to the attribute"""
    class Java:
        """extends the Java FlowFileTransform Processor"""
        implements = ['org.apache.nifi.python.processor.FlowFileTransform']
    class ProcessorDetails:
        """set up the details of the processor"""
        version = 'v0.0.1-beta'
        description =  "Dieser Prozessor entscheidet, ob etwas in eine Datei oder in HTTP geloggt wird."
        tags = ['ordix', 'sparkasse', 'logging', 'test', 'demo']


    def __init__(self, **kwargs):
        pass

    FILE = Relationship(
        name="file",
        description="If the log_type is 'file', route to this relationship",
        auto_terminated=False
    )

    HTTP = Relationship(
        name="http",
        description="If the log_type is 'http', route to this relationship",
        auto_terminated=False
    )

    INVALID = Relationship(
        name="invalid",
        description="If the JSON is invalid or log_type is neither 'file' nor 'http'",
        auto_terminated=False
    )

    relationships = [
        FILE,
        HTTP,
        INVALID
    ]

    def getRelationships(self):
        """Function to initialise the relationships"""
        return self.relationships

    def onScheduled(self, context):
        """Function that runs when the processor is started"""
        self.logger.debug("LogRouter processor scheduled successfully")

    def transform(self, context, flowfile):
        """Function to transform the flowfile format"""

        try:
            content_as = flowfile.getContentsAsBytes()

            conent_str = content_as.decode('utf-8')

            self.logger.info(f"Content ist angekommen und sieht so aus: {conent_str}")

            data_as_json = json.loads(conent_str)

            log_type = data_as_json['log_type']
            log_message = data_as_json['log_message']

            self.logger.debug(f"Log Type ist: {log_type}")
            self.logger.debug(f"Log Mesage ist: {log_message}")

            if log_type == 'file': 
                return FlowFileTransformResult(relationship='file', contents=content_as, attributes={'log_type': log_type})
            elif log_type == 'http':
                return FlowFileTransformResult(relationship='http', contents=content_as, attributes={'log_type': log_type})
            else: 
                return FlowFileTransformResult(relationship='invalid', contents=content_as, attributes={'log_type': 'Unbekannt'})

            

        except: 
            return FlowFileTransformResult(relationship = "invalid")



        # return FlowFileTransformResult(relationship = "success",
        #                                contents = "Hello World",
        #                                attributes = {"greeting": "hello"})