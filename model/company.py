from pydantic import BaseModel

class Company(BaseModel):
    companyId:      int
    name:           str
    description:    str | None = None
    budget:         float
    dateTime:       str
