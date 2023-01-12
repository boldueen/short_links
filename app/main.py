from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api import router


app = FastAPI(title='short link')

app.include_router(router.root_router, prefix='')

@app.get('/{short_link}')
def redirect_short_link(short_link:str):
    return RedirectResponse(f'/api/v1/link/{short_link}', status_code=status.HTTP_301_MOVED_PERMANENTLY)

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, port=1488, reload=True)

    
