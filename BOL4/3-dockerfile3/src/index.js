const express = require("express");
const path = require("path");
require("dotenv").config();

const app = express();
const port = process.env.PORT || 3000;
const message = process.env.WELCOME_MESSAGE || "Merhaba Docker Multi-Stage!";

app.use(express.static(path.join(__dirname, "public")));

app.get("/api/message", (req, res) => {
  res.json({ message });
});

app.listen(port, () => {
  console.log(`Server ${port} portunda çalışıyor`);
});