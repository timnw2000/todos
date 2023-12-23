
-- Todo table includes all todos
CREATE TABLE todos (
    id INTEGER NOT NULL,
    todo TEXT NOT NULL,
    weekday TEXT NOT NULL,
    importance TEXT,
    description TEXT,
    PRIMARY KEY (id)
    UNIQUE (todo)
);

-- Log table includes entire history of todos that were finished
CREATE TABLE history (
    id INTEGER NOT NULL,
    todo TEXT NOT NULL,
    scheduled TEXT NOT NULL,
    finished_weekday TEXT NOT NULL,
    importance TEXT,
    description TEXT
);
