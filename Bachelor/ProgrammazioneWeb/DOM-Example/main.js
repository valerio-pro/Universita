"use strict";

const menuList = document.getElementById("menu-list");
const menuBtn = document.getElementById("menu-btn");
const closeBtn = document.getElementById("close-btn");
const divOverlay = document.getElementById("div-overlay");
let data;

// <node>.parentNode (nodo padre)
// <node>.nextElementSibling (nodo fratello successivo)
// <event>.target (nodo su cui e' definito l'evento) -> l'oggetto <event> e' preso in input dalle callback degli eventi

// <node>.classList.add("<css-class-name>")
// <node>.classList.remove("<css-class-name>")
// <node>.classList.toggle("<css-class-name>") -> aggiunge la classe se non e' presente, rimuove la classe se e' presente

// <node>.setAttribute("<attribute-name>", "<value>")
// <node>.innerHTML = "<string-of-text>"

// Se il nodo DOM e' un elemento HTML "<input ...>" di un Form, allora con <node>.value si accede al valore assegnato all'elemento "<input ...>"
// Se si definisce una callback per un evento "submit" su un Form, allora con <event>.preventDefault() si evita il ricarimento della pagina
// quando e' premuto il bottone di "submit"


// Le callback degli eventi hanno in input l'oggetto "event" -> event.target e' il nodo DOM sul quale si sta definendo l'evento
addEventListener("load", async (event) => {

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


menuBtn.addEventListener("click", (event) => {

    if (window.innerWidth < 600) {

        menuList.classList.toggle("hidden");

    }

});

closeBtn.addEventListener("click", (event) => {

    divOverlay.classList.add("hidden");

});
