from random import randint
from opentelemetry import trace
from repository.factory.telemetry import Telemetry


class Service:

    @classmethod
    def getCompany_Service(self):

        tracer = Telemetry().getTracer()

        myCompanyId = 0

        with tracer.start_as_current_span("Service::getCompany_Service") as childSpan:
            
            try:
                myCompanyId = randint(1, 1000)

                if myCompanyId > 500:

                    raise Exception("Ops, Its Bigger than 500!!!")
            except Exception as msg:

                childSpan.record_exception(msg)


        return myCompanyId
