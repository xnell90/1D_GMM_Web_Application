import torch

from gmm import GMMSimple, train_model, extract_gmm_parameters
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict


app = FastAPI()
# Set up the static files (JS, CSS, images, etc.) directory
app.mount("/static", StaticFiles(directory="static"), name="static")

class Points(BaseModel):
    coordinates: List[Dict[str, float]]

@app.get("/")
async def root():
    with open("./index.html") as f:
        html = f.read()

    return HTMLResponse(content=html, status_code=200)

model = None

@app.post("/train")
def train(n_components: int, epochs: int, points: Points, retrain: int):
    points = points.coordinates

    if len(points) <= 1:
        raise Exception("Not Enough Data Points!")

    #Since the y-coordinates is always 0, simply remove the y-coordinate.
    points = torch.tensor([
        point['x']
        for point in points
    ])

    global model
    if retrain or (model is None): model = GMMSimple(n_components=n_components)

    losses_mean = train_model(
        model=model, 
        optimizer=torch.optim.SGD(model.parameters(), lr=0.01), 
        x=points, 
        n_epochs=epochs
    )
    
    data_mean = points.mean().item()
    data_std = points.std().item()

    pi, mu, sigma = extract_gmm_parameters(model, data_mean, data_std)

    pi = [float(num) for num in list(pi.flatten())]
    mu = [float(num) for num in list(mu.flatten())]
    sigma = [float(num) for num in list(sigma.flatten())]

    return {
        "pi": pi,
        "mu": mu,
        "sigma": sigma
    }





    
