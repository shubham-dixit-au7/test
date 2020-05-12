const upload = require("./../utils/storageMulter");
const isEmpty = require("./../utils/func");

exports.start = (req, res) => {
  res.render("main");
};

exports.fileUpload = function (req, res, next) {
  upload(req, res, function (err) {
    if (err) {
      return res.render("main", { status: "Cannot upload more than 12 files" });
    }
    let fileWritten = { ...req.files };

    if (!isEmpty(fileWritten)) {
      console.log("File Uploaded Succesfully");
      res.render("main", { status: "File Uploaded Succesfully" });
    } else {
      res.render("main", { status: "Select Files To Upload" });
    }
  });
};
