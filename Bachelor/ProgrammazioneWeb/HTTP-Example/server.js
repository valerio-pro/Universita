const http = require("http");
const fs = require("fs");

// lettura sincrona/bloccante dei dati su file .json e conversione in oggetto JSON 
const data = JSON.parse(fs.readFileSync("./listaDellaSpesa.json", "utf-8"));

const port = 8080;
const host = "127.0.0.1";

const server = http.createServer( (req, res) => {

    // contiene il path presente dopo il numero di porta/hostname
    let path = req.url;

    const headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"  // permettere CORS da tutte le origini
    };

    if (path === "/data") {
        res.writeHead(200, headers);  // scrittura degli headers -> stato della risposta + headers
        res.write(JSON.stringify(data, null, 2));  
        res.end();  // chiusura dello stream di risposta, puo' prendere in input una stringa
    }
    else {
        res.writeHead(400, headers);
        res.write(JSON.stringify({status: "error", msg: "API not implemented"}, null, 2));
        res.end();
    }

});

// mettere il server in ascolto sulla porta "port" all'indirizzo "host"
server.listen(port, host);
