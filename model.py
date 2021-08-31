from pydantic import BaseModel, Field


# Models
class JobList(BaseModel):
    id: str
    title: str
    description: str
    create_at: str


class JobEntry(BaseModel):
    title: str = Field(..., example="title")
    description: str = Field(..., example="Desc")


class JobUpdate(BaseModel):
    id: str = Field(..., example="Enter your id")
    title: str = Field(..., example="Developer")
    description: str = Field(..., example="SD")


class JobDelete(BaseModel):
    id: str = Field(..., example="Enter your id")
