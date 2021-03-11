# py-stick-path #

## Description ##

Receives arrays of stick paths and returns all solutions considering all paths must turn everytime it's possible.

*Example :*

**Input**
````
7 7
A  B  C 
|  |  | 
|--|  | 
|  |--| 
|  |--| 
|  |  | 
1  2  3
````

**Output**
````
A2 
B1 
C3 
````

## Usage ##

### Calling script ###

A simple script "paths_script.py" can be called in a console :
````
C:\Users\Leogiciel\Peacock\py-stick-path> python paths_script.py '22 18
>> P  Q  R  S  T  U  V  W
>> |  |  |  |  |--|  |  |
>> |  |  |--|  |  |  |--|
>> |  |--|  |--|  |  |  |
>> |--|  |--|  |  |  |--|
>> |--|  |  |  |  |--|  |
>> |  |--|  |  |--|  |--|
>> |  |  |  |--|  |--|  |
>> |--|  |  |  |--|  |  |
>> |  |  |--|  |  |  |  |
>> |  |  |  |--|  |  |--|
>> |  |  |  |  |--|  |  |
>> |--|  |  |  |  |  |  |
>> |--|  |--|  |  |  |--|
>> |  |--|  |  |--|  |  |
>> |  |  |--|  |  |  |--|
>> |--|  |--|  |  |--|  |
>> 1  2  3  4  5  6  7  8 '
P3
Q7
R8
S5
T6
U2
V4
W1
````

### main.py ###

This file can be runned. It executes unit tests on given functional requirements.

## TODO ##

Add some logs.

Raise exceptions on invalid received datas.