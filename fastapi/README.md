# FastAPI Challenge

https://fastapi.tiangolo.com/

This challenge is intended to give you an introduction to the features of FastAPI.
The goal is to learn how to use FastAPI to accept data, perform a calculation, and return an appropriate response.

## Tasks

1. Create an endpoint `/area/` that returns a `json` object containing the `radius` and `area` of the circle. Create three versions of the endpoint. Each endpoint should return `{"radius": 1, "area": 3.14159}`.
  - Specify data in url path `/area/1`
  - Specify data in query string. Either `/area/?radius=1` or `/area/?diameter=2` should work.
  - Specify data using post data `/area/`. Data could be either `{"radius": 1}` or `{"diameter": 2}`
2. Create an endpoint `/circumference/` that returns a `json` object containing the `radius` and `circumference` of the circle. Create three versions of the endpoint. Each endpoint should return `{"radius": 1, "circumference": 6.28318}`.
  - Specify data in url path `/circumference/1`
  - Specify data in query string. Either `/circumference/?radius=1` or `/circumference/?diameter=2` should work.
  - Specify data using post data `/circumference/`. Data could be either `{"radius": 1}` or `{"diameter": 2}`
3. Create a webpage at `/` that presents the user with a web form. The form should allow the user to input a `measurement` and specify if the `parameter` is `radius` or `diameter`.
  - Use [Jinja2](https://jinja.palletsprojects.com/) templates to create the html.
  - The form should display what the user entered before hitting `submit`
  - Below the form, display the area and circumference of the circle (only if it has been calculated, so not on the initial page load)

For reference, the formulas for area and circumference area as follows:

$$A = \pi r^2 = \frac{\pi}{4} d^2$$
$$C = 2 \pi r = \pi d$$
$$d = 2 r$$

## Skill Levels

Depeding on your skill level, you should start with the following configuration.

**Absolute Beginner:**
Take a look at `app.py`, `templates/index.html`, and `test_app.py` and browse through the FastAPI documentation to see if you can understand what is going on.

**Novice:**
Copy `requirements.txt`, `start.py`, `templates/index.html`, and `test_app.py` to your directory. Install the required packages. Work through the problems as best as you can and use pytest to make sure you're on the right track. Use `templates/index.html` to help figure out what you need for challenge item 3.

**Junior:**
Copy `requirements.txt`, `start.py`, and `test_app.py` to your directory.Install the required packages. Work through the problems as best as you can and use pytest to make sure you're on the right track. Fill out `start.py` and write `templates/index.html` to complete the challenge.

**Senior:**
Copy `start.py` to your directory. Figure out what packages you need to install and work through the problems as best as you can. Fill out `start.py` and write `templates/index.html` to complete the challenge. Write tests in `test_app.py` as you go.

**Professional:**
You have a blank slate. Make it all happen.
