const app = require("./app");

let port = 3001;

app.listen(port, "localhost", () => {
  console.log(`Listening on port : ${port}`);
});
