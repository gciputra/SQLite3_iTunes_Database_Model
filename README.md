# SQLite3 ITunes Database Model
 Why this iTunes Database model? Imagine wanting to export your favorite iTunes tracks as a well-organized SQL table and infuriatingly having to maninpulate the endless elements of an XML file. This project utilizes strategies in relational databases to convert iTune's XML export into meaningful and well-defined relational tables which immensely eases data query and filtration with software programs. 

 
### View the database model [here](https://imgur.com/MMO62Z1) 

## Sample Data
The sample data can be found in this folder: [Training Data in XML](https://file.io/pCrmGj6gm0OD)

## How the code works:
1. The code asks for a write access to a database file from SQLite3 and imports methods from the SQLite 3 Library.
2. The program checks first whether there are existing tables with the titles: Artist, Genre, Album, Track. If those 4 tables exist, then the program asks SQLite 3 to erase all the data and create 4 new tables with the same titles to prevent syntax error. Each table is defined with specific column headers and their schema (nature). 
3. An input from the user for an existing path to the XML iTunes File is processed and the XML is parsed to allow iteration and string methods.
4. A function is defined to lookup each line in the XML which contains data about a single music track and checks first if a Track ID is present for that particular track. If it is present, then the program is allowed to receive subsequent data ranging from the track name up until its length. This is a precaution to prevent syntax errors for an improper track data.
5. The program updates each table according to values stored from accessing the XML file and creates connections between the tables.
6. The 3 individual tables are combined based on matching foreign keys to present an overall data for each music track as an SQL Table "Tracks".
Note: Visit the program file to read more in-depth comments for sections of code.  

### For Future Use:
As this programming structure assumes a sample data, for future users wanting to convert their library exports into this data base model: Visit the -`Future_Use` file. 
Note: iTunes XML formats might be updated from time to time which prevents the program from working properly.


