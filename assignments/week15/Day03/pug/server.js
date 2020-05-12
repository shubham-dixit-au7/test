const app = require("./app");

let port = 300;

app.listen(port, "localhost", () => {
  console.log(`Listening on port : ${port}`);
});
