from fastapi import APIRouter, HTTPException
from .models import Query, Response
from core.travel_assistant import TravelAssistant

router = APIRouter()
travel_assistant = TravelAssistant()

@router.post("/itinerary", response_model=Response)
async def get_itinerary(query: Query):
    try:
        response = travel_assistant.get_response(query.question)
        return Response(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 