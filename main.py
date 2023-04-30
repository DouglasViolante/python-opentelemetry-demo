from datetime import datetime
from fastapi import FastAPI
import uvicorn
#from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from repository.factory.telemetry import Telemetry
from model.company import Company

class API:

    app = FastAPI(title="python-opentelemetry-demo")
    FastAPIInstrumentor.instrument_app(app, tracer_provider=Telemetry().traceProvider)

    @app.get("/")
    def getCompany() -> Company:
        # current_span = trace.get_current_span() 
        # current_span.set_attribute("root.lol", "I LOLED")

        myCompany = Company(name="Company A", 
                            description="This is Company A", 
                            dateTime=str(datetime.now()), 
                            traceId="")

        myCompany.traceId = Telemetry.newSpan("main::getCompany")

        return myCompany



if __name__ == "__main__":
    uvicorn.run(API().app, host="0.0.0.0", port=8000, reload=False)