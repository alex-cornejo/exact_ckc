# Capacitated vertex k-center problem
Exact algorithm implementation for the capacitated vertex k-center problem. The virtual poster of this work can be checked in https://www.youtube.com/watch?v=qPmeCb4HTAE&ab_channel=smm_oficial (spanish).


## Setup
### Install gurobipy:

Source: https://www.gurobi.com/gurobi-and-anaconda-for-windows/

#### Step one: Download and install Anaconda

Gurobi supports Python 2.7 and 3.7 for Windows. Please choose the version of Anaconda you wish to download (the download will start automatically):

Once the download is complete, click on it to run the installer.

#### Step two: Install Gurobi into Anaconda

The next step is to install the Gurobi package into Anaconda. You do this by first adding the Gurobi channel into your Anaconda platform and then installing the gurobi package from this channel.

From an Anaconda terminal issue the following command to add the Gurobi channel to your default search list:

```
$ conda config --add channels http://conda.anaconda.org/gurobi
```

Now issue the following command to install the Gurobi package:

```
$ conda install gurobi
```

You can remove the Gurobi package at any time by issuing the command:

```
$ conda remove gurobi
```

#### Step three: Install a Gurobi License

The third step is to install a Gurobi license (if you haven’t already done so).

You are now ready to use Gurobi from within Anaconda. Your next step is to launch either the Spyder IDE or Jupyter Notebook.


## Running the exact algorithm

To execute the exact algorithms (algorithm_1.py or F1C.py) run the following command on the Anaconda prompt.

```
$ python algorithm_1.py {instance} {n} {k} {Q}
```
or
```
$ python F1C.py {instance} {n} {k} {Q}
```

### Where,

|  Parameter |                                          Description                                          |
|----------|---------------------------------------------------------------------------------------------|
| `{instance}` | (string) Instance file path                                    |
| `{n}`    | (integer) Number of vertices  |
| `{k}`    | (integer) Number of centers  |
| `{Q}`    | (integer or string) for uniform capacity specify an integer. Otherwise, set 'NA'  |


## Example 1

```
$ python algorithm_1.py C:\Users\kroA100.tsp 100 5 NA
```

The output of this command includes the Gurobi Log. Once its over, the output shows the solution in JSON format, which consists of the set of centers, and the vertices assigned to each center. The solution size and the total runtime is also showed.

```
{"instance": "kroA100_Q1.tsp",
"centers": [
{ "center": 21, "nodes": [6, 10, 11, 15, 17, 18, 24, 32, 36, 38, 45, 47, 49, 59, 63, 72, 74, 90, 91, 98, 99]},
{ "center": 25, "nodes": [2, 28, 40, 44, 50, 54, 58, 61, 64, 67, 69, 73, 81, 93]},
{ "center": 35, "nodes": [7, 9, 12, 20, 23, 27, 34, 43, 46, 51, 55, 57, 60, 62, 77, 83, 86, 87]},
{ "center": 75, "nodes": [1, 4, 8, 16, 19, 22, 26, 31, 42, 53, 56, 65, 66, 70, 79, 80, 84, 88, 89, 92, 94, 97]},
{ "center": 78, "nodes": [3, 5, 13, 14, 29, 30, 33, 37, 39, 41, 48, 52, 68, 71, 76, 82, 85, 95, 96, 100]}
]}
UPPER = MID
solution size: 895.6439024523083
total runtime: 6.712827682495117
```

## Example 2

```
$ python F1C.py C:\Users\kroA100.tsp 100 5 NA
```

The output of this command includes the Gurobi Log. Once its over, the output shows the solution in JSON format, which consists of the set of centers, and the vertices assigned to each center. The solution size and the total runtime is also showed.

```
{"instance": "kroA100_Q1.tsp",
"centers": [
{ "center": 21, "nodes": [1, 6, 10, 11, 15, 17, 23, 24, 32, 36, 38, 45, 47, 49, 59, 63, 72, 74, 79, 91, 98, 99]},
{ "center": 43, "nodes": [3, 12, 14, 20, 27, 29, 30, 34, 35, 41, 46, 48, 55, 57, 71, 83, 100]},
{ "center": 61, "nodes": [7, 9, 25, 28, 44, 51, 54, 58, 60, 62, 64, 67, 69, 77, 81, 85, 86, 87, 93]},
{ "center": 75, "nodes": [4, 8, 16, 18, 19, 22, 26, 31, 42, 53, 56, 65, 66, 70, 80, 84, 88, 89, 90, 92, 94, 97]},
{ "center": 82, "nodes": [2, 5, 13, 33, 37, 39, 40, 50, 52, 68, 73, 76, 78, 95, 96]}
]}
Solution size: 895.6439024523083
Total runtime: 30.864023
```

## Citing
### MDPI and ACS Style
Cornejo Acosta, J.A.; García Díaz, J.; Menchaca-Méndez, R.; Menchaca-Méndez, R. Solving the Capacitated Vertex K-Center Problem through the Minimum Capacitated Dominating Set Problem. *Mathematics* **2020**, *8*, 1551.

### AMA Style
Cornejo Acosta JA, García Díaz J, Menchaca-Méndez R, Menchaca-Méndez R. Solving the Capacitated Vertex K-Center Problem through the Minimum Capacitated Dominating Set Problem. *Mathematics*. 2020; 8(9):1551.

### Chicago/Turabian Style
Cornejo Acosta, José A.; García Díaz, Jesús; Menchaca-Méndez, Ricardo; Menchaca-Méndez, Rolando. 2020. "Solving the Capacitated Vertex K-Center Problem through the Minimum Capacitated Dominating Set Problem." *Mathematics* 8, no. 9: 1551.
### BibTex
```
@article{ckc2020,
author = {{Cornejo Acosta}, Jos{\'{e}} Alejandro and {Garc{\'{i}}a D{\'{i}}az}, Jes{\'{u}}s and Menchaca-M{\'{e}}ndez, Ricardo and Menchaca-M{\'{e}}ndez, Rolando},
doi = {10.3390/math8091551},
issn = {2227-7390},
journal = {Mathematics},
keywords = {facility location,graph theory,integer programming,optimization},
month = {sep},
number = {9},
pages = {1551},
publisher = {MDPI},
title = {{Solving the Capacitated Vertex K-Center Problem through the Minimum Capacitated Dominating Set Problem}},
url = {https://www.mdpi.com/2227-7390/8/9/1551},
volume = {8},
year = {2020}
}
```

# Contact

* alexcornejo@inaoep.mx
* jesgadiaz@inaoep.mx
