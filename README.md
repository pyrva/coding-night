# PyRVA Coding Night Exercises

Welcome to the PyRVA coding night repository. Coding night is a monthly gathering where we challenge our members to work through some exercises. Some nights we will play with existing challenge sites on the web, while other meetings will have custom generated content.

The custom generated content will rely on [Jupyter Notebooks](https://jupyter.org/) located in the source code above. The brilliant minds behind [Binder](https://mybinder.org) make it really easy for you to get started with our exercises. You can click this badge [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyrva/coding-night/master) and have access to an environment with all the dependencies you'll need already installed. For a specific meeting, click the link in the table below to go straight to the challenge. You will be able to download a copy of your notebook at the end of the session.

>***Please note that the environment will timeout after 10 minutes of activity.***

Check us out on [Meetup](https://www.meetup.com/PyRVAUserGroup/) to see when the next meeting is scheduled. **Due to current events, we are hosting virutal meetings on [Discord](https://discord.com/). Invite links will be posted on Meetup.**


# Code Night History

Date | Topic | Link
---|---|---
2021-05-27 | FastAPI | Go to the `fastapi` folder in this repo.
2020-11-19 | Numpy 100 | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rougier/numpy-100/master?filepath=100_Numpy_exercises.ipynb)
2020-10-22 | 100 Pandas Puzzles | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ajcr/100-pandas-puzzles/master?filepath=100-pandas-puzzles.ipynb)
2020-08-27 | Refactoring and Testing | [emilybache/gildedrose-refactoring-kata](github.com/emilybache/gildedrose-refactoring-kata)
2020-07-23 | pathlib | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyrva/coding-night/master?filepath=pathlib/Challenge.ipynb)
2020-06-25 | Web Scraping | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyrva/coding-night/master?filepath=web-scraping-intro/Challenge.ipynb)
2020-05-28 | Python Challenge | http://www.pythonchallenge.com
2020-04-23 | Python Morsels | https://www.pythonmorsels.com/
2020-03-26 | py.checkio.org | https://py.checkio.org/
2020-02-27 | Twilio Quest | https://www.twilio.com/quest
2020-01-23 | Project Euler | https://projecteuler.net/
2019-07-25 | Data analysis with Pandas |

# Notes for Contributors

[nbstripout](https://pypi.org/project/nbstripout/) should be used to keep git commits small and manageable. This automatically cleans the output and run counts from the notebook before committing to the repository. The commands below will help you get your environment setup and ready for development.

Create the environment

    python -m venv venv
    pip install -r requirements.txt

Activate your environment

    win> venv\Scripts\activate
    nix$ source venv/bin/activate

Ensure notebook output and run counts are stripped before committing

    nbstripout --install

Open Jupyter Lab

    jupyter lab
