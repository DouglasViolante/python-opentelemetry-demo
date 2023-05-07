from pydantic import BaseModel

class Company(BaseModel):
    name:           str
    description:    str | None = None
    companyId:      int
    traceId:        str = ""
    dateTime:       str
