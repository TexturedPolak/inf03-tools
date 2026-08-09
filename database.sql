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
	PRIMARY KEY("id")
);

CREATE TABLE "przedmioty" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nazwa"	TEXT NOT NULL UNIQUE,
	"krotka_nazwa"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "arkusz-przedmiot" (
	"id_arkusza"	INTEGER NOT NULL,
	"id_przedmiotu"	INTEGER NOT NULL,
	FOREIGN KEY("id_arkusza") REFERENCES "arkusze"("id"),
	FOREIGN KEY("id_przedmiotu") REFERENCES "przedmioty"("id")
);

CREATE TABLE "config" (
	"id"	TEXT NOT NULL UNIQUE,
	"directory"	TEXT UNIQUE,
	PRIMARY KEY("id")
);

INSERT INTO "przedmioty" ("id", "nazwa", "krotka_nazwa") VALUES
(NULL, "Projektowanie stron internetowych", "PSI"),
(NULL, "Projektowanie aplikacji internetowych", "PAI"),
(NULL, "Tworzenie i administrowanie bazami danych", "TIABD"),
(NULL, "Dom", "DOM");

INSERT INTO "config" ("id") VALUES ("default");
