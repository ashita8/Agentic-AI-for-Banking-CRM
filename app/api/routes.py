from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze-customers")
def analyze_customers():

    return {
        "message": "Customer analysis started"
    }