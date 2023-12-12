console.log("app.js loaded");

var year = new Date().getFullYear();
var month = new Date().getMonth() + 1;
var day = new Date().getDate();

footer = document.getElementById("footer");
footer.getElementsByTagName("p")[0].innerHTML += year;
