from fastapi import FastAPI
import routes
from middleware import auth_check
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()
# TO RUN THE APP SPECIFY THIS INSTANCE OF THE FastApi class
# uvicorn file_name:instance name --reload

app.include_router(routes.router)
app.add_middleware(BaseHTTPMiddleware, dispatch=auth_check)
