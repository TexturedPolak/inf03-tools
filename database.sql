CREATE TABLE "arkusze" (
	"id"	TEXT NOT NULL UNIQUE,
	"sciezka"	TEXT NOT NULL UNIQUE,
	"status"	TEXT NOT NULL DEFAULT 'nierozpoczete',
	"plik_arkusz"	TEXT NOT NULL,
	"plik_ocenianie"	TEXT,
	"plik_archiwum"	TEXT,
	"rok" INTEGER NOT NULL,
	"sesja" INTEGER NOT NULL,
	"numer" INTEGER NOT NULL,
	"port"	INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("id")
);

CREATE TABLE "przedmioty" (
	"id"	TEXT NOT NULL UNIQUE,
	"nazwa"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id")
);

CREATE TABLE "arkusz-przedmiot" (
	"id_arkusza"	TEXT NOT NULL,
	"id_przedmiotu"	TEXT NOT NULL,
	FOREIGN KEY("id_arkusza") REFERENCES "arkusze"("id"),
	FOREIGN KEY("id_przedmiotu") REFERENCES "przedmioty"("id")
);

CREATE TABLE "config" (
	"id"	TEXT NOT NULL UNIQUE,
	"directory"	TEXT UNIQUE,
	"last"	TEXT,
	PRIMARY KEY("id")
);

INSERT INTO "przedmioty" ("id", "nazwa") VALUES
("PSI", "Projektowanie stron internetowych"),
("PAI", "Projektowanie aplikacji internetowych"),
("TIABD", "Tworzenie i administrowanie bazami danych"),
("DOM", "Dom");

INSERT INTO "config" ("id") VALUES ("default");
