"""
@author      : rscalia
@build-date  : 29/12/2023 
@last-update : 29/12/2023 

Service 2 REST end-points
"""
from fastapi                                        import APIRouter, HTTPException, status
from pydantic                                       import BaseModel
from random                                         import randint

# DTOs
class AddInfo(BaseModel):
    id:str                  = None
    
class Descr(BaseModel):
    analysis_response:str   = None

# Router def
router:APIRouter                                    = APIRouter()


@router.post(
    "/service_2"                                                                            , 
    summary                                             =           "Service 2 start"       ,
                                                                                            )
async def service_2(pRequest:AddInfo) -> Descr:
    """
    # **service_2**
    """
    # Parse req
    parsed_req:dict             = pRequest.dict()
    
    # Return data to the caller
    return { 'analysis_response': str( randint(1,5000) )+"____"+parsed_req['id'] } 