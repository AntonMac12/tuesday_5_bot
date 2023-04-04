CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    tg_id INTEGER,
    phone_number TEXT
);

CREATE TABLE users_location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    lat TEXT,
    lon TEXT,
    on_date DATETIME,

    CONSTRAINT fk_users  /* добавляем связь по внешнему ключу */
            FOREIGN KEY (user_id)  /* поле user_id - внешний ключ */
            REFERENCES users (id)  /* связывается с таблицей users, полем id */
);