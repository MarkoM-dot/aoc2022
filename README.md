# Advent of Code 2022

## Introduction

This repo contains some answers to the advent of code puzzles and support modules.

Get started by executing the following commands to set up your environment.

```shell
poetry shell
poetry install
```

This repo contains three modules and a data dump. 

## aoc

The `aoc` module is a CLI tool to view the puzzle question, store/view puzzle data, and
submit your answer. You only need to provide the value of your session cookie in a
`.cookie` file in the working directory. If you don't you cannot submit your answers.

Check out the cli tool:

```shell
python -m aoc --help
```
![image](https://user-images.githubusercontent.com/83985775/205521984-2eb9d642-b334-495d-b0a3-f4764c8f33c2.png)

## aoc2022

The `aoc2022` module has been turned into a cli tool to quickly view answers making it
easier to sumbit solutions via the command line. Check it out in the familiar way:

```shell
python -m aoc2022 -h
```
![image](https://user-images.githubusercontent.com/83985775/205522077-81706718-63cd-43ae-97f7-83a61941e327.png)

## tests

This module contains the tests provided by AOC or some I have time to make myself. 
Run them with the following command:

```shell
python -m unittest
```

## data

The `data` folder contains puzzle input as text files. Puzzle input is required to
see if the potential solutions provided in `aoc2022` run or not.


## Methodology

1. Get the value of your session cookie by visiting the site and store this value in a
`.cookie` file -- never commit this to source control, it should be gitignored anyway.

2. Check out the puzzle question:
```shell
python -m aoc 3 question
```

![image](https://user-images.githubusercontent.com/83985775/205522107-ce1a1c92-0b69-4202-b932-9c0a36a95290.png)

3. Write a test in the the `tests` folder. Run the tests and watch them fail.

4. Write a solution in the `aoc2022` folder and import it in the `__init__.py`
file... I've automated the boring stuff.

5. Run the tests again watch them pass..

6. Fetch the puzzle input:
```shell
python -m aoc 3 data
```

7. Check to see if your data folder is populated with some puzzle data. Remember the path,
you'll need it for your solution class.

8. Run the `aoc` module and check your answer.
```shell
python -m aoc2022 --day 3
```

![image](https://user-images.githubusercontent.com/83985775/205522183-5357d4fb-a461-464c-9f4e-b494f56fa2ff.png)

9. If you are happy with what you've got. It's time to submit what you see.
```shell
python -m aoc 1 submit <answer> --part 1
```

10. Read the response in the terminal. If you've submitted a successful soluion, you may 
now kiss... uh, check out the question again. You will see the second part of the puzzle.
If you are done with part two just increment the day. Rinse and repeat from part 2.
```shell
python -m aoc 1 question
```

## Conclusion

Advent of Code rocks and you know it. Code katas typically have you fill in the blanks,
maybe write your answer below an already defined method. The same can't be said of these
puzzles. 

Happy holidays!
