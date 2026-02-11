from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/inventory", tags=["Inventory"])

# Load medicine data
df = pd.read_csv("data/medicines.csv")

@router.get("/")
def get_inventory():
    return df.to_dict(orient="records")
