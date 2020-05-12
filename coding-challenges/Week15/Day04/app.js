const express = require("express");
const dotenv = require("dotenv");
const router = require("./router/route");
dotenv.config({ path: `./config.env` });

const app = express();
app.use(express.json());

app.use("/mathOperation", router);

module.exports = app;
