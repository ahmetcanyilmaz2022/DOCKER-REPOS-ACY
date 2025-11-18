const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.json({ message: "Ana rota çalışıyor!" });
});

router.get("/users", (req, res) => {
  res.json([
    { id: 1, name: "Ahmet" },
    { id: 2, name: "Can" }
  ]);
});

router.post("/login", (req, res) => {
  const { username } = req.body;
  res.json({ message: `Hoş geldin ${username}!` });
});

module.exports = router;
