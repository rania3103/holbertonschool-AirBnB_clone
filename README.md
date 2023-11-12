
<div align="center">
  <img src="images/img1.png" width="100%">
</div>

# [AirBnB clone - The Console](https://via.placeholder.com/10/00b48a?text=+)
This project is a simplified console clone for managing Airbnb-like objects. It allows users to create, update, and delete instances of different classes such as User, Place, State, City, Amenity, and Review. The project also includes serialization and deserialization functionality for storing instances in a JSON file.



[What’s a command interpreter?](https://via.placeholder.com/10/00b48a?text=+)  
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

    *Create a new object (ex: a new User or a new Place)  
    *Retrieve an object from a file, a database etc…  
    *Do operations on objects (count, compute stats, etc…)  
    *Update attributes of an object  
    *Destroy an object

<div align="center">
  <img src="images/img2.png" width="100%">
</div>

## [Usage](https://via.placeholder.com/10/00b48a?text=+)💻

```bash
./console.py
```
![Screen Recording](images/console.gif)
### [Prerequisites](https://via.placeholder.com/10/00b48a?text=+)

- Python 3.x
- Clone this repository to your local machine.

## [Testing](https://via.placeholder.com/10/00b48a?text=+) 🔎

Our shell work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```
also in non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## [Available commands](https://via.placeholder.com/10/00b48a?text=+) 🖊

| opcode            | functionnality                                                              |
| ----------------- | ------------------------------------------------------------------ |
| [quit or EOF](https://via.placeholder.com/10/00b48a?text=+) | [Exit the console.](https://via.placeholder.com/10/0a192f?text=+) |
| [create](https://via.placeholder.com/10/00b48a?text=+) | [Create a new instance of a class and save it to the JSON file.](https://via.placeholder.com/10/0a192f?text=+) |
| [show](https://via.placeholder.com/10/00b48a?text=+) | [ Display the string representation of an instance based on class name and id.](https://via.placeholder.com/10/0a192f?text=+) |
| [destroy](https://via.placeholder.com/10/00b48a?text=+) | [ Delete an instance based on class name and id.](https://via.placeholder.com/10/0a192f?text=+) |
| [all](https://via.placeholder.com/10/00b48a?text=+) | [Display string representation of all instances or all instances of a specific class..](https://via.placeholder.com/10/0a192f?text=+) |
| [update](https://via.placeholder.com/10/00b48a?text=+) | [ Update an instance based on class name and id by adding or updating attributes.](https://via.placeholder.com/10/0a192f?text=+)



## [Our files](https://via.placeholder.com/10/00b48a?text=+) 📁

```
   - AUTHORS: contributors to the project
   - console.py:  Main entry point for the console.
   - models/: Contains the class definitions 
   for BaseModel, User, Place, State, City, Amenity, and Review.
   - models/engine/: Contains the FileStorage class for 
   serialization and deserialization.
   - tests/: Contains unit tests for the project.
```


## [Authors](https://via.placeholder.com/10/00b48a?text=+)

- [@rania3103](https://www.github.com/rania3103)
