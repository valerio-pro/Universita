"use strict";

const btn = document.getElementById("convert-btn");
const main = document.getElementsByTagName("main")[0];

const pre = document.createElement("pre");
const ul = document.createElement("ul");

// Array globale di dati ottenuti dalla fetch
let data;
const url = "http://127.0.0.1:8080/data";


addEventListener("load", async () => {

    let resp = await fetch(url);
    
    // Salvataggio contenuto json in variabile globale
    data = await resp.json();

    // JSON.stringify(<array_of_json_objects>, null, 2) -> pretty print JSON
    pre.append(document.createTextNode(JSON.stringify(data, null, 2))); 
    
    main.insertBefore(pre, btn);

});

btn.addEventListener("click", () => {

    for(let i = 0; i < data.length; i++) {
        let li = document.createElement("li");
        li.append(document.createTextNode(JSON.stringify(data[i])));
        ul.append(li);
    }

    main.insertBefore(ul, btn);
    main.removeChild(pre);
    btn.remove();

});



