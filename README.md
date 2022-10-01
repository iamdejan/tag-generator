# Tag Generator

![Github Actions](https://github.com/iamdejan/tag-generator/actions/workflows/main.yaml/badge.svg)
[![License: GPL v2](https://img.shields.io/badge/License-GPL_v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

I wrote this program originally to create a SemVer tag in an easy way.

## Prerequisites

1) Python 3.10
2) pip3
    - Install the necessary packages by running `pip3 install -r requirements.txt`

## How to Use

Run `python3 main.py -h` for help.

## Screenshots

### Help Menu

![Help](./screenshots/help.png)

### Create Tag

![Create Invalid Tag](./screenshots/create-invalid-tag.png)
![Create Valid Tag](./screenshots/create-valid-tag.png)

### Bump Tag

![Bump prerelease tag](./screenshots/bump-prerelase-tag.png)
![Bump minor and major tag](./screenshots/bump-minor-and-major-tag.png)
