const app = require("./app");

const port = process.env.PORT;
const host = process.env.HOST;

app.listen(port, host, () => {
  console.log(`Server running on http://${host}:${port}`);
});
