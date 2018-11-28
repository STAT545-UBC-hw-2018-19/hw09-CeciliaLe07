## Welcome

This is the repository of the [**4th assigment**](https://github.com/STAT545-UBC/Classroom/blob/master/assignments/hw09/hw09.md) at [STAT547](http://stat545.com/Classroom/)

## Overview

This assignment consisted in modifying [this provided pipeline](https://github.com/STAT545-UBC/make-activity) into a new want that perform new tasks. 

The changes are:

+ Create a second report called **report 2** on pdf format which contains:

  - A barplot with the counts of words that start by each different letter of the alphabeth.
  
  - The data of most and less common inital letter
  
  - The counts of words that start with the different vowels

+ Add 4 different phony targets `report_type2`, `clean_type2`, `report_type1` and `clean_type1` to create/delete the two types of report.

These changes can be watched at the following files:
  
|  Name  | Content |
|--------|---------|
|[Makefile](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/Makefile) | Creation of files: `report2.pdf`, `barplot.png`, `vowels_count.tsv`. The lines for phony targets `all` and  `clear` were updated. Four new phony targets added.|
|[barplot.R](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/barplot.R)  | The R script that generates the outputs [barplot.png](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/barplot.png) and [barplot_dat.tsv](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/barplot_dat.tsv) |
[vowels.py](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/vowels.py) | The python script that produces the output [vowels_count.tsv](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/vowels_count.tsv) |
|[report2.Rmd](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/report2.Rmd) | The `Rmarkdown` file that generates [the second report in pdf format](https://github.com/STAT545-UBC-students/hw09-CeciliaLe07/blob/master/report2.pdf)|

## Sources to get extra help

+ https://stackoverflow.com/questions/28432607/pandoc-version-1-12-3-or-higher-is-required-and-was-not-found-r-shiny



<p align="center">
<img src="https://media.giphy.com/media/26AHyxxCItIbFijLO/giphy.gif" width="300" height="150"/>
</p>