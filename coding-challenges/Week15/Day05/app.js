const express = require("express");
const router = require("./router/route");

const app = express();
app.set("view engine", "hbs");

app.use("/", router);
module.exports = app;
