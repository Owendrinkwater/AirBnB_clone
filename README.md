# AirBnB Clone - The Console

## Description
This is the first phase of the AirBnB clone project. In this step, we create a command-line interface (CLI) that simulates the console of the AirBnB web application. This CLI allows users to create, update, destroy, and retrieve instances of classes like `User`, `Place`, `City`, etc.

The goal is to build a foundation that will later be extended with file storage, database storage, API endpoints, front-end integration, and full web functionality.

---

## Command Interpreter

### How to Start
Clone the repository and run the console:

```bash
$ git clone https://github.com/Owendrinkwater/AirBnB_clone.git
$ cd AirBnB_clone
$ ./console.py

### How to use
Interactive mode
$ ./console.py
(hbnb) help
(hbnb) create User
(hbnb) show User <id>
(hbnb) quit

Non interactive mode
$ echo "create User" | ./console.py



