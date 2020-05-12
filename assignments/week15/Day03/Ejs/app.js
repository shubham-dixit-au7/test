const path = require("path");
const express = require("express");
const router = require("./router/route");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.set("view engine", "ejs");

app.use("/", router);
app.use("/:id", router);

module.exports = app;
