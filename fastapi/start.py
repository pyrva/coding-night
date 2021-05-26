from math import pi


def area(radius: float) -> float:
    return pi * radius ** 2


def circumference(radius: float) -> float:
    return 2 * pi * radius


async def home():
    """Return webpage with area and circumference presented.

    Should have a form with an input for a measurement and
    a measurement type (radius or diameter) via radio box
    or dropdown.

    Browser URL should look like "/". After the form is submitted
    the URL should look like "/?param=radius&measurement=1"
    """
    return


async def area__path():
    """Get area from circle with given radius.

    Browser URL should look like "/area/1"
    Data submitted in url directly
    Accept radius only
    """
    return


async def area__query():
    """Get area from circle with given radius.

    Browser URL should look like "/area/?radius=1"
    Data submitted in query string
    Should accept radius or diameter
    """
    return


async def area__post():
    """Get area from circle with given radius.

    Browser URL should look like "/area/"
    Data submitted by post
    Should accept radius or diameter
    """
    return


async def circumference__path():
    """Get circumference from circle with given radius.

    Browser URL should look like "/circumference/1"
    Data submitted in url directly
    Accept radius only
    """
    return


async def circumference__query():
    """Get circumference from circle with given radius.

    Browser URL should look like "/circumference/?radius=1"
    Data submitted in query string
    Should accept radius or diameter
    """
    return


async def circumference__post():
    """Get circumference from circle with given radius.

    Browser URL should look like "/circumference/"
    Data submitted by post
    Should accept radius or diameter
    """
    return
