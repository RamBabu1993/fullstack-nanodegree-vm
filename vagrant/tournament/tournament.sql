-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- drop database if exist in project
   drop database if exists tournament;
   
-- create database tournament
   
   create database tournament;

   \c tournament;

   create table players(id serial primary key, name text);

-- create table matches

   create table matches(id serial primary key, 
   	                    winner_id int references players(id),
   	                    loser_id int references players(id));

-- create view for winners record of matches

   create view winners_record 
   as select players.id, count(matches.winner_id)
   from players left join matches
   group by players.id;

-- create view for losers record of matches

   create view losers_record 
   as select players.id, count(matches.loser_id)
   from players left join matches
   group by players.id;

-- create view to record wins, losses and total matches played by a players

   create view players_matches_record 
   as select *
   from winners_record natural join losers_record;
   
   


