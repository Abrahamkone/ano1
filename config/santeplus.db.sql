BEGIN TRANSACTION;
DROP TABLE IF EXISTS "consultation";
CREATE TABLE IF NOT EXISTS "consultation" (
	"id_consultation"	INTEGER,
	"date_consul"	TEXT,
	"heure"	TEXT,
	"service"	TEXT,
	"id_patient"	TEXT,
	"allergie"	TEXT,
	"temperature"	NUMERIC,
	"observation"	TEXT,
	"symptome"	TEXT,
	"nom_med"	TEXT,
	PRIMARY KEY("id_consultation"),
	FOREIGN KEY("id_patient") REFERENCES "patient"("id_patient") ON UPDATE NO ACTION
);
DROP TABLE IF EXISTS "patient";
CREATE TABLE IF NOT EXISTS "patient" (
	"id_patient"	TEXT NOT NULL,
	"nom"	TEXT,
	"prenom"	TEXT,
	"sexe"	TEXT,
	"dateNaiss"	TEXT,
	"cni"	TEXT,
	"profession"	TEXT,
	"tel"	REAL,
	"email"	TEXT,
	"assurance"	TEXT,
	"lien_photo"	TEXT DEFAULT 'photo',
	PRIMARY KEY("id_patient")
);
DROP TABLE IF EXISTS "rdv";
CREATE TABLE IF NOT EXISTS "rdv" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"id_patient"	TEXT,
	"date_consul"	TEXT,
	"heure_consul"	TEXT,
	"nom_med"	TEXT,
	"service"	TEXT,
	"date_rdv"	TEXT,
	FOREIGN KEY("id_patient") REFERENCES "patient"("id_patient") ON UPDATE NO ACTION
);
DROP TABLE IF EXISTS "connexion";
CREATE TABLE IF NOT EXISTS "connexion" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"pseudo"	TEXT,
	"password"	TEXT
);
DROP TABLE IF EXISTS "ordonnance";
CREATE TABLE IF NOT EXISTS "ordonnance" (
	"id_ord"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"medicaments"	TEXT,
	"date"	TEXT,
	"id_med"	INTEGER,
	"id_patient"	TEXT,
	FOREIGN KEY("id_med") REFERENCES "medecin"("id_med") ON UPDATE NO ACTION,
	FOREIGN KEY("id_patient") REFERENCES "patient"("id_patient") ON UPDATE NO ACTION
);
DROP TABLE IF EXISTS "medecin";
CREATE TABLE IF NOT EXISTS "medecin" (
	"id_med"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nom"	TEXT,
	"prenom"	TEXT,
	"specialité"	TEXT
);
INSERT INTO "consultation" ("id_consultation","date_consul","heure","service","id_patient","allergie","temperature","observation","symptome","nom_med") VALUES (1,'2020-04-15','03:37:30.340819','','AN99','',45,'ljgljgjgljqc','qxcqx',''),
 (2,'2020-04-15','03:38:12.972425','','AN99','',33,'vvvhhv,h,v','wxcwxc',''),
 (3,'2020-04-15','13:05:51.277761','URGENCE','KI896','PIQURES',37.2,'MGJMJDFGDFG','SDFSLLK','DR JOSUE'),
 (4,'2020-04-15','16:45:24.578102','GYNECOLOGIE','KI896','CHLOROQUINE',45,'sdqdqds','RAS','DR IBRAHIM');
INSERT INTO "patient" ("id_patient","nom","prenom","sexe","dateNaiss","cni","profession","tel","email","assurance","lien_photo") VALUES ('AN99','gael','sedrick','HOMME','12/12/1996','CNI789','python',757755.0,'mail','assufar','dsfsdfsdfsdf'),
 ('DA454','dsdf','aze','FEMME','14/04/2020','azeaze77','azeae',45454.0,'zerzer','assurace','c://zerzerzerzer'),
 ('KI896','kone','ibrahim','HOMME','14/04/2020','AN45DD','programmeur',89652312.0,'kone@gmail.com','mugefci','c://zerzerzerzer'),
 ('VG','vddd','gfddd','','14/04/2020','','','','','','c://zerzerzerzer');
INSERT INTO "connexion" ("id","pseudo","password") VALUES (28,'admin','santeplus');
INSERT INTO "ordonnance" ("id_ord","medicaments","date","id_med","id_patient") VALUES (1,'zerc','2020-04-15',2,'KI896'),
 (2,'zerzer','2020-04-15',3,'KI896');
INSERT INTO "medecin" ("id_med","nom","prenom","specialité") VALUES (1,'DR JOSUE','JONATHAN','PEDIATRE'),
 (2,'DR GAËL','SEDRICK','OPHTALMOLOGUE'),
 (3,'DR IBRAHIM','ZIE','GYNECOLOGUE'),
 (4,'DR SILVA','PATRICK','URGENTISTE');
COMMIT;
