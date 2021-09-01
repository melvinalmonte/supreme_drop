# Supreme Drop Script

A silly script that goes through [Supreme New York](https://www.instagram.com/supremenewyork/) instagram page and tries to extract the date of their latest supply drop. 

## Getting Started

Just clone this repo.

### Prerequisites

Python 3 with pip

### Installing

Once cloned go to the project root file and create a virtual environment

```
$ python3 -m venv .venv
```

Activate environment

for Linux and MacOS:
```
$ source .venv/bin/activate
```
for Windows:
```
$ .venv/Scripts/activate.bat
```

Install dependencies:

```
$ pip install -r requirements.txt
```

### Run App

Just run the script!

```
$ python index.py
```

## Example output:
Expected response:
```
___________________________________________________________
Collab: Supreme®/New York Yankees™.  
Drop Date: 09/02/2021
```

## Built With


* [Python](https://www.python.org/) - Programming language.
* [instaloader](https://instaloader.github.io/) - Instagram loader library.