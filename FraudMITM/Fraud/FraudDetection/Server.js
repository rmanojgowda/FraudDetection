const express = require("express");
const path = require("path");
const app = express();
const PORT = 3000;

// Serve static files from current directory
app.use(express.static(__dirname));
app.use(express.json());

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "Index.html"));
});

app.get("/product", (req, res) => {
  res.sendFile(path.join(__dirname, "Product.html"));
});

app.get("/payment", (req, res) => {
  res.sendFile(path.join(__dirname, "Payment.html"));
});

app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
