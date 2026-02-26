CREATE TABLE Messages(
    id INT PRIMARY KEY,
    user INT REFERENCES User(id),
    conversation INT REFERENCES Conversations(id),
    message TEXT NOT NULL
);