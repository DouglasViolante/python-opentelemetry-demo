from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor 
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry import trace
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.trace import NonRecordingSpan, SpanContext, TraceFlags

class Telemetry:

    traceProvider = None
    meterProvider = None

    def __init__(self) -> None:

        try: 

            otlpExporter = "http://localhost:4317"

            resource = Resource.create(attributes={"service.name" : "otlp_python_demo"})

            # Metrics Configuration
            reader = PeriodicExportingMetricReader(OTLPMetricExporter(endpoint=otlpExporter, insecure=True))
            self.meterProvider = MeterProvider(resource=resource, metric_readers=[reader])

            # Traces Configuration
            spanProcessor = BatchSpanProcessor(OTLPSpanExporter(endpoint=otlpExporter, insecure=True))
            self.traceProvider = TracerProvider(resource=resource)
            self.traceProvider.add_span_processor(spanProcessor)

        except Exception as msg:
            print("Fail, Could not Start Telemetry Backend! {} ".format(msg))

    def getTracer(self):
        return trace.get_tracer(tracer_provider=self.traceProvider, instrumenting_module_name="oltp_python_demo")
    
    def getMeter(self):
        return metrics.get_meter(meter_provider=self.meterProvider, name="oltp_python_demo")
    
    def getRemoteTraceContext(traceId, spanId):
        context = SpanContext(
            trace_id    = int(traceId, 16),
            span_id     = int(spanId, 16),
            is_remote   = True,
            trace_flags = TraceFlags(0x01)
        )
        return trace.set_span_in_context(NonRecordingSpan(context=context))
    
    def startMeters(self):

        meter = self.getMeter()

        counter_company_budget = meter.create_counter(name="company.budget", description="Accumulative Company Budget", unit="{Dolar}")

        return {"counter_company_budget" : counter_company_budget}

        
