CREATE TABLE Feedback(
    id INT PRIMARY KEY,
    conversation INT REFERENCES Conversations(id), /* feedback is linked to the conversation between buyer and seller rather than the listing */
    rating INT NOT NULL, /* e.g. 1-5 */
    feedback TEXT
);