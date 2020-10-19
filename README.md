# Text Detector

an ML like application to detect text subject.

!!! only for utf-8 files !!!

## Usage

there are two main ways to use this application :

<h3>1.with interactive menu</h3>
	
to use this menu just run the `main.py` with out any arguments.

<h3>2.with arguments</h3>

`$ python ./main.py SWITCH [PARAMETERS]`

Switchs :

***-a*** : add new file to database

ex:
`$ python ./main.py  -a  CATEGORYNAME  FILENAME`

***-p*** : process a file and show it's scores

ex:
`$ python ./main.py  -p  FILENAME`

***-c*** : show all avaliable categories

ex:
`$ python ./main.py  -c`

***-w*** : wipe database

ex:
`$ python ./main.py  -w`

***-h*** , ***--help*** , ***/?*** : show help message

ex:
`$ python ./main.py -h`

## How it works

First you must add many text files to the database and tell the program their category.

The program will count all words of given text and store them in the database.



While processing a text file, the program will compare percentage of each word in text file with it's database.
The most similar category to the file will get most score. So the answer is the category wich has the greatest score.