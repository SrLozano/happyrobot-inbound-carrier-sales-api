from datetime import datetime

from pydantic import BaseModel, Field


class CarrierVerificationResponse(BaseModel):
    is_eligible: bool = Field(..., description="Indicates if the carrier is eligible.")
    mc_number: str = Field(..., description="The carrier's Motor Carrier number.")
    detail: str = Field(..., description="Details about the carrier's status.")
    carrier_name: str | None = Field(None, description="The legal name of the carrier.")


class Load(BaseModel):
    load_id: str = Field(..., description="Unique identifier for the load.")
    origin: str = Field(..., description="Starting location of the load.")
    destination: str = Field(..., description="Final destination of the load.")
    equipment_type: str = Field(
        ..., description="Required equipment type (e.g., Reefer, Dry Van)."
    )
    loadboard_rate: float = Field(
        ..., description="Rate offered for the load on the loadboard."
    )
    weight: int = Field(..., description="Total weight of the load in kilograms.")
    miles: int = Field(..., description="Estimated mileage for the load.")
    pickup_datetime: datetime = Field(
        ..., description="Scheduled pickup date and time for the load."
    )
    delivery_datetime: datetime = Field(
        ..., description="Scheduled delivery date and time for the load."
    )
    notes: str = Field(
        default="", description="Additional notes or special instructions for the load."
    )
    commodity_type: str = Field(
        ...,
        description="Type of commodity being transported (e.g., Cítricos, Electronics).",
    )
    num_of_pieces: int = Field(
        ..., description="Number of pieces or pallets in the load."
    )
    dimensions: str = Field(
        ..., description="Dimensions of the load (e.g., 120x80x160 cm)."
    )
