function whenChooseTeacher(id) {
    var course_id = document.getElementById("course_id").innerHTML;
    var teacher = document.getElementById(id).value;
    var httpReq = new XMLHttpRequest();
    var url = '/getTeacherCoursePage/' + course_id + '/' + teacher;
    httpReq.open('GET', url, true);
    httpReq.send();
    httpReq.onreadystatechange = function () {
        if (httpReq.status == 200 && httpReq.readyState == 4) {
            document.getElementById("getAjaxInfo").innerHTML = httpReq.responseText;
        }
    }
}