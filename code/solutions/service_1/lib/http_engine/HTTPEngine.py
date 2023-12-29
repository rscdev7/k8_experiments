"""
@author           	:  rscalia
@build-date         :  Thu 15/07/2021
@last_update        :  Mon 20/11/2023

This class manages HTTPS sync and async requests
"""
from aiohttp                                import ( 
                                                        ClientSession           , 
                                                        ClientTimeout           , 
                                                        ClientError             , 
                                                        ClientPayloadError      , 
                                                        InvalidURL              , 
                                                        ClientResponseError     , 
                                                        ClientResponseError     , 
                                                        TCPConnector
                                                    )
import json
import requests
from requests.models                        import Response
from typing                                 import Dict, Union, Tuple
from .HTTPError                             import HTTPError


class HTTPEngine(object):

    def __init__(self, pSecTimeOut:int , pVerifySSLCert:bool=True) -> object:
        """
        # **HTTPEngine**

        Args:
            pSecTimeOut         (int)               : timeout per le richieste HTTP in secondi
            pVerifySSLCert      (bool, optional)    : TRUE for verifying identity of SSL certificates for HTTPS requests. Defaults to True.
        """
        self._timeOut:int                           = pSecTimeOut
        self._asyncSession:ClientSession            = None
        self._verifySSL:bool                        = pVerifySSLCert


    def startAsync(self) -> None:
        """
        # **startAsync**

        Start async HTTPS session
        """
        timeout:ClientTimeout                       = ClientTimeout(total=self._timeOut)
        self._asyncSession:ClientSession            = ClientSession( timeout=timeout , connector=TCPConnector(ssl=self._verifySSL) )

    async def closeAsync(self) -> Union[ None , Exception]:
        """
        # **closeAsync**
        
        Close async HTTP session
        """
        try:
            await self._asyncSession.close()
        except Exception as exp:
            return exp


    def get(self, pURL:str , pParams:dict={}) -> Union[ Dict[int,dict] , Exception, Tuple[Exception,int,dict] ]:
        """
        # **get**

        This method performs an HTTP sync GET request

        Args:\n
                pURL            (str)                                               : get request URL
                pParams         (dict, optional)                                    : additional parameters to HTTP get request. Defaults to {}.
        
        Returns:        
            Union[ Dict[int,dict] , Exception, Tuple[Exception,int,dict] ]          : Dict fmt in right case:\n
                                                                                        - "status_code", HTTP request status code     \n
                                                                                        - "payload", HTTP request payload             \n

                                                                                      Tuple Fmt:\n
                                                                                        - 0 -> Exception that describe in short error \n
                                                                                        - 1 -> HTTP Status Code                       \n
                                                                                        - 2 -> Payload as dictionary
                                
                                

        Raises:
            - "HTTPError"     : HTTP error from 400 to 499 \n
            - "RuntimeError"  : Runtime error \n
            - "Exception"     : Generic error
        """
        try:
            r:Response      = requests.get( pURL, params=pParams, verify=self._verifySSL, timeout=self._timeOut)
            status_code:int = r.status_code
            response:dict   = r.json()
            if status_code >= 400 and status_code <= 599: raise HTTPError("HTTP Error {}".format(status_code))
            return { "status_code": status_code , "payload": response }
        
        except HTTPError as err:
            return err, status_code, response
        except RuntimeError as rte:
            return rte
        except Exception as ex:
            return ex


    async def getAsync(self, pURL:str, pParams:dict={}) -> Union[ Dict[int,dict] , Exception, Tuple[Exception,int,dict] ]:
        """
        # **getAsync**

        This method performs an HTTP async GET request

        Args:\n
                pURL            (str)                                               : get request URL
                pParams         (dict, optional)                                    : additional parameters to HTTP get request. Defaults to {}.
        
        Returns:        
            Union[ Dict[int,dict] , Exception, Tuple[Exception,int,dict] ]          : Dict fmt in right case:\n
                                                                                        - "status_code", HTTP request status code   \n
                                                                                        - "payload", HTTP request payload           \n

                                                                                      Tuple Fmt:\n
                                                                                        - 0 -> Exception that describe in short error \n
                                                                                        - 1 -> HTTP Status Code                       \n
                                                                                        - 2 -> Payload as dictionary

        Raises:\n
            - "HTTPError"             : HTTP error from 400 to 499 \n
            - "InvalidURL"            : bad formed URL \n
            - "ClientPayloadError"    : bad payload format \n
            - "ClientResponseError"   : error on client answer process \n
            - "ClientError"           : HTTP API error \n
            - "RuntimeError"          : Runtime error \n
            - "Exception"             : Generic error
        """
        try:
            async with self._asyncSession.get( url=pURL , params=pParams) as resp:
                status_code:int     = resp.status
                response:dict       = await resp.json()
                if status_code >= 400 and status_code <= 599: raise HTTPError("HTTP Error {}".format(status_code))
                return { "status_code": status_code , "payload": response }
                
        except HTTPError as err:
            return err, status_code, response
        except InvalidURL as iurl:
            return iurl
        except ClientPayloadError as cpe:
            return cpe
        except ClientResponseError as cl:
            return cl
        except ClientError as cle:
            return cle
        except RuntimeError as rte:
            return rte
        except Exception as ex:
            return ex


    def post(self, pUrl:str , pPayload:dict) -> Union[ Dict[int,dict] , Exception, Tuple[Exception,int,dict] ]:
        """
        # **post**

        This method performs an HTTP sync POST request

        Args:\n
                pURL            (str)                                               : post request URL
                pParams         (dict)                                              : payload
        
        Returns:        
            Union[ Dict[int,dict] , Exception, Tuple[Exception,int,dict] ]          : Dict fmt in right case:                           \n
                                                                                        - "status_code", HTTP request status code       \n
                                                                                        - "payload", HTTP request payload               \n

                                                                                      Tuple Fmt:\n
                                                                                        - 0 -> Exception that describe in short error \n
                                                                                        - 1 -> HTTP Status Code                       \n
                                                                                        - 2 -> Payload as dictionary
                                
                                
        Raises:
            - "HTTPError"     : HTTP error from 400 to 499 \n
            - "RuntimeError"  : Runtime error \n
            - "Exception"     : Generic error
        """
        try:
            r:Response      = requests.post( pUrl                                                                   , 
                                             data=json.dumps( pPayload , default=lambda o:o.__dict__ , indent=2 )   , 
                                             verify=self._verifySSL                                                 ,
                                             timeout=self._timeOut                                                  )
            status_code:int = r.status_code
            response:dict   = r.json()
            if status_code >= 400 and status_code <= 599: raise HTTPError("HTTP Error {}".format(status_code))
            return { "status_code": status_code , "payload": response }

        except HTTPError as err:
            return err, status_code, response
        except RuntimeError as rte:
            return rte
        except Exception as ex:
            return ex


    async def postAsync(self, pUrl:str , pPayload:dict) -> Union[ Dict[int,dict] , Exception, Tuple[Exception,int,dict] ]:
        """
        # **postAsync**

        This method performs an HTTP async POST request

        Args:\n
                pURL            (str)                                               : post request URL
                pParams         (dict)                                              : payload
        
        Returns:        
            Union[ Dict[int,dict] , Exception, Tuple[Exception,int,dict] ]          : Dict fmt in right case:                       \n
                                                                                        - "status_code", HTTP request status code   \n
                                                                                        - "payload", HTTP request payload           \n

                                                                                      Tuple Fmt:\n
                                                                                        - 0 -> Exception that describe in short error \n
                                                                                        - 1 -> HTTP Status Code                       \n
                                                                                        - 2 -> Payload as dictionary

        Raises:\n
            - "HTTPError"             : HTTP error from 400 to 499 \n
            - "InvalidURL"            : bad formed URL \n
            - "ClientPayloadError"    : bad payload format \n
            - "ClientResponseError"   : error on client answer process \n
            - "ClientError"           : HTTP API error \n
            - "RuntimeError"          : Runtime error \n
            - "Exception"             : Generic error
        """
        try:
            resp:_RequestContextManager     = await self._asyncSession.post(pUrl, json=pPayload)
            status_code:int                 = resp.status
            response:str                    = await resp.json()
            if status_code >= 400 and status_code <= 599: raise HTTPError("HTTP Error {}".format(status_code))
            return { "status_code": status_code , "payload": response }

        except HTTPError as err:
            return err,status_code, response
        except InvalidURL as iurl:
            return iurl
        except ClientPayloadError as cpe:
            return cpe
        except ClientResponseError as cl:
            return cl
        except ClientError as cle:
            return cle
        except RuntimeError as rte:
            return rte
        except Exception as ex:
            return ex