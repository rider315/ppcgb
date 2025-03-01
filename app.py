# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.responses import FileResponse
# from fastapi.middleware.cors import CORSMiddleware
# import pandas as pd
# from calculation import calculate_new_bid, EQUIPMENT_SETTINGS
# from utils.dictionary_manager import DictionaryManager5Lang
# from format_config import apply_template_format
# import os
# from typing import Optional
# from pydantic import BaseModel
# from auth import register_user, login_user  # Import simplified auth functions

# app = FastAPI()
# dict_manager = DictionaryManager5Lang()

# # Temporary file storage
# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # Enable CORS for frontend communication
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Pydantic model for the /optimize endpoint
# class OptimizeRequest(BaseModel):
#     target_roas: float
#     strategy: str
#     filename: str
#     equipment: Optional[dict] = None

# # Pydantic model for authentication requests
# class AuthRequest(BaseModel):
#     email: str
#     password: str

# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     if not file.filename.endswith(".xlsx"):
#         raise HTTPException(status_code=400, detail="Only XLSX files are supported")
    
#     file_path = os.path.join(UPLOAD_DIR, file.filename)
#     with open(file_path, "wb") as f:
#         f.write(await file.read())
    
#     try:
#         df = pd.read_excel(file_path)
#     except Exception as e:
#         os.remove(file_path)
#         raise HTTPException(status_code=400, detail=f"Invalid file: {str(e)}")
    
#     return {"filename": file.filename, "message": "File uploaded successfully"}

# @app.post("/optimize")
# async def optimize_bids(request: OptimizeRequest):
#     filename = request.filename
#     target_roas = request.target_roas
#     strategy = request.strategy
#     equipment = request.equipment

#     if not filename:
#         raise HTTPException(status_code=400, detail="No file specified")
    
#     file_path = os.path.join(UPLOAD_DIR, filename)
#     if not os.path.exists(file_path):
#         raise HTTPException(status_code=404, detail="File not found")
    
#     try:
#         df = pd.read_excel(file_path)
#         df["Altes Gebot"] = df.get("Gebot", 0.0)
#         df["ROAS"] = df.get("ROAS", None)

#         df["Neues Gebot"] = df.apply(
#             lambda row: calculate_new_bid(
#                 current_bid=row["Altes Gebot"],
#                 target_roas=target_roas,
#                 current_roas=row["ROAS"],
#                 strategy=strategy,
#                 row_data=row.to_dict(),
#                 equipment=equipment if strategy == "Individuell" else None
#             ),
#             axis=1
#         )

#         df["Veränderung in %"] = ((df["Neues Gebot"] - df["Altes Gebot"]) / df["Altes Gebot"] * 100).round(2).fillna(0)
#         df["Veränderung in €"] = (df["Neues Gebot"] - df["Altes Gebot"]).round(2)

#         formatted_df = apply_template_format(df)
#         output_path = os.path.join(UPLOAD_DIR, f"optimized_{filename}")
#         formatted_df.to_excel(output_path, index=False)

#         return {"optimized_filename": f"optimized_{filename}", "message": "Bids optimized successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

# @app.get("/download/{filename}")
# async def download_file(filename: str):
#     file_path = os.path.join(UPLOAD_DIR, filename)
#     if not os.path.exists(file_path):
#         raise HTTPException(status_code=404, detail="File not found")
#     return FileResponse(file_path, filename=filename, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# # Authentication endpoints
# @app.post("/register")
# async def register(request: AuthRequest):
#     return await register_user(request.email, request.password)

# @app.post("/login")
# async def login(request: AuthRequest):
#     return await login_user(request.email, request.password)
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from calculation import calculate_new_bid, EQUIPMENT_SETTINGS
from utils.dictionary_manager import DictionaryManager5Lang
from format_config import apply_template_format
from sku_matcher import SKUMatcher
import os
from typing import Optional, List
from pydantic import BaseModel
from auth import register_user, login_user  # Import from auth.py
from mangum import Mangum  # Import Mangum for Vercel

app = FastAPI()

# Enable CORS for frontend communication (update allow_origins for Vercel deployment)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-vercel-url.vercel.app"],  # Update to your frontend Vercel URL or use ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# MongoDB connection (using .env or default MongoDB Atlas)
mongo_client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = mongo_client["ppc_goat_db"]
users_collection = db["users"]

# Temporary file storage (use /tmp for Vercel serverless environment)
UPLOAD_DIR = "/tmp/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

dict_manager = DictionaryManager5Lang()
known_skus = ["SKUXYZAA", "SKUXYZAB"]  # Example SKUs; load from a file or database in production
sku_matcher = SKUMatcher(known_skus)

# Pydantic models
class OptimizeRequest(BaseModel):
    target_roas: float
    strategy: str
    filename: str
    equipment: Optional[dict] = None
    sku_rules: Optional[List[dict]] = None

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="Only XLSX files are supported")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        os.remove(file_path)
        raise HTTPException(status_code=400, detail=f"Invalid file: {str(e)}")
    
    return {"filename": file.filename, "message": "File uploaded successfully"}

