exports.add = (req, res) => {
  const data = {
    num1: req.body.num1,
    num2: req.body.num2,
  };
  if (typeof data.num1 == "number" && typeof data.num2 == "number") {
    res.status(200).json({
      status: "Success",
      result: `Sum of ${data.num1} and ${data.num2} is ${
        data.num1 + data.num2
      }`,
    });
  }
  if (typeof data.num1 == "undefined" && typeof data.num2 == "undefined") {
    res.status(200).json({
      status: "Failed",
      result: `Enter Num1 and Num2 as Number`,
    });
  }
  if (typeof data.num1 != "number" || typeof data.num2 != "number") {
    res.status(404).json({
      status: "failed",
      message: "Invalid Input",
    });
  }
};

exports.subtraction = (req, res) => {
  const data = {
    num1: req.body.num1,
    num2: req.body.num2,
  };
  if (typeof data.num1 == "number" && typeof data.num2 == "number") {
    res.status(200).json({
      status: "Success",
      result: ` ${data.num1} - ${data.num2} is ${data.num1 - data.num2}`,
    });
  }
  if (typeof data.num1 == "undefined" && typeof data.num2 == "undefined") {
    res.status(200).json({
      status: "Failed",
      result: `Enter Num1 and Num2 as Number`,
    });
  }
  if (typeof data.num1 != "number" || typeof data.num2 != "number") {
    res.status(404).json({
      status: "failed",
      message: "Invalid Input",
    });
  }
};

exports.multiplication = (req, res) => {
  const data = {
    num1: req.body.num1,
    num2: req.body.num2,
  };
  if (typeof data.num1 == "number" && typeof data.num2 == "number") {
    res.status(200).json({
      status: "Success",
      result: `Multiple of ${data.num1} and ${data.num2} is ${
        data.num1 * data.num2
      }`,
    });
  }
  if (typeof data.num1 == "undefined" && typeof data.num2 == "undefined") {
    res.status(200).json({
      status: "Failed",
      result: `Enter Num1 and Num2 as Number`,
    });
  }
  if (typeof data.num1 != "number" || typeof data.num2 != "number") {
    res.status(404).json({
      status: "failed",
      message: "Invalid Input",
    });
  }
};

exports.division = (req, res) => {
  const data = {
    num1: req.body.num1,
    num2: req.body.num2,
  };
  if (typeof data.num1 == "number" && typeof data.num2 == "number") {
    res.status(200).json({
      status: "Success",
      result: `divison of ${data.num1} by ${data.num2} is ${
        data.num1 / data.num2
      }`,
    });
  }
  if (typeof data.num1 == "undefined" && typeof data.num2 == "undefined") {
    res.status(200).json({
      status: "Failed",
      result: `Enter Num1 and Num2 as Number`,
    });
  }
  if (typeof data.num1 != "number" || typeof data.num2 != "number") {
    res.status(404).json({
      status: "failed",
      message: "Invalid Input",
    });
  }
};
