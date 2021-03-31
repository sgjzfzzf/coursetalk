whenChooseTeacher = function (id) {
    var teacher = document.getElementById(id).value;
    document.getElementById("teacher_name").innerHTML = "Course Teacher Name:" + teacher;
}