CREATE TABLE greetings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255)
);

INSERT INTO greetings (message) 
VALUES ('Hello from MySQL inside Docker 🚀');