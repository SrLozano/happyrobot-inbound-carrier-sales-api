from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query

from ..data import LOADS
from ..models import Load
from ..security import get_api_key

router = APIRouter()


@router.get("/search_loads", response_model=list[Load])
def search_loads(
    equipment_type: str = Query(..., description="Type of equipment required"),
    origin: str | None = Query(None, description="Pickup city/state"),
    destination: str | None = Query(None, description="Delivery city/state"),
    pickup_date: str | None = Query(None, description="Pickup date in YYYY-MM-DD"),
    delivery_date: str | None = Query(None, description="Delivery date in YYYY-MM-DD"),
    api_key: str = Depends(get_api_key),
):
    """Search loads that match equipment type, optional origin/destination, and dates."""
    results = []

    for load in LOADS:
        # Equipment filter (mandatory)
        if load["equipment_type"].lower() != equipment_type.lower():
            continue

        # Origin / Destination filters (optional)
        if origin and origin.lower() not in load["origin"].lower():
            continue
        if destination and destination.lower() not in load["destination"].lower():
            continue

        # Date filters (optional)
        if pickup_date:
            load_pickup = datetime.fromisoformat(load["pickup_datetime"]).date()
            if str(load_pickup) != pickup_date:
                continue
        if delivery_date:
            load_delivery = datetime.fromisoformat(load["delivery_datetime"]).date()
            if str(load_delivery) != delivery_date:
                continue

        results.append(load)

    if not results:
        raise HTTPException(status_code=404, detail="No loads found matching criteria")

    return results


@router.get("/get_load_details", response_model=Load)
def get_load_details(
    load_id: str = Query(..., description="Unique identifier for the load"),
    api_key: str = Depends(get_api_key),
):
    """Retrieve details for a specific load by its ID."""
    print(LOADS)
    # Iterate through the loads to find the one with the matching load_id
    for load in LOADS:
        if load.get("load_id") == load_id:
            return load

    # If no load is found, raise an HTTPException
    raise HTTPException(status_code=404, detail=f"Load with ID '{load_id}' not found.")
