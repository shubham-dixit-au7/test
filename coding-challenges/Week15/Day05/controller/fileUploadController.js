const upload = require("./../utils/storageMulter");
const isEmpty = require("./../utils/func");
var cloudinary = require("cloudinary").v2;

cloudinary.config({
  cloud_name: process.env.cloud_name,
  api_key: process.env.api_key,
  api_secret: process.env.api_secret,
});

exports.start = (req, res) => {
  res.render("main");
};

exports.fileUpload = function (req, res, next) {
  upload(req, res, function (err) {
    if (err) {
      return res.render("main", {
        status: "Cannot upload more than 1 image",
      });
    }
    try {
      let filetoCloud = req.files[0].originalname;
      let fileWritten = { ...req.files };

      if (!isEmpty(fileWritten)) {
        console.log("File Uploaded Succesfully");
        cloudinary.uploader.upload(`./uploads/${filetoCloud}`, function (
          error,
          result
        ) {
          if (error) console.log(error);
          console.log("File Uploaded To Cloud");
        });
        res.render("main", { status: "File Uploaded Succesfully" });
      } else {
        res.render("main", { status: "Select Files To Upload" });
      }
    } catch (err) {
      res.render("main", { status: "Something Went Wrong" });
    }
  });
};