@app.post("/optimize")
async def optimize_bids(request: OptimizeRequest):
    filename = request.filename
    target_roas = request.target_roas
    strategy = request.strategy
    equipment = request.equipment
    sku_rules = request.sku_rules

    if not filename:
        raise HTTPException(status_code=400, detail="No file specified")
    
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        df = pd.read_excel(file_path)
        df["Altes Gebot"] = df.get("Gebot", 0.0)
        df["ROAS"] = df.get("ROAS", None)
        df["SKU"] = df.get("SKU", None)  # Ensure SKU column exists

        # Apply SKU-specific rules if provided
        if sku_rules:
            for rule in sku_rules:
                skus = sku_matcher.get_skus_for_keyword(rule["sku"]) or [rule["sku"]]
                for sku in skus:
                    mask = df["SKU"] == sku
                    df.loc[mask, "Neues Gebot"] = df.loc[mask].apply(
                        lambda row: calculate_new_bid(
                            current_bid=row["Altes Gebot"],
                            target_roas=rule["target_roas"],
                            current_roas=row["ROAS"],
                            strategy=rule["strategy"],
                            row_data=row.to_dict(),
                            equipment=equipment if rule["strategy"] == "Individuell" else None
                        ),
                        axis=1
                    )

        # Apply global strategy if no SKU rules or for rows without SKU rules
        mask_no_sku = df["SKU"].isna() | ~df["SKU"].isin([rule["sku"] for rule in sku_rules or []])
        df.loc[mask_no_sku, "Neues Gebot"] = df.loc[mask_no_sku].apply(
            lambda row: calculate_new_bid(
                current_bid=row["Altes Gebot"],
                target_roas=target_roas,
                current_roas=row["ROAS"],
                strategy=strategy,
                row_data=row.to_dict(),
                equipment=equipment if strategy == "Individuell" else None
            ),
            axis=1
        )

        df["Veränderung in %"] = ((df["Neues Gebot"] - df["Altes Gebot"]) / df["Altes Gebot"] * 100).round(2).fillna(0)
        df["Veränderung in €"] = (df["Neues Gebot"] - df["Altes Gebot"]).round(2)

        formatted_df = apply_template_format(df)
        output_path = os.path.join(UPLOAD_DIR, f"optimized_{filename}")
        formatted_df.to_excel(output_path, index=False)

        return {"optimized_filename": f"optimized_{filename}", "message": "Bids optimized successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, filename=filename, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@app.post("/register")
async def register(request: RegisterRequest):
    try:
        result = await register_user(request.name, request.email, request.password)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Registration error: {str(e)}")

@app.post("/login")
async def login(request: LoginRequest):
    try:
        result = await login_user(request.email, request.password)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login error: {str(e)}")

@app.get("/insights/{filename}")
async def get_insights(filename: str):
    file_path = os.path.join(UPLOAD_DIR, f"optimized_{filename}")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Optimized file not found")
    
    try:
        df = pd.read_excel(file_path)
        
        # Calculate summary statistics
        total_impressions = df["Impressions"].sum()
        total_clicks = df["Klicks"].sum()
        ad_spend = df["Ausgaben"].sum()
        sales = df["Verkäufe"].sum()
        ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
        conversion_rate = (df["Bestellungen"].sum() / total_clicks * 100) if total_clicks > 0 else 0
        acos = (ad_spend / sales * 100) if sales > 0 else 0
        roas = (sales / ad_spend) if ad_spend > 0 else 0
        bids_raised = len(df[df["Veränderung in %"] > 0])
        bid_reductions = len(df[df["Veränderung in %"] < 0])
        updated_rows = len(df[df["Veränderung in %"] != 0])
        new_roas_target = 5.5  # This could be dynamic based on the request

        # Get example rows for insights
        examples = df.sample(n=3, random_state=42)[[
            "Keyword-Text", "ROAS", "Conversion-Rate", "Impressions", "Ausgaben", "Altes Gebot", "Neues Gebot"
        ]].to_dict(orient='records')
        for example in examples:
            example["keyword"] = example.pop("Keyword-Text")
            example["conversion_rate"] = example.pop("Conversion-Rate")
            example["ad_spend"] = example.pop("Ausgaben")
            example["old_bid"] = example.pop("Altes Gebot")
            example["new_bid"] = example.pop("Neues Gebot")
            example["bid_change"] = ((example["new_bid"] - example["old_bid"]) / example["old_bid"] * 100).round(2) if example["old_bid"] > 0 else 0

        return {
            "new_roas_target": new_roas_target,
            "bids_raised": bids_raised,
            "bid_reductions": bid_reductions,
            "updated_rows": updated_rows,
            "ad_spend": round(ad_spend, 2),
            "sales": round(sales, 2),
            "acos": round(acos, 2),
            "roas": round(roas, 2),
            "impressions": total_impressions,
            "clicks": total_clicks,
            "ctr": round(ctr, 2),
            "conversion_rate": round(conversion_rate, 2),
            "examples": examples
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating insights: {str(e)}")

# Export handler for Vercel serverless environment
handler = Mangum(app)