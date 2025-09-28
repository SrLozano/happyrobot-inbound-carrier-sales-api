from fastapi import APIRouter, Depends

from ..models import CarrierVerificationResponse
from ..security import get_api_key

router = APIRouter()


@router.get("/verify_carrier", response_model=CarrierVerificationResponse)
def verify_carrier(mc_number: str, api_key: str = Depends(get_api_key)):
    """MOCKED: FMCSA API DOWN
    Verifies a carrier's MC number to check if they are eligible."""
    eligible_carriers = {
        "123456": {"name": "Rapid Trans Inc."},
        "654321": {"name": "Safe Trucks Inc."},
    }

    if mc_number in eligible_carriers:
        return {
            "is_eligible": True,
            "mc_number": mc_number,
            "carrier_name": eligible_carriers[mc_number]["name"],
            "detail": "Mock verification successful: Carrier is eligible.",
        }
    else:
        return {
            "is_eligible": False,
            "mc_number": mc_number,
            "carrier_name": None,
            "detail": "Mock verification failed: Carrier is not found or ineligible.",
        }
