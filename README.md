# CompetenceProject

### GitHub contains

- project (competence_project)
- documentation (docs)
- generated data (data_csv)

### How to use our program
1. Start MySQL server (login: root, password: admin)
2. Open competence_project in PyCharm.
3. Press "Run" button.
4. And follow instructions (should appear in console).
5. Enjoy:)

### Information about data sets
**User has 3 sets to choose**
- small _(0.1MB, 20 hotspots, 5 person, 1883 traces)_
- medium _(1MB, 200 hotspots, 50 person, 20 088 traces)_
- large _(11.5MB, 2000 hotspots, 500 person, 202 817 traces)_

**People profiles**

student, cook, seller, athlete, retired

**People interests**

football, cinemagoer, sport, bowling, shopping, books

**Hotspot descriptions**

cafe, bowlingPlace, restaurant, shop, park, library, parking, university, stadium, cinema

**Database schema**
````
create table if not exists CP_database.persons (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    phone_number int NOT NULL,
    profile varchar(99) NOT NULL,
    interests varchar(99) NOT NULL,
    PRIMARY KEY (id)) 
````
    
````
create table if not exists CP_database.hotspots (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name varchar(32) NOT NULL,
    description varchar(255),
    x double NOT NULL,
    y double NOT NULL,
    type enum('indoor', 'outdoor'),
    PRIMARY KEY (id))
````
    
```` 
create table if not exists CP_database.traces (
    id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id MEDIUMINT not null,
    FOREIGN KEY (user_id)
            REFERENCES persons(id)
            ON DELETE CASCADE,
    hotspot_id mediumint not null,   
    FOREIGN KEY (hotspot_id)
            REFERENCES hotspots(id)
            ON DELETE CASCADE,
    entry_time datetime,
    exit_time datetime)
````    

### Team Members

- Karol Lasek
- Radosław Grela
- Jakub Wąchała
- Marek Szafran
- Maciej Księżak
- Bartłomiej Grzelak
- Michał Włodarczyk
- Mateusz Mus

 
