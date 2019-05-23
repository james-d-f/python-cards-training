# Python Cards Training
## Contents:
* [Project Summary](#Project-Summary)
* [File Structure](#File-Structure)
* [Setup](#Setup)
* [Session One](#Session-One)
* [Assignment](#Reviewing-the-Assignment)
* [Reviewing the Assignment](#Reviewing-the-Assignment)
* [Session Two](#Session-Two)
* [Additional Reading](#Additional-Reading)

---
## Project Summary
This project models a playing card in Python.

This project demonstrates basic Python features, including:

0. Setup - Virtual environments and pipenv *
1. Classes
2. Functions and magic methods
3. Class attributes
4. Importing modules
5. Class methods
6. Formatting and Linting *
7. Docstrings
8. Dataclasses
9. Exceptions
10. 3rd party packages
11. Testing with pytest
12. Using 3rd party packages
13. Generators
14. Debugging
15. Typing and MyPy *
16. Immutability *

(* Includes explanation slides)
[Python Slides](https://docs.google.com/presentation/d/1lPxt7WF5IMX6muThL46N9cJc_ZleAgIGy9pu0mBVsuA/edit#slide=id.g57842172a5_0_75)

---
## File Structure
These are the core files in the project
* [`mypy.ini`](mypy.ini)
* [`Pipfile`](Pipfile)
* [`Pipfile.lock`](Pipfile.lock)
* [`src/card.py`](src/card.py)
* [`src/create_card_image.py`](src/create_card_image.py)
* [`tests/test_card.py`](tests/test_card.py)

The Python core files are also full solutions to the assignment. **You are very strongly discouraged to view these files if you are attempting the assignment.**

The Python core files also have partial versions (e.g. `card_0_classes.py`) that demonstrate a step by step process of adding complexity that culminates in the core Python files of the project. These do not contain solutions to the assignment.

---
## Setup
``` shell
pip3 install black
pip3 install mypy
pip3 install pipenv
pip3 install flake8
```

Install VS Code Python extension.
Add these to your VS Code `settings.json`.

``` json
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "/usr/local/bin/black",
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Path": "/usr/local/bin/flake8",
    "python.linting.flake8Args": [
        "--max-line-length=88"
    ],
    "python.linting.mypyEnabled": true,
    "python.linting.mypyPath": "/usr/local/bin/mypy",
    "python.linting.pylintEnabled": false,
    "python.testing.pyTestEnabled": true,
    "python.testing.noseEnabled": false,
    "python.testing.unittestEnabled": false,
```

Create a new folder for the project.
In this folder:

``` shell
pipenv install
```

---
## Session One
This session should cover:

0. Setup
    * Explain:
        * Project structure
        * `pip` and `pipenv`
    * Create:
        * Folder for project
        * `src` folder
    * Run:
        * All of the `## Setup` steps
1. Classes
    * `card_0`
    * Create a basic class for a card 
2. Functions and magic methods
    * `card_1`
	* `__repr__()`
3. Class attributes
    * `card_2`
	* Card ranks and suits
	* Can now implement `__add__`  and `__int__` 
4. Importing
    * `card_2`
	* `from random import choice`
5. Class methods
    * `card_2`
	* `random()`
6. Formatting and Linting
    * Explain and demonstrate:
        * [PEP8](https://www.python.org/dev/peps/pep-0008/)
        * Flake8
        * Black
7. Docstrings
    * `card_3`
    * Add examples of docstrings. Show VS Code reading them.
8. Dataclasses
    * `card_4`
    * Demonstrate missing methods like `__eq__`
	* Ordering 
        * Explain `__post_init__`
        * Show private method with underscore
9. Exceptions
    * `card_6`
10. Packages
    * Explain:
        * `pipenv` packages and dev packages
    * Run:
        * `pipenv install pillow`
        * `pipenv install --dev pytest`
11. Testing (Continued in assignment)
    * `test_card_0`
    * Create:
        * `tests` folder
        * `test_card.py` file
    * Explain:
        * `assert`
        * pytest
    * Run:
        * `pipenv run python -m pytest` in project directory
    * `test_card_1`
    * Explain:
        * `isinstance`
    * `test_card_2`
    * Explain:
        * Fixtures
    * `test_card_3`
    * Explain:
        * `pytest.raises()`
12. Create image (Continued in assignment)
    * `create_card_image_0`

---
## Assignment
Between session one and two there are the following assignment tasks. These are fully implemented in the core files (e.g. `src/card.py`).

### Add features to `card.py`

#### Add the `_convert_suit()` function
The `_convert_suit()` function will be added to `__post_init__()` and run before the `_add_sort_index_field()` function.

It will take the current suit, and if it is the "name" of a suit (e.g. 'Spade' or 'Spades') convert it to the symbol (e.g. '♠').

It will then update the value of `self.suit` to the symbol.

#### Add the `all()` function
The `all()` function should return all possible valid cards for the class. This should be every combination of rank and suit. `all()` should be a classmethod, and callable as `Card.all()`.

##### Simple:
Return a `list` of all cards.

##### Advanced:
Return a [generator](https://wiki.python.org/moin/Generators) for all cards.


### Add additional tests
[Starting from a base of `test_card_3_raises.py`]

At this stage of the `Card` class, some of these tests will fail. They are marked with #Fail.
Tests that depend on the assignment work are marked with #Assignment.

These tests should be added to your `test_card.py` file:

* `test_init_name()`
    * Passes if a card instance can be created when the suit is given as a name (e.g. 'Spade').
* `test_init_name_plural()` #Assignment
    * Passes if a card instance can be created when the suit is given as a plural name (e.g. 'Spades').
* `test_init_random()`
    * Passes if a card instance can be created with the `Card.random()` method.
* `test_init_random_multiple()`
    * Tests that `Card.random()` outputs different cards each time.
* Fixture `deck()`
    * Add a pytest fixture which is a list of at least 5 different cards.
* Fixtures for more cards
    * Add at least two more fixtures for individual cards.
* `test_str()`
    * Passes if card instances match their expected string representation.
    * Test more than one card instance.
* `test_eq()`
    * Passes if:
        * A card is equal (`==`) to itself.
        * A card is equal to another instance of the same card (same rank and suit).
        * A card is not equal (`!=`) to a different card. 
* `test_add()`
    * Passes if all of these give a correct result:
        * `Card` + `Card`
        * `Card` + `int`
        * `int` + `Card`
        * `Card` (with non numeric rank) + `Card`
        * `Card` (with non numeric rank) + `int`
* `test_sum()`
    * Passes if the `sum()` of the deck fixture is correct.
* `test_ordering`
    * Passes if:
        * Less than operator works correctly.
        * Greater than operator works correctly.
        * `sorted(deck)` gives a correctly sorted list of cards.
* `test_hash()` #Fail
    * Passes if cards can be hashed (`hash()`)
* `test_frozen` #Fail
    * Passes if changing the rank or suit of a card results in a `dataclasses.FrozenInstanceError` error.
* `test_all` #Assignment
    * Passes if:
        * `Card.all()` returns all of the possible cards.
        * `Card.all()` is a [generator](https://wiki.python.org/moin/Generators).

### Improve `create_card_image()`
This is an open ended tasks to improve the `create_card_image()` function to output better card images. You can chose to make your images as traditional or non-traditional as you want.

Some traditional things you may want to try adding:
* A border around your card.
    * Probably with a margin.
    * Your border could be simple, or multilayered and patterned.
* The symbol and rank flipped in the bottom right corner.
    * To ensure the card's top left corner is visible in either orientation.
        * _Hint:_ If you make a change to an `Image` object, you will need to make a new `Draw` object to draw on the image correctly
        * I'm willing to provide a code snippet to help with image rotation
* Symbols in the centre of the card.
    * Matching the suit.
    * With a count matching the rank.
    * Center a large version of the symbol for aces.
    * Have the symbols arranged half one way up, and half flipped.

Useful links:
[Pillow Image Reference](https://pillow.readthedocs.io/en/3.1.x/reference/Image.html)
[Pillow Image Draw Reference](https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html)

---
## Reviewing the Assignment
**This section is intended for mentors who are reviewing a trainee's work on the assignment.**

After the assignment and sessions two, the trainee's code should resemble the [core files](#File-structure).

The trainee's [card class file](src/card.py) should loosely match the example. It is possible they may not have implemented some of the things added in session two, such as immutability and type hints. The version of the code they will have started with at the end of sessions one is [version 6](src/card_6_exceptions.py). Implementing `all()` with a generator was given as an advanced option, but simply returning a list of all cards is fine, generators are explained in session two. Ensure their code is clean, with good naming, docstrings, and comments where appropriate. Discuss with them if you feel this is not the case.

The trainee's [test file](tests/test_card.py) should closely match the example, with some difference choices made for the fixtures. Ensure they have implemented the multiple random test in a way they won't fail for some proportion of the runs.

Since the [`create_card_image.py`](src/create_card_image.py)  part of the assignment is very open ended, the trainee's code is unlikely to match the example very closely. Use the [core file](src/create_card_image.py) to see a valid approach and some examples of image manipulation, and use your own judgement of good code to assess their approach. It is fine for the outputted images to be very none traditional, for the examples generated by [`create_card_image.py`](src/create_card_image.py), see the [Card Images](Card-Images) folder.

---
## Session Two
This session should cover:

Sessions One followup:
* Recap session one using the examples files
* Check for questions

Assignment followup:
* Talk about any issues encountered
* Compare card images generated

13. `all()` (Expand from assignment)
    * Generators (Briefly)
14. Debugging
    * Show debugging in VS Code
15. Typing
    * `card_7`
	* Add `mypy.ini`
    * Explain:
        * Types
        * MyPy 
16. Frozen dataclass
    * `card_8`
    * Explain:
        * Immutability
            * e.g. `list` vs `tuple`


## Additional Reading
[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

[Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

[Black Autoformatter](https://github.com/python/black)

[Data Structures (Lists, Tuples, Sets, Dicts)](https://docs.python.org/3/tutorial/datastructures.html#)

[Exceptions](https://docs.python.org/3/tutorial/errors.html)

[List comprehension](https://hackernoon.com/list-comprehension-in-python-8895a785550b)

[Decorators](https://realpython.com/primer-on-python-decorators/)

[Dataclasses](https://docs.python.org/3/library/dataclasses.html)

[Testing with Pytest](https://docs.pytest.org/en/latest/getting-started.html)

[Using Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

[Generators](https://realpython.com/introduction-to-python-generators/)

[Typing in Python](https://realpython.com/python-type-checking/)

[Typing cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

[Immutability in Python](https://towardsdatascience.com/https-towardsdatascience-com-python-basics-mutable-vs-immutable-objects-829a0cb1530a)

[Properties (getters and setters)](https://www.python-course.eu/python3_properties.php)
