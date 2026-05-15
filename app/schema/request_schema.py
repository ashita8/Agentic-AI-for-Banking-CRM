from pydantic import BaseModel


class CustomerAnalysisRequest(BaseModel):

    query: str