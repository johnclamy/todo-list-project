import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.router import api_router


app = FastAPI()


# Enable CORS so the React frontend can communicate with the server
# In production, replace "*" with your specific frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix='/api/v1')


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
