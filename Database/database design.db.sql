BEGIN TRANSACTION;
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"favourites"	NUMERIC,
	"admin"	INTEGER NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "preferences";
CREATE TABLE IF NOT EXISTS "preferences" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"number_of_bedrooms"	INTEGER NOT NULL,
	"university"	TEXT NOT NULL,
	"max_price"	INTEGER NOT NULL,
	"min_price"	INTEGER NOT NULL,
	"allergies"	INTEGER NOT NULL,
	"residential"	INTEGER NOT NULL
);
DROP TABLE IF EXISTS "housing_prices_dataset";
CREATE TABLE IF NOT EXISTS "housing_prices_dataset" (
	"borough_ID"	INTEGER NOT NULL,
	"borough"	TEXT NOT NULL,
	"room"	INTEGER NOT NULL,
	"studio"	INTEGER NOT NULL,
	"1_bedroom"	INTEGER NOT NULL,
	"2_bedrooms"	INTEGER NOT NULL,
	"3_bedrooms"	INTEGER NOT NULL,
	"4+_bedrooms"	INTEGER NOT NULL,
	PRIMARY KEY("borough_ID")
);
DROP TABLE IF EXISTS "borough";
CREATE TABLE IF NOT EXISTS "borough" (
	"borough_ID"	INTEGER NOT NULL,
	"borough_name"	TEXT NOT NULL,
	PRIMARY KEY("borough_ID")
);
DROP TABLE IF EXISTS "datasets";
CREATE TABLE IF NOT EXISTS "datasets" (
	"dataset_ID"	INTEGER NOT NULL UNIQUE,
	"dataset_name"	TEXT NOT NULL,
	PRIMARY KEY("dataset_ID")
);
DROP TABLE IF EXISTS "crime_rate";
CREATE TABLE IF NOT EXISTS "crime_rate" (
	"borough_ID"	INTEGER NOT NULL UNIQUE,
	"crime_rate"	NUMERIC NOT NULL,
	PRIMARY KEY("borough_ID")
);
DROP TABLE IF EXISTS "population_density";
CREATE TABLE IF NOT EXISTS "population_density" (
	"borough_ID"	INTEGER NOT NULL UNIQUE,
	"population_density"	NUMERIC NOT NULL,
	PRIMARY KEY("borough_ID")
);
DROP TABLE IF EXISTS "transport_links";
CREATE TABLE IF NOT EXISTS "transport_links" (
	"borough_ID"	INTEGER NOT NULL UNIQUE,
	"transport_links"	NUMERIC NOT NULL,
	PRIMARY KEY("borough_ID")
);
DROP TABLE IF EXISTS "greenspace";
CREATE TABLE IF NOT EXISTS "greenspace" (
	"borough_ID"	INTEGER NOT NULL UNIQUE,
	"greenspace"	NUMERIC NOT NULL,
	PRIMARY KEY("borough_ID")
);
DROP TABLE IF EXISTS "pollution";
CREATE TABLE IF NOT EXISTS "pollution" (
	"borough_ID"	INTEGER NOT NULL UNIQUE,
	"pollution_levels"	NUMERIC,
	PRIMARY KEY("borough_ID")
);
DROP TABLE IF EXISTS "favourites";
CREATE TABLE IF NOT EXISTS "favourites" (
	"ID"	INTEGER NOT NULL,
	"rankings"	TEXT,
	PRIMARY KEY("ID")
);
COMMIT;
