from dataclasses import dataclass

from fastapi import FastAPI
from internal.telemetry import configTelemetry


@dataclass
class Config:
    
    tracer = configTelemetry.Telemetry().getTracer()
    meter = configTelemetry.Telemetry().getMeter()
    counters = configTelemetry.Telemetry().startMeters()
    app = FastAPI(title="python-opentelemetry-demo")