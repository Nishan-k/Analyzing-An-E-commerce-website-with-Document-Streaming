from fastapi import FastAPI, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import json

from pydantic import BaseModel
from datetime import datetime



# TODO:1 Create a schema for the incoming data:
class InvoiceItem(BaseModel):
    InvoiceNo:int
    StockCode: str
    Description: str
    Quantity: int
    InvoiceDate: str
    UnitPrice: float
    CustomerID: int
    Country:str

# TODO:2 Create an object for FastAPI:
app = FastAPI()

# Base URL:
@app.get("/")
async def root():
    return {
        "message":"The API is running."
    }


# Add new invoice:
@app.post("/invoiceitem")
async def post_invoice_item(item:InvoiceItem):
    print("New invoice recieved !!")
    try:
        # Change the date format from d/m/y to d:m:y
        
        date = datetime.strptime(item.InvoiceDate, "%d/%m/%Y %H:%M")
        print(date)

        item.InvoiceDate = date.strftime("%d-%m-%Y %H:%M")


        # Change the format of the data from string to json:
        json_invoice = jsonable_encoder(item)

        # Change the json into string for kafka:
        json_invoice_string = json.dumps(json_invoice)
        print(item)
        return JSONResponse(content=json_invoice, status_code=201)
    except ValueError:
        return JSONResponse(content=jsonable_encoder(item), status_code=400)