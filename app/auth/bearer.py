from typing_extensions import Annotated, Doc
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from.handler import decodeJWT
from fastapi import Request, HTTPException

class Bearer(HTTPBearer):
    def __init__(self, auto_error:bool = True): 
        super(Bearer,self).__init__(auto_error=auto_error)

    async def __call__(self,request:Request):
        credentials: HTTPAuthorizationCredentials=await super(Bearer, self).__call__(request)
        if credentials:
            if not credentials.scheme =="Bearer":
                raise HTTPException(status_code=403, detail="invalid authentification scheme")
            if not self.varify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token")
            def verify_jwt(self,token:str):
                decoded_token = decodeJWT(token)
                if decoded_token:
                    return True
                return False