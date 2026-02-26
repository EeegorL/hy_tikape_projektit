CREATE TABLE Users(
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    passwordHash TEXT NOT NULL /* plain text passwords should not be stored as is, so the password is hashed */
);