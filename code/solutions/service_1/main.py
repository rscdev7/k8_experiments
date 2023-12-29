"""
@author      : rscalia
@build-date  : 29/12/2023 
@last-update : 29/12/2023 

Service 1 driver
"""

from fastapi                                import FastAPI
from lib.rest_api.end_points                import router 

app:FastAPI         = FastAPI()
app.include_router(router)