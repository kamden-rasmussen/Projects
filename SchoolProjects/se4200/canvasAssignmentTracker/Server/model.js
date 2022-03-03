const mongoose = require("mongoose");
mongoose.connect(
    ""
);

const assignment = mongoose.model("Assignment", {
    name: String,
    class: String,
    duedate: String,
    priority: String,
    notes: String,
});

module.exports = {
    assignmentDB: assignment,
};
