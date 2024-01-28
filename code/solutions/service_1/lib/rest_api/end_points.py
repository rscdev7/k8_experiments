"""
@author      : rscalia
@build-date  : 29/12/2023 
@last-update : 29/12/2023 

Service 1 REST end-points
"""
from fastapi                                        import APIRouter, HTTPException, status
from pydantic                                       import BaseModel
from ..http_engine.HTTPEngine                       import HTTPEngine
from typing                                         import Union

# DTOs
class AddInfo(BaseModel):
    id:str              = None
    
class Descr(BaseModel):
    analysis:str        = None    

# Router def
router:APIRouter                                    = APIRouter()

# CFG
K8_SERV:str             = "k8-sample-app-svc"
K8_PORT:str             = "85"
COMPOSE_VER:str         = "service_2"
COMPOSE_PORT:str        = "9006"
S2_END_POINT:str        = "http://{}:{}/service_2".format( K8_SERV , K8_PORT )

@router.get(
    "/service_1"                                                                            , 
    summary                                             =           "Service 1 start"       ,
                                                                                            )
async def service_1(id:str, name:str, surname:str) -> Descr:
    """
    # **service_1**
    """
    # Parse req
    parsed_req:dict             = { 'id':id, 'name':name, 'surname':surname }
    
    # Init HTTP engine
    engine:HTTPEngine           = HTTPEngine( 1.0, False )
    engine.startAsync()
    
    # Perform request to service 2 in order to get info
    result:dict[int,dict] | Exception | tuple[Exception,int,dict] = await engine.postAsync( S2_END_POINT, { 'id':parsed_req['id'] } )
    match result:
        case Exception():
            raise HTTPException( status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=str(result) )
        case tuple():
            raise HTTPException( status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=str(result[0]) )
                                
    # Return data to the caller
    return { 'analysis':result['payload']['analysis_response'] } 