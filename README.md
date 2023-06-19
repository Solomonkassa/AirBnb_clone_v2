# Airbnb Clone_v2 Project

![logo](https://github.com/Solomonkassa/Solomonkassa/blob/main/hbnb.png)

------------------------------------------------------------------------------------------------------------------------------
This Airbnb Console Project is a command-line interface tool that allows users to interact with an AirBnB-like database from the comfort of their terminal. It was developed using Python and includes features like data manipulation, searching, filtering, and more.

## Getting Started

To get started with this project, you'll need to have Python 3 installed on your system. You can download the latest version of Python from the official website. Additionally, you'll need to set up a MySQL database. Follow these steps to set up the project:

1. Clone the repository:

2. Install the necessary dependencies using pip:

3. Set up a MySQL database and update the configuration:
    - Create a new MySQL database for the project.
    - Update the `models/engine/db_storage.py` file with your database connection details (host, user, password, database).

## Usage

To use the Airbnb Console, simply run the `console.py` file:

This will start the console, and you'll be presented with a prompt where you can enter commands to interact with the database. Here are some of the available commands:

- `create <class_name>`: Creates a new instance of the specified class.
- `show <class_name> <id>`: Displays the specified instance.
- `destroy <class_name> <id>`: Deletes the specified instance.
- `all <class_name>`: Displays all instances of the specified class.
- `update <class_name> <id> <attribute_name> "<attribute_value>"`: Updates the specified attribute of the specified instance.

For a full list of available commands, you can type `help` at the prompt.

## Data Persistence

The Airbnb Console uses a MySQL database as the engine for data persistence. The connection details are provided in the `models/engine/db_storage.py` file. When running the console, the data will be stored and retrieved from the MySQL database.

## Tests

This project includes a suite of tests to ensure that everything is working as expected. To run the tests, simply run the `test_console.py` file:


## Contributing

This is an open-source project, and contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes.

### Contributors

- [Solomon Kassa](https://github.com/Solomonkassa/)
- [Hiwot Zeleke](https://github.com/BHiwot)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Solomonkassa/AirBnB_clone/blob/main/LICENSE) file for details.
