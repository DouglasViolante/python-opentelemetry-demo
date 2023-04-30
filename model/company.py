from pydantic import BaseModel

class Company(BaseModel):
    name: str
    description: str | None = None
    traceId: str 
    dateTime: str
