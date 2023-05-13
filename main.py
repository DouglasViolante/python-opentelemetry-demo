import uvicorn
from datetime import datetime
from internal.config import Config
from internal.telemetry.configTelemetry import Telemetry
from service.getCompany_Service import Service
from fastapi import Response, Request
from model.company import Company
from opentelemetry import trace

class Controller:

    @Config.app.get("/", summary="Endpoint to Get Company Info")
    async def getCompany(response: Response, request: Request) -> Company:

        tracer = Config.tracer
        CompanyBudget = 0

        if (request.headers.get('x-trace-id') and request.headers.get('x-span-id')) != None:
            ctx = Telemetry.getRemoteTraceContext(request.headers.get('x-trace-id'), request.headers.get('x-span-id'))
        else:
            ctx = None

        with tracer.start_as_current_span(context=ctx, name="Controller::getCompany") as parentSpan:

            CompanyBudget = Service.getCompany_Service()

            myCompany = Company(companyId=1,
                                name="Company A", 
                                description="This is Company A",
                                budget=CompanyBudget,
                                dateTime=str(datetime.now()), )
            
            response.headers['x-trace-id'] = trace.format_trace_id(parentSpan.get_span_context().trace_id)
            response.headers['x-span-id'] = trace.format_trace_id(parentSpan.get_span_context().span_id)

        return myCompany

if __name__ == "__main__":
    uvicorn.run(Config.app, host="0.0.0.0", port=8000, reload=False)