var body = document.getElementsByTagName("body");
var button1 = document.getElementById("button1");
var button2 = document.getElementById("button2");
var button3 = document.getElementById("button3");
var button4 = document.getElementById("button4");
var button5 = document.getElementById("button5");
var button6 = document.getElementById("button6");
var button7 = document.getElementById("button7");
var button8 = document.getElementById("button8");
var button9 = document.getElementById("button9");
var escupinada = document.getElementById("escupinada");
var bota = document.getElementById("bota");
var cowboy = document.getElementById("cowboy");
var sang = document.getElementById("sang");
var locomotora = document.getElementById("locomotora");
var revolver = document.getElementById("revolver");
var fletxa1 = document.getElementById("fletxa1");
var fletxa2 = document.getElementById("fletxa2");
var fletxa3 = document.getElementById("fletxa3");
var fletxa4 = document.getElementById("fletxa4");
var fletxa5 = document.getElementById("fletxa5");
var fletxa6 = document.getElementById("fletxa6");

button1.addEventListener("click", function() {
    escupinada.style.display = "block";
    escupinada.classList.add("a_escupinada");
    cowboy.style.display = "block";
    cowboy.classList.add("a_cowboy1");
});

button2.addEventListener("click", function() {
    bota.style.display = "block";
    bota.classList.add("a_bota");
    cowboy.style.display = "block";
    cowboy.classList.add("a_cowboy2");
    sang.classList.add("a_sang2");
});

button3.addEventListener("click", function() {
    revolver.style.display = "block";
    revolver.classList.add("a_revolver");
    cowboy.style.display = "block";
    cowboy.classList.add("a_cowboy3");
    sang.classList.add("a_sang3");
});

button4.addEventListener("click", function() {
    locomotora.style.display = "block";
    locomotora.classList.add("a_locomotora");
    cowboy.style.display = "block";
    cowboy.classList.add("a_cowboy4");
    sang.classList.add("a_sang4");
});

button9.addEventListener("click", function() {
    fletxa1.style.display = "block";
    fletxa1.classList.add("a_fletxa1");
    fletxa2.style.display = "block";
    fletxa2.classList.add("a_fletxa2");
    fletxa3.style.display = "block";
    fletxa3.classList.add("a_fletxa3");
    fletxa4.style.display = "block";
    fletxa4.classList.add("a_fletxa4");
    fletxa5.style.display = "block";
    fletxa5.classList.add("a_fletxa5");
    fletxa6.style.display = "block";
    fletxa6.classList.add("a_fletxa6");
    body.classList.add("a_body");
});