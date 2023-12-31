# A* path finding

<div align="center">

![Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/SverreNystad/a-star-pathfinding/build_and_test.yml)
[![codecov.io](https://codecov.io/github/SverreNystad/a-star-pathfinding/coverage.svg?branch=main)](https://codecov.io/github/SverreNystad/a-star-pathfinding?branch=main)
![GPT-dungeon-master top language](https://img.shields.io/github/languages/top/SverreNystad/a-star-pathfinding)
![GitHub language count](https://img.shields.io/github/languages/count/SverreNystad/a-star-pathfinding)
[![Project Version](https://img.shields.io/badge/version-1.0.0-blue)](https://img.shields.io/badge/version-1.0.0-blue)

</div>

<details>
  <summary> <b> Table of Contents </b> </summary>
  <ol>
    <li>
    <a href="#A* path finding"> A* path finding</a>
    </li>
    <li>
      <a href="#Introduction">Introduction</a>
    </li>
    </li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Installation">Installation</a>
      <ul>
        <li><a href="#Prerequisites">Prerequisites</a></li>
        <li><a href="#Setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#Tests">Tests</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgment">Acknowledgment</a></li>
  </ol>
</details>

## Introduction
This project is a pathfinding algorithm that uses the A* algorithm to find the shortest path between two points. The algorithm is implemented in Python and uses the Pillow library to visualize the results. The algorithm is tested using pytest and the coverage is measured using the codecov.io service. The project is set up to use GitHub actions to run the tests and measure the coverage. The results of the tests and coverage are presented in the badges above.


## Usage
When the proper setup is done, the program can be run by executing the following command in the root directory of the project:
```bash
python main.py
```
### Results
To see the results of the different tasks look into the docs folder. Here the results are presented in a png files.
<details>

#### Task 1
![Task 1](docs/map_of_task_1.png)
![Task 1 exploration](docs/exploration_of_task_1.gif)
#### Task 2
![Task 2](docs/map_of_task_2.png)
![Task 2 exploration](docs/exploration_of_task_2.gif)
#### Task 3
![Task 3](docs/map_of_task_3.png)
![Task 3 exploration](docs/exploration_of_task_3.gif)
#### Task 4
![Task 4](docs/map_of_task_4.png)
![Task 4 exploration](docs/exploration_of_task_4.gif)
#### Task 5
![Task 5](docs/map_of_task_5.png)
![Task 5 exploration](docs/exploration_of_task_5.gif)
</details>

## Installation
To install the A star pathfinding, one needs to have all the prerequisites installed and set up, and follow the setup guild. The following sections will guide you through the process.

### Prerequisites
- Ensure that git is installed on your machine. [Download Git](https://git-scm.com/downloads)
- Ensure Python 3.9 or newer is installed on your machine. [Download Python](https://www.python.org/downloads/)

### Setup
1. Clone the repository
```bash
git https://github.com/SverreNystad/a-star-pathfinding.git
cd a-star-pathfinding
```
2. Create a virtual environment (optional, but recommended)
    #### On Windows:
    ```bash
    python3 -m venv venv
    source venv/Scripts/activate
    ```
    #### On macOS and Linux: 
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages
```bash
pip install -r requirements.txt
```


## Tests
To run all the tests, run the following command in the root directory of the project:
```bash
pytest --cov
coverage html # To generate a coverage report
```

## License
Licensed under the [MIT License](LICENSE). Because sharing is caring :)


## Acknowledgment
The dataset of Samfundet (https://www.samfundet.no/) is not made by me, and most of the code in the class Map_Obj was created by Håkon Måløy then later extended and documented by Xavier Sánchez-Díaz.

Thanks to the following libraries:
- [Pillow](https://pillow.readthedocs.io/en/stable/) for image manipulation
- [Pytest](https://docs.pytest.org/en/stable/) for testing
- [NumPy](https://numpy.org/) for numerical computing
- [Panadas](https://pandas.pydata.org/) for data analysis

