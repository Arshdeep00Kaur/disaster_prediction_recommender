from models import PreventionMeasure, DisasterPrediction
from typing import Dict, List

class PreventionService:
    def get_prevention_measures(self, predictions: List[DisasterPrediction]) -> Dict[str, List[PreventionMeasure]]:
        """Get prevention recommendations based on predicted disasters"""
        prevention_measures = {}
        
        for prediction in predictions:
            disaster_type = prediction.disaster_type
            severity = prediction.severity
            
            if disaster_type == "Flood":
                prevention_measures["Flood"] = self._get_flood_preventions(severity)
            elif disaster_type == "Heat Wave":
                prevention_measures["Heat Wave"] = self._get_heat_wave_preventions(severity)
            elif disaster_type == "Storm":
                prevention_measures["Storm"] = self._get_storm_preventions(severity)
            elif disaster_type == "Wildfire":
                prevention_measures["Wildfire"] = self._get_wildfire_preventions(severity)
                
        return prevention_measures
    
    def _get_flood_preventions(self, severity: str) -> List[PreventionMeasure]:
        preventions = [
            PreventionMeasure(
                title="Avoid flood-prone areas",
                description="Stay away from low-lying areas and river banks",
                urgency="High"
            ),
            PreventionMeasure(
                title="Prepare emergency kit",
                description="Include water, food, medications, and important documents",
                urgency="Medium"
            )
        ]
        
        if severity in ["Severe", "Extreme"]:
            preventions.append(PreventionMeasure(
                title="Consider evacuation",
                description="Follow local authority evacuation instructions if issued",
                urgency="High"
            ))
            preventions.append(PreventionMeasure(
                title="Move to higher ground",
                description="Relocate to higher elevation if in a flood-prone area",
                urgency="High"
            ))
            
        return preventions
    
    def _get_heat_wave_preventions(self, severity: str) -> List[PreventionMeasure]:
        preventions = [
            PreventionMeasure(
                title="Stay hydrated",
                description="Drink plenty of water even if not thirsty",
                urgency="High"
            ),
            PreventionMeasure(
                title="Stay in cool areas",
                description="Use air conditioning or visit public cooling centers",
                urgency="Medium"
            )
        ]
        
        if severity in ["High", "Extreme"]:
            preventions.append(PreventionMeasure(
                title="Check on vulnerable people",
                description="Monitor elderly, young children, and those with health conditions",
                urgency="High"
            ))
            
        return preventions
    
    def _get_storm_preventions(self, severity: str) -> List[PreventionMeasure]:
        preventions = [
            PreventionMeasure(
                title="Stay indoors",
                description="Remain inside and away from windows",
                urgency="High"
            ),
            PreventionMeasure(
                title="Secure loose objects",
                description="Bring in or tie down outdoor furniture and items",
                urgency="Medium"
            )
        ]
        
        if severity == "Severe":
            preventions.append(PreventionMeasure(
                title="Prepare for power outages",
                description="Have flashlights, batteries, and emergency supplies ready",
                urgency="High"
            ))
            
        return preventions
    
    def _get_wildfire_preventions(self, severity: str) -> List[PreventionMeasure]:
        preventions = [
            PreventionMeasure(
                title="Create defensible space",
                description="Clear vegetation around your home",
                urgency="High"
            ),
            PreventionMeasure(
                title="Stay informed",
                description="Monitor local news and emergency alerts",
                urgency="High"
            )
        ]
        
        if severity == "High":
            preventions.append(PreventionMeasure(
                title="Prepare evacuation plan",
                description="Know evacuation routes and have emergency supplies ready",
                urgency="High"
            ))
            
        return preventions