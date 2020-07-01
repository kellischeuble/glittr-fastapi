from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

# Models to be moved to another file:
class Artist(BaseModel):
    artist_id: int 
    first_name: str = None
    last_name: str = None
    email: str = None
    password_hash: str = None
    zip_code: int = None
    is_active: bool = None


@app.get("/")
async def root():
    """
    Verifies the API is deployed and links to the docs
    """
    return HTMLResponse(
        """
        <H1> Glittr API </h1>
        <p> go to <a href="/docs">docs</a> for documentation.</p>
        """
    )

@app.post("/get-artist/")
async def get_artist(artist: Artist):
    return artist

@app.post("/update-artist/")
async def update_artist(artist: Artist):
    return artist

@app.post("/delete-artist/")
async def delete_artist(artist: Artist):
    return artist

@app.post("/create-artist/")
async def create_artist(artist: Artist):
    return artist

# @app.get("/create-payment-intent/")
# @app.get("/charge-saved-card/")
# @app.get("/stripe-webhook")
