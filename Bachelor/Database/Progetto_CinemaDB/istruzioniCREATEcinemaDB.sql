CREATE TABLE Categoria (codice_categoria CHAR(1) NOT NULL,
			descrizione VARCHAR(32) NOT NULL,
			PRIMARY KEY(codice_categoria)) ENGINE=InnoDB;

CREATE TABLE Tipo (codice_tipo CHAR(1) NOT NULL,
		   descrizione VARCHAR(16) NOT NULL,
		   PRIMARY KEY(codice_tipo)) ENGINE=InnoDB;

CREATE TABLE Genere (codice_genere VARCHAR(3) NOT NULL,
		     descrizione VARCHAR(16) NOT NULL,
		     PRIMARY KEY(codice_genere)) ENGINE=InnoDB;

CREATE TABLE Agenzia (nome_agenzia VARCHAR(32) NOT NULL,
		      citta VARCHAR(24),
		      indirizzo VARCHAR(32),
                      numero_telefono CHAR(10) NOT NULL,
		      PRIMARY KEY(nome_agenzia)) ENGINE=InnoDB;


CREATE TABLE Studio_Cinematografico (nome_studio VARCHAR(24) NOT NULL,
				     citta VARCHAR(24),
				     indirizzo VARCHAR(32),
				     quota_di_mercato DECIMAL(3,2),
				     PRIMARY KEY(nome_studio)) ENGINE=InnoDB;



CREATE TABLE Artista (id INT UNSIGNED NOT NULL AUTO_INCREMENT,
		     nome VARCHAR(16) NOT NULL,
	  	     cognome VARCHAR(16) NOT NULL,
		     data_nascita DATE,
		     agenzia VARCHAR(32) NOT NULL,
		     FOREIGN KEY(agenzia) REFERENCES Agenzia(nome_agenzia) ON UPDATE CASCADE ON DELETE NO ACTION,
		     PRIMARY KEY(id)) ENGINE = InnoDB;


CREATE TABLE Regista (id INT UNSIGNED NOT NULL,
		      FOREIGN KEY(id) REFERENCES Artista(id) ON UPDATE CASCADE ON DELETE NO ACTION,
		      numero_film_indipendenti TINYINT UNSIGNED NOT NULL,
		      PRIMARY KEY(id)) ENGINE = InnoDB;


CREATE TABLE Attore (id INT UNSIGNED NOT NULL,
		     FOREIGN KEY(id) REFERENCES Artista(id) ON UPDATE CASCADE ON DELETE NO ACTION,
		     esordio YEAR NOT NULL,
		     categoria CHAR(1) NOT NULL,
		     FOREIGN KEY(categoria) REFERENCES Categoria(codice_categoria) ON UPDATE CASCADE ON DELETE NO ACTION,
		     PRIMARY KEY(id)) ENGINE = InnoDB;

CREATE TABLE Film (titolo VARCHAR(32) NOT NULL,
		   data_uscita DATE NOT NULL,	
		   durata TINYINT UNSIGNED NOT NULL,
		   incasso INT UNSIGNED NOT NULL,
		   studio VARCHAR(24) NOT NULL,
		   FOREIGN KEY(studio) REFERENCES Studio_Cinematografico(nome_studio) ON UPDATE CASCADE ON DELETE NO ACTION,
 		   id_regista INT UNSIGNED NOT NULL,
		   FOREIGN KEY(id_regista) REFERENCES Regista(id) ON UPDATE CASCADE ON DELETE NO ACTION,
		   tipo CHAR(1) NOT NULL,
		   FOREIGN KEY(tipo) REFERENCES Tipo(codice_tipo) ON UPDATE CASCADE ON DELETE NO ACTION,
		   formato CHAR(2) NOT NULL,		   
		   PRIMARY KEY(titolo)) ENGINE = InnoDB;		   

CREATE TABLE Cinema (nome_cinema VARCHAR(24) NOT NULL,
		     citta VARCHAR(24),
		     indirizzo VARCHAR(32),
		     numero_sale TINYINT NOT NULL,
		     prezzo_biglietto DECIMAL(4,2),
		     PRIMARY KEY(nome_cinema)) ENGINE=InnoDB;


CREATE TABLE Azienda (nome_azienda VARCHAR(32) NOT NULL,
		      anno_fondazione YEAR NOT NULL,
		      net_worth BIGINT UNSIGNED NOT NULL,
		      PRIMARY KEY(nome_azienda)) ENGINE=InnoDB;



CREATE TABLE Generi_Film (titolo VARCHAR(32) NOT NULL,
			  codice_genere VARCHAR(3) NOT NULL,
			  FOREIGN KEY(titolo) REFERENCES Film(titolo) ON UPDATE CASCADE ON DELETE CASCADE,
			  FOREIGN KEY(codice_genere) REFERENCES Genere(codice_genere) ON UPDATE CASCADE ON DELETE CASCADE,
			  PRIMARY KEY(titolo, codice_genere)) ENGINE = InnoDB;

CREATE TABLE Distribuzione (nome_studio VARCHAR(24) NOT NULL,
			    nome_cinema VARCHAR(24) NOT NULL,
			    FOREIGN KEY(nome_studio) REFERENCES Studio_Cinematografico(nome_studio) ON UPDATE CASCADE ON DELETE CASCADE,
			    FOREIGN KEY(nome_cinema) REFERENCES Cinema(nome_cinema) ON UPDATE CASCADE ON DELETE CASCADE,
			    PRIMARY KEY(nome_studio, nome_cinema)) ENGINE=InnoDB;

CREATE TABLE Recita (titolo VARCHAR(32) NOT NULL,
		     id INT UNSIGNED NOT NULL,
		     compenso INT UNSIGNED NOT NULL,
		     ruolo VARCHAR(16) NOT NULL,
		     FOREIGN KEY(titolo) REFERENCES Film(titolo) ON UPDATE CASCADE ON DELETE CASCADE,
		     FOREIGN KEY(id) REFERENCES Attore(id) ON UPDATE CASCADE ON DELETE CASCADE,
		     PRIMARY KEY(titolo, id)) ENGINE = InnoDB;


CREATE TABLE Contratto_Azienda (titolo VARCHAR(32) NOT NULL,
			        nome_azienda VARCHAR(32) NOT NULL,
				valore_contratto INT UNSIGNED NOT NULL,
				FOREIGN KEY(titolo) REFERENCES Film(titolo) ON UPDATE CASCADE ON DELETE CASCADE,
			        FOREIGN KEY(nome_azienda) REFERENCES Azienda(nome_azienda) ON UPDATE CASCADE ON DELETE CASCADE,
				PRIMARY KEY(titolo, nome_azienda)) ENGINE=InnoDB;
