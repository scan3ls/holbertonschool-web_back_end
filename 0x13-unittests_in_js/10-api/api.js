const express = require('express');

const app = express();
const port = 7865;

app.use(express.json())

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

app.get('/available_payments', (req, res) => {
  const payload = {
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  };

  res.status(200);
  res.send(payload);
});

app.post('/login', (req, res) => {
  const user = req.body.userName;
  if (user) {
    res.status(200);
    res.send(`Welcome ${user}`);
  } else {
    console.log(req.body);
    res.status(404);
    res.send("Unknown user");
  } 
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
