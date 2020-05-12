const app = require("./app");

const host = "localhost";
const port = 3000;
app.listen(port, host, () => {
  console.log(`Server Started Go to http://${host}:${port}/upload`);
});
