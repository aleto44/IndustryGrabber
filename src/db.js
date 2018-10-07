const express = require('express');
const bodyParser = require('body-parser');
const mysql      = require('mysql');
// https://github.com/mysqljs/mysql
const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'love1998',
  database : 'info2'
});

// Initialize the app
const app = express();

// https://expressjs.com/en/guide/routing.html
app.get('/companies', function (req, res) {
    connection.connect();

    connection.query('SELECT * FROM companies', function (error, results, fields) {
      if (error) throw error;
      res.send(results)
    });

    connection.end();
});
// Start the server
app.listen(3000, () => {
 console.log('Go to http://localhost:3000/companies to see posts');
});