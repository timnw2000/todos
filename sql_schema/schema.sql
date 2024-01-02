
-- Todo table includes all todos
CREATE TABLE todos (
    id INTEGER NOT NULL,
    todo TEXT NOT NULL,
    weekday TEXT NOT NULL,
    importance TEXT,
    description TEXT,
    status TEXT,
    PRIMARY KEY (id)
    UNIQUE (todo)
);

-- History table includes entire history of todos that were finished
CREATE TABLE history (
    id INTEGER NOT NULL,
    todo TEXT NOT NULL,
    finished_time TEXT NOT NULL,
    importance TEXT,
    description TEXT,
    comment TEXT,
    status TEXT,
    PRIMARY KEY (id)
);

-- Logs tables includes all actions
CREATE TABLE logs (
    id INTEGER NOT NULL,
    todo TEXT NOT NULL,
    time TEXT NOT NULL,
    action TEXT,
    status TEXT,
    PRIMARY KEY (id)
);
