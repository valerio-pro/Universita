CREATE VIEW totaleProduzione(studio, totale_incassi) 
	AS SELECT studio, SUM(incasso)
	   FROM film
	   GROUP BY studio; 


CREATE VIEW partecipazioniAttori(nome, cognome, numeroPartecipazioni)
	AS SELECT nome, cognome, COUNT(*) 
	   FROM artista, attore, recita
	   WHERE artista.id = attore.id 
	   AND attore.id = recita.id
	   GROUP BY attore.id;
