const router = require("express").Router();
const controller = require("./../controller/fileUploadController");

router.route("/upload").get(controller.fileUpload).post(controller.fileUpload);

module.exports = router;
