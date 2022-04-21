 function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    var date = today.getDate()+'/'+(today.getMonth()+1)+'/'+today.getFullYear();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('realTime').innerHTML =
    h + ":" + m + ":" + s + " - " + date;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  
    return i;
}

function goBack(){
    window.open("../index.html","_self");
}