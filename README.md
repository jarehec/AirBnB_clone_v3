# hbnb - AirBnB_clone <img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/HBTN-hbnb-Final.png" width="160" height=auto />

## Description

Project attempts to clone the the AirBnB application and website, including the database, storage, RESTful API, Web Framework, and Front End.

<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/hbnb_step5.png" />

* __Environment:__ Ubuntu 14.04 LTS
* __python version:__ Python 3.4.3
* __style:__ PEP 8 (v. 1.7.0)

## Testing

This project uses python library, `unittest` to run tests on all python files.  All unittests are in the `./tests` directory with the command:

* `python3 -m unittest discover -v ./tests/`

This bash script executes all unittests, checks `pep8` style, and clears the storage file, `file.json`

```
$ ./dev/init_test.sh
```

### Interactive Tests

This project uses python library, `cmd` to run tests in an interactive command line interface.  To begin tests with the CLI, run this script:

```
$ ./console.py
```

## Authors

* MJ Johnson, [@mj31508](https://github.com/mj31508)
* David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/)

## License

Public Domain, no copyright protection
