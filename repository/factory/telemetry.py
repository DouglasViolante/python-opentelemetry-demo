from opentelemetry.exporter.zipkin.proto.http import ZipkinExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor 
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry import trace


class Telemetry:

    traceProvider = None

    def __init__(self) -> None:

        try: 

            zipkinExporter = ZipkinExporter(endpoint="http://localhost:9411/api/v2/spans")

            spanProcessor = BatchSpanProcessor(zipkinExporter)
            self.traceProvider = TracerProvider(resource=Resource.create({"service.name": "oltp_python_demo"}))
            self.traceProvider.add_span_processor(spanProcessor)

        except Exception as msg:
            print("This Error Message: {}".format(msg))


    def newSpan(spanSource):
        current_span = trace.get_current_span() 

        current_span.set_attribute("span.source", spanSource)

        return trace.format_trace_id(current_span.get_span_context().trace_id)

        
