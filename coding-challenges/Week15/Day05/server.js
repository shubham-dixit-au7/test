const dotenv = require("dotenv");

dotenv.config({ path: "./config.env" });
const host = "localhost";

const app = require("./app");

const port = 3000;
app.listen(port, host, () => {
  console.log(`Server Started Go to http://${host}:${port}/upload`);
});
