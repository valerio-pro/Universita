"use strict";

const menuList = document.getElementById("menu-list");
const menuBtn = document.getElementById("menu-btn");
const closeBtn = document.getElementById("close-btn");
const divOverlay = document.getElementById("div-overlay");
let data;

// ESERCIZIO 2
addEventListener("load", async () => {

    let response = await fetch("./data.json");
    data = await response.json();

    data.forEach( (el) => {
        
        let li = document.createElement("li");
        let a = document.createElement("a");
        a.setAttribute("href", el.link);
        a.innerHTML = el.desc;

        li.append(a);
        menuList.append(li);

    });
    
});


// ESERCIZIO 5
menuBtn.addEventListener("click", () => {

    if (window.innerWidth < 600) {

        menuList.classList.toggle("hidden");

    }

});

// ESERCIZIO 7
closeBtn.addEventListener("click", () => {

    divOverlay.classList.add("hidden");

});