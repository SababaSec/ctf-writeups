const express = require('express');
const path = require('path')
const app = express();

require('dotenv').config();

app.use(express.urlencoded({extended: true}));
app.use(express.json());
app.use('/static', express.static(path.join(__dirname, 'static')))

const port = process.env.PORT || 3000;
const nope = '🚫';

// PLANET-TC39-1
app.get('/planet-tc39-1', (req, res) => res.sendFile(path.join(__dirname, 'views/planet-tc39-1.html')));
app.post('/planet-tc39-1', (req, res) => {
  const { a, b } = req.body;
  
  if (a !== b) { res.send(nope); return; }
  if (1/a === 1/b) { res.send(nope); return; }

  res.send(process.env.FLAG_1 || "No way. Contact an admin.");
});

// PLANET-TC39-2
app.get('/planet-tc39-2', (req, res) => res.sendFile(path.join(__dirname, '/views/planet-tc39-2.html')));
app.post('/planet-tc39-2', (req, res) => {
  const { a, b } = req.body;

  if (!Number.isSafeInteger(a)) { res.send(nope); return; }
  if (!Number.isSafeInteger(b)) { res.send(nope); return; }

  if (a !== b) { res.send(nope); return; }
  if (1/a === 1/b) { res.send(nope); return; }

  res.send(process.env.FLAG_2 || "No way. Contact an admin.");
});


app.listen(port, () => console.log(`Planet-TC39 listening on port ${port}`));