from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor 
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry import trace


class Telemetry:

    traceProvider = None

    def __init__(self) -> None:

        try: 

            otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

            spanProcessor = BatchSpanProcessor(otlp_exporter)
            self.traceProvider = TracerProvider(resource=Resource.create({"service.name": "oltp_python_demo"}))
            self.traceProvider.add_span_processor(spanProcessor)

        except Exception as msg:
            print("This Error Message: {}".format(msg))

    def getTracer(self):

        return trace.get_tracer(tracer_provider=self.traceProvider, instrumenting_module_name="oltp_python_demo")

        
