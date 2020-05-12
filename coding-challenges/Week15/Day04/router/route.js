const express = require("express");
const controller = require("./../controller/mathController");

const router = express.Router();
router.route("/add").post(controller.add);
router.route("/sub").post(controller.subtraction);
router.route("/mul").post(controller.multiplication);
router.route("/div").post(controller.division);

module.exports = router;
