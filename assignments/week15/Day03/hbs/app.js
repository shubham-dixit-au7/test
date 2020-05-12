const path = require("path");
const express = require("express");
const router = require("./router/route");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.set("view engine", "hbs");
app.set("views", path.join(__dirname, "views"));
app.use("/", router);
app.use("/:id", router);
// app.get("/", (req, res) => {
//   res.render("main", { data: ["Praveen", "nagaraj"] });
// });

module.exports = app;

// app.listen(3000, "localhost", () => {
//   console.log("Started");
// });
