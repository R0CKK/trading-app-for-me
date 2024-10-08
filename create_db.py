import mysql.connector

CREATE TABLE IF NOT EXISTS stock (
  id INT AUTO_INCREMENT PRIMARY KEY,
  symbol VARCHAR(20) NOT NULL UNIQUE,
  company VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS stock_price (
  id INT AUTO_INCREMENT PRIMARY KEY,
  stock_id INT,
  date DATE NOT NULL,
  open DECIMAL(10, 2) NOT NULL,
  high DECIMAL(10, 2) NOT NULL,
  low DECIMAL(10, 2) NOT NULL,
  close DECIMAL(10, 2) NOT NULL,
  adjusted_close DECIMAL(10, 2) NOT NULL,
  volume INT NOT NULL,
  FOREIGN KEY (stock_id) REFERENCES stock (id)
);
