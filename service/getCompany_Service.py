from random import randint
from internal.config import Config
from datetime import datetime

class Service:

    @classmethod
    def getCompany_Service(self):

        tracer = Config.tracer

        myCompanyBudget = 0

        with tracer.start_as_current_span("Service::getCompany_Service") as childSpan:
            try:
                myCompanyBudget = randint(1, 10000)

                Config.counters["counter_company_budget"].add(amount=myCompanyBudget, attributes={"Month" : datetime.today().month})

                if myCompanyBudget < 100:
                    raise Exception("Ops, We Broke!")
            except Exception as msg:
                childSpan.record_exception(msg)

        return myCompanyBudget
