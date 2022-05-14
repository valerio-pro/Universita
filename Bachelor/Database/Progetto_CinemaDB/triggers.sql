
DELIMITER //

CREATE TRIGGER checkMovieType BEFORE INSERT ON film 
FOR EACH ROW

BEGIN 

	IF NEW.tipo = 'L' AND NEW.durata <= 30 THEN
		SET NEW.tipo = 'C';
	END IF;	

	IF NEW.tipo = 'C' AND new.durata > 30 THEN
		SET NEW.tipo = 'L';
	END IF;

END; //

DELIMITER ;




DELIMITER //

CREATE TRIGGER checkNumeroGeneri BEFORE INSERT ON generi_film
FOR EACH ROW

BEGIN 

	DECLARE currentNumber TINYINT;
	
	SELECT COUNT(*) AS numero INTO currentNumber
	FROM generi_film
	WHERE generi_film.titolo = NEW.titolo;

	IF currentNumber = 3 THEN 
		SIGNAL SQLSTATE '45000' 
		SET message_text = 'Inserimento non consentito, numero massimo di generi raggiunto';			
	END IF;
	
END; //

DELIMITER ;





