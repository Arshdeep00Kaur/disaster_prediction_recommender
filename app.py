from fastapi import FastAPI, HTTPException, Query
from models import PredictionResponse
from weather_service import WeatherService
from disaster_predictor import DisasterPredictor
from prevention_service import PreventionService
import uvicorn

app = FastAPI(
    title="Disaster Prediction and Prevention API",
    description="API for predicting potential disasters and recommending preventive measures",
    version="1.0.0"
)

weather_service = WeatherService()
disaster_predictor = DisasterPredictor()
prevention_service = PreventionService()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Disaster Prediction and Prevention API"}

@app.get("/api/predict", response_model=PredictionResponse)
def predict_disasters(location: str = Query(..., description="City name or lat,long coordinates")):
    """
    Get disaster predictions and prevention recommendations for a location
    """
    try:
        # Get weather data
        weather_data, location_data = weather_service.get_current_weather(location)
        
        # Predict potential disasters
        predictions = disaster_predictor.predict_disasters(weather_data)
        
        # Get prevention recommendations
        preventions = prevention_service.get_prevention_measures(predictions)
        
        # Return response
        return PredictionResponse(
            location=location_data,
            weather=weather_data,
            predictions=predictions,
            preventions=preventions
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/weather")
def get_weather(location: str = Query(..., description="City name or lat,long coordinates")):
    """
    Get current weather data for a location
    """
    try:
        weather_data, location_data = weather_service.get_current_weather(location)
        return {
            "location": location_data.dict(),
            "weather": weather_data.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/forecast")
def get_forecast(
    location: str = Query(..., description="City name or lat,long coordinates"),
    days: int = Query(3, description="Number of forecast days (1-3)")
):
    """
    Get weather forecast for a location
    """
    try:
        forecast = weather_service.get_forecast(location, days)
        return forecast
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)