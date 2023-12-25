# ToDo List Manager

A simple command-line utility for managing a ToDo list, using SQLite for storage.

## Features

- Initialize a new ToDo list database
- Add ToDo items with details
- Show all ToDo items
- Show history of completed ToDo items
- Remove ToDo items and add them to history

## Classes

### ToDos

A class to handle ToDo list operations.

#### Methods

- `__init__()`: Initializes the ToDo list. Connects to SQLite database or exits if the database is not initialized.
- `add(todo)`: Adds a new ToDo item to the list. Exits if the wrong number of command-line arguments are provided or if the weekday is invalid.
- `show()`: Displays all ToDo items in a tabulated format. Handles various search criteria.
- `show_history()`: Shows the history of completed ToDo items in a tabulated format.
- `create_database()`: Class method to create a new SQLite database with `todos` and `history` tables.
- `remove()`: Removes a ToDo item from the list and adds it to the history table.

### ToDo

A data class for representing a ToDo item.

#### Fields

- `todo`: The name of the ToDo item.
- `weekday`: The day of the week for the ToDo item.
- `description`: A description of the ToDo item.
- `importance`: The importance level of the ToDo item.

## Usage

1. **Initialize the database**: Run the script with `todo init` to create the database.
2. **Add a ToDo item**: Use `todo add <name> <weekday> <description> <importance>` to add a new item.
3. **Show ToDo items**: Use `todo show` to display all items or `todo show <criteria>` for specific items.
4. **Remove a ToDo item**: Use `todo remove <id_or_name>` to remove an item and add it to the history.

## Dependencies

- `dataclasses`: For the ToDo data class.
- `datetime`: To handle date and time operations.
- `os`: To interact with the operating system.
- `sqlite3`: For SQLite database operations.
- `sys`: To handle command-line arguments.
- `tabulate`: To display tables in the command line.

## Limitations

- The script expects command-line arguments for certain operations.
- Database initialization must be performed before any other operations.
- Error handling is primarily done through `sys.exit` with error messages.
