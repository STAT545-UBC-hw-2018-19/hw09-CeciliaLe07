## Welcome

This is the repository of the [**4th assigment**](https://github.com/STAT545-UBC/Classroom/blob/master/assignments/hw09/hw09.md) at [STAT547](http://stat545.com/Classroom/)

## Overview

This assignment consisted in modifying [this provided pipeline](https://github.com/STAT545-UBC/make-activity) into a new want that perform new tasks. 

The changes are:

+ Create a second report called **report 2** on pdf format which contains:

  - A barplot with the counts of words that start by each different letter of the alphabeth.
  
  - The data of most and less common inital letter
  
  - The counst of words that start with the different vowels

These changes can be watched at the following files:
  
|  Name  | Content |
|--------|---------|
|[Makefile](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/Makefile) | Creation of files: `report2.pdf`, `barplot.png`, `vowels_count.tsv`. Also the lines for phony targets `all` and  `clear` were updated|
|[barplot.R](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/barplot.R)  | The R script that generates the outputs [barplot.png](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/barplot.png) and [barplot_dat.tsv](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/barplot_dat.tsv) |
[vowels.py](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/vowels.py) | The python script that produces the output [vowels_count.tsv](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/vowels_count.tsv) |
|[report2.Rmd](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/report2.Rmd) | The `Rmarkdown` file that generates [the second report in pdf format](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/report2.pdf)|


<p align="center">
<img src="https://media.giphy.com/media/26AHyxxCItIbFijLO/giphy.gif" width="300" height="150"/>
</p>