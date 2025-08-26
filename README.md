<h1 align="center">pylogic</h1>

<div align=center>

[![GitHub Release](https://img.shields.io/github/v/release/kuroninninja/pylogic?style=for-the-badge)](https://www.github.com/kuroninninja/pylogic/releases/latest)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/kuroninninja/pylogic/latest?style=for-the-badge)](https://github.com/kuroninninja/pylogic/commits/main/)
[![Python Version](https://img.shields.io/badge/python->3.13.2-%233776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads)
[![Static Badge](https://img.shields.io/badge/coverage-71%25-yellow?style=for-the-badge)
](https://kuroninninja.github.io/pylogic/)

[![standard-readme](https://img.shields.io/badge/readme_style-standard-green?style=for-the-badge)](https://www.github.com/RichardLitt/standard-readme)
[![code style black](https://img.shields.io/badge/code_style-black-black?style=for-the-badge)](https://black.readthedocs.io/en/stable/index.html)


</div>

**A simple module for simulating Boolean logic operations**

`pylogic` is a small module made just for the purpose of simulating logic gates and their interactions.

The module contains all of the essential gates (as listed by [Wikipedia](https://en.wikipedia.org/wiki/Logic_gate#)) and a class for binary numbers specifically designed for passing through the logic operations.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
    - [Import](#import)
    - [Binary Numbers](#binary-numbers)
    - [Logic](#logic)
    - [merge()](#merge)
    - [CBAS](#cbas)
- [Docs](#docs)
- [Acknowledgements](#acknowledgements)

## Install

Ensure that Python version _3.13.2 or later_ is installed:

```bash
# Windows
python --version

# MacOS/Linux
python3 --version
```

If not, [download the latest version of Python](https://www.python.org/downloads/).

Next, [download the latest release](https://www.github.com/kuroninninja/pylogic/releases/latest) and unzip the .zip file.

Finally, move the folder into your main directory as shown:

```
<directory>
├──pylogic
├──<main>.py
└──...
```

## Usage

### Import

Begin a file by importing the module:

```python
>>> from pylogic.gates import *
```

### Binary Numbers

Next, create a `BinaryNum` instance

```python
>>> input_a = BinaryNum(num, bits)
```

where `num` is the numerical value (e.g. `101`) and `bits` is the number of bits (e.g. `32` for a 32-bit integer).

> Note: currently, `pylogic` does _**NOT**_ support a `BinaryNum` with a decimal point (e.g. `101` is supported but `101.1` is not).

Printing the `Num` returns its value:

```python
>>> ex_num = BinaryNum(1010, 4)
>>> ex_num
1010
```

### Logic

Now that you've created a `BinaryNum`, use logic gates!

```python
>>> num_0 = BinaryNum(0, 1)
>>> num_1 = BinaryNum(1, 1)
>>> AND(num_1, num_0)
0
>>> OR(num_1, num_0)
1
```

> Note that for all logic operations, the value must be 1 digit (the `bits` parameter doesn't matter).

### merge()

A helpful utility function is `merge()`: it takes a list of `BinaryNum` instances and returns one `BinaryNum` whose values are appended to one another:

```python
>>> merge([num_1, num_0])
10
```

Note that regardless of the previous bit values of the input numbers, the output bits will always be the minimum possible value:

```python
>>> merge([num_1, num_0]).bits
2
```

This can be changed by specifying the number of bits with the argument `bits`:

```python
>>> merge([num_1, num_0], bits=8)
000000010
```

### CBAS

The CBAS _(Computer Boolean Algebra System)_ is a handy way to shorten long expressions, such as when creating a full adder.

The CBAS is able to take a Boolean algebra equation, such as `"(1*0)•(0*1)"`, and can output the result of the equation in the form of a `BinaryNum` instance.

Firstly, import the CBAS:

```python
>>> from pylogic import cbas
```

Just pass the expression through the CBAS as follows:

```python
>>> cbas.calculate("(1*0)•(0*1)")
1
```

> Please note that one **MUST** use the correct Unicode characters as shown below. You can print them by using `cbas.reference()`:
> ```
> >>> cbas.reference()
> NOT | AND | NAND | XOR
>  L  |  •  |  ^   |  *
> 
> XNOR | OR | NOR | IMPLY | NIMPLY
>  o   | +  |  ±  |   >   |   *L
> ```
> Note that `•` is `ALT+8` and `±` is `ALT-SHIFT-+`.

The order of operations is as follows:
```
Parenthesis
NOT
AND
NAND
XOR
XNOR
OR
NOR
IMPLY
```

## Docs

A full list of classes and functions can be found at [the wiki](https://www.github.com/kuroninninja/pylogic/wiki).

## Acknowledgements

Thanks to [ModPunchtree on YouTube](https://www.youtube.com/@ModPunchtree) for their [tutorial on the Shunting Yard algorithm](https://www.youtube.com/watch?v=ybRWZC9gYjM).
