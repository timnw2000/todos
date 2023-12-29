# ToDo List Manager
---

A simple command-line utility for managing a ToDo list, using SQLite for storage.

This Tool can also be used in an collaborative environment. By adding the created hidden file `todos.db` to the repository, you can share todos with other, who can also manipulate that file using this command-line-tool.

## Features

- Initialize a new ToDo list database
- Add ToDo items with details
- Show all ToDo items
- Show history of completed ToDo items
- Remove ToDo items and add them to history

## Classes

### ToDos

A class to handle ToDo list operations.

### ToDo

A data class for representing a ToDo item.

#### Fields

- `todo`: The name of the ToDo item.
- `weekday`: The day of the week for the ToDo item.
- `description`: A description of the ToDo item.
- `importance`: The importance level of the ToDo item.
- `comments`: A comment left after completing a ToDo.
- `status`: The state the current ToDo is in. It is either `Pending ...`, `In Progress` or `Finished`.
- `action`: An action that has been taken.

## Usage

1. **Initialize the database**: Run the script with `todo init` to a create the database for the current Directory. Therefore each Directory can have their own ToDo-Manager.

    ```
    todo init
    ```
    

2. **Add a ToDo item**: Use `todo add <todo-name> <weekday>` to add a new item.

    ```
    todo add some_todo sunday
    ```

    The next prompts give you the opportunity to further describe your todo

    ```
    Description: some description
    ```

    ```
    Importance: high
    ```


3. **Show ToDo items**: Use `todo show` to display all items or `todo show [criteria]` for specific items. You can search for the `name`, `id`, `day` and `importance`.

    ```
    todo show 
    ```
    or
    ```
    todo show some_todo_name
    ```
    or 
    ```
    todo show 1
    ```
    or
    ```
    todo show sunday
    ```
    or 
    ```
    todo show high
    ```

    Output looks something like this:

        +------+---------------------------------+-----------+--------------+------------------------------------------+-------------+
        |   ID | ToDo                            | Weekday   | Importance   | Description                              | Status      |
        +======+=================================+===========+==============+==========================================+=============+
        |    1 | collaborations                  | sunday    | high         | Implementing collaboration functionality | Pending ... |
        +------+---------------------------------+-----------+--------------+------------------------------------------+-------------+
        |    2 | uploading first version to pypi | friday    | high         | Uploading current version to pypi        | Pending ... |
        +------+---------------------------------+-----------+--------------+------------------------------------------+-------------+





4. **Remove a ToDo item**: Use `todo remove <id_or_name>` to remove an item and add it to the history.

    ```
    todo remove 1 
    ```
    or
    ```
    todo remove some_todo_name
    ```

5. **Updating Status of ToDo**: Use `todo update <id_or_name>` to update the status of a ToDo from `pending` to `in progress`.

    ```
    todo update 1 
    ```
    or
    ```
    todo update some_todo
    ```




5. **Show History of completed ToDos**: Use `todo history` to display all items or `todo history [criteria]` for specific items. You can search for the `id`, `name` and `importance`.

    ```
    todo history 
    ```
    or
    ```
    todo history some_todo
    ```
    or 
    ```
    todo history 1
    ```
    or 
    ```
    todo history high
    ```

    Output looks something like this:

        +------+----------------+------------------+--------------+------------------------------------------+-----------------------------------------------------+----------+
        |   ID | ToDo           | Finished         | Importance   | Description                              | Comment                                             | Status   |
        +======+================+==================+==============+==========================================+=====================================================+==========+
        |    1 | collaborations | 29 December 2023 | high         | Implementing collaboration functionality | I should implement this feature in the next version | Finished |
        +------+----------------+------------------+--------------+------------------------------------------+-----------------------------------------------------+----------+



6. **Show Logs, which includes all actions**: Use `todo logs` to display all actions, that has been taken so far.

    ```
    todo logs
    ```

    Output looks something like this:

        +------+---------------------------------+------------------+-----------------+-------------+
        |   ID | ToDo                            | Time             | Action          | Status      |
        +======+=================================+==================+=================+=============+
        |    1 | collaborations                  | 28 December 2023 | Adding ToDo     | Pending ... |
        +------+---------------------------------+------------------+-----------------+-------------+
        |    2 | uploading first version to pypi | 29 December 2023 | Adding ToDo     | Pending ... |
        +------+---------------------------------+------------------+-----------------+-------------+
        |    3 | uploading first version to pypi | 29 December 2023 | Updating Status | In Progress |
        +------+---------------------------------+------------------+-----------------+-------------+
        |    4 | collaborations                  | 29 December 2023 | Removing ToDo   | Finished    |
        +------+---------------------------------+------------------+-----------------+-------------+



## Limitations

- The script expects command-line arguments for certain operations.
- Database initialization must be performed before any other operations.
- Error handling is primarily done through `sys.exit` with error messages.
