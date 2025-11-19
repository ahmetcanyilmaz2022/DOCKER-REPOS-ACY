const express = require('express');
const mysql = require('mysql2');
const app = express();
const port = 3000;

// JSON body parsing
app.use(express.json());

// MySQL connection
const connection = mysql.createConnection({
  host: process.env.DB_HOST || 'db',
  user: process.env.DB_USER || 'root',
  password: process.env.DB_PASSWORD || '1234',
  database: process.env.DB_NAME || 'demo'
});

// Test route
app.get('/users', (req, res) => {
  connection.query('SELECT 1+1 AS solution', (err, results) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: err.message });
    }
    res.json(results);
  });
});

// Health check route
app.get('/health', (req, res) => {
  res.json({ status: 'API is healthy 🚀' });
});

// Start server
app.listen(port, () => {
  console.log(`API listening on port ${port}`);
});