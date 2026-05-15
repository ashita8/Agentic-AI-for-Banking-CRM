from pydantic import BaseModel

class CustomerAnalysisRequest(BaseModel):

    query: str
    minimum_salary: int = 100000
    minimum_credit_score: int = 720
    top_k: int = 10