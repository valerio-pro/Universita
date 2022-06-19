"use strict";

const title = document.getElementsByTagName("h1")[0];
const main = document.getElementsByTagName("main")[0];
let data;

// Ottenere tutti gli stili calcolati sull'elemento "main"
const mainStyle = getComputedStyle(main);

// Altezza del viewport -> window.innerHeight
// Larghezza del viewport -> window.innerWidth
const viewportHeight = window.innerHeight;

// Al caricamento della finestra viene fatto il fetch dei dati contenuti nel file "data.json"
addEventListener("load", async () => {

    let response = await fetch("./data.json");
    data = await response.json();

    data.forEach( (el) => {
        console.log(el);
    });

});


// Al click del titolo vengono aggiunti nel main dei div quadrati usando i dati presenti nel file "data.json"
title.addEventListener("click", () => {

    main.style.position = "relative";

    const mainWidth = parseInt(mainStyle.width);
    const mainHeight = parseInt(mainStyle.height);

    data.forEach( (el) => {

        let div = document.createElement("div");
        div.style.backgroundColor = el.colore;
        div.style.position = "absolute";

        div.style.top = `${(el.pos_vert/100) * mainHeight}px`;
        div.style.left = `${(el.pos_orizz/100) * mainWidth}px`;

        div.style.width = `${viewportHeight/10}px`;
        div.style.height = `${viewportHeight/10}px`;

	// Rimozione dei div al loro click
        div.addEventListener("click", (event) => {
            event.target.remove();
        });

        main.append(div);

    });

});

