import uvicorn
from datetime import datetime
from fastapi import FastAPI
from opentelemetry import trace
from repository.factory.telemetry import Telemetry
from service.getCompany_Service import Service
from model.company import Company

class API:

    app = FastAPI(title="python-opentelemetry-demo")

    @app.get("/", summary="Endpoint to Get")
    def getCompany() -> Company:

        tracer = Telemetry().getTracer()
        CompanyID = 0

        with tracer.start_as_current_span("API::getCompany") as parentSpan:

            CompanyID = Service.getCompany_Service()

            myCompany = Company(name="Company A", 
                                description="This is Company A",
                                companyId=CompanyID, 
                                dateTime=str(datetime.now()), 
                                traceId=trace.format_trace_id(parentSpan.get_span_context().trace_id))
        return myCompany



if __name__ == "__main__":
    uvicorn.run(API().app, host="0.0.0.0", port=8000, reload=False)