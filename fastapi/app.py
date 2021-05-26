from math import pi
from fastapi import FastAPI, Request
from typing import Optional
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Circle(BaseModel):
    radius: float = None
    diameter: float = None


def area(radius: float) -> float:
    if radius is None:
        return
    return pi * radius ** 2


def circumference(radius: float) -> float:
    if radius is None:
        return
    return 2 * pi * radius


@app.get("/", response_class=HTMLResponse)
async def home(
    request: Request, param: Optional[str] = None, measurement: Optional[float] = None
):
    """Return webpage with area and circumference presented.

    Should have a form with an input for a measurement and
    a measurement type (radius or diameter) via radio box
    or dropdown.
    
    Browser URL should look like "/". After the form is submitted
    the URL should look like "/?param=radius&measurement=1"
    """
    radius = measurement
    if param == "diameter":
        radius /= 2.0

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "param": param,
            "measurement": measurement,
            "radius": radius,
            "area": area(radius),
            "circumference": circumference(radius),
        },
    )


@app.get("/area/{radius}")
async def area__path(radius: float):
    """Get area from circle with given radius.

    Browser URL should look like "/area/1"
    Data submitted in url directly
    Accept radius only
    """
    return {"radius": radius, "area": area(radius)}


@app.get("/area/")
async def area__query(radius: float = None, diameter: float = None):
    """Get area from circle with given radius.

    Browser URL should look like "/area/?radius=1"
    Data submitted in query string
    Should accept radius or diameter
    """
    if diameter and radius is None:
        radius = diameter / 2
    return {"radius": radius, "area": area(radius)}


@app.post("/area/")
async def area__post(circle: Circle):
    """Get area from circle with given radius.

    Browser URL should look like "/area/"
    Data submitted by post
    Should accept radius or diameter
    """
    radius = circle.radius
    if radius is None and circle.diameter:
        radius = circle.diameter / 2
    return {"radius": radius, "area": area(radius)}


@app.get("/circumference/{radius}")
async def circumference__path(radius: float):
    """Get circumference from circle with given radius.

    Browser URL should look like "/circumference/1"
    Data submitted in url directly
    Accept radius only
    """
    return {"radius": radius, "circumference": circumference(radius)}


@app.get("/circumference/")
async def circumference__query(radius: float = None, diameter: float = None):
    """Get circumference from circle with given radius.

    Browser URL should look like "/circumference/?radius=1"
    Data submitted in query string
    Should accept radius or diameter
    """
    if diameter and radius is None:
        radius = diameter / 2
    return {"radius": radius, "circumference": circumference(radius)}


@app.post("/circumference/")
async def circumference__post(circle: Circle):
    """Get circumference from circle with given radius.

    Browser URL should look like "/circumference/"
    Data submitted by post
    Should accept radius or diameter
    """
    radius = circle.radius
    if radius is None and circle.diameter:
        radius = circle.diameter / 2
    return {"radius": radius, "circumference": circumference(radius)}
