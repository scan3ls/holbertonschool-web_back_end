const express = require('express');

const app = express();
const port = 7865;

app.get('/', (req, res) => {
  res.status(200);
  res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
  const id = parseInt(req.params.id);
  if (isNaN(id)) {
    res.status(404);
    res.send('Id must be a number');
  } else {
    res.status(200);
    res.send(`Payment methods for cart ${id}`);
  }
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
