#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn=connect()
    cursor=conn.cursor()
    cursor.execute(" delete from matches")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn=connect()
    cursor=conn.cursor()
    cursor.execute(" delete from players")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("select count(id)from players")
    results=cursor.fetchone()[0]
    return results
    conn.close()


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn=connect()
    cursor=conn.cursor()
    cursor.execute(" insert into players(name) values (%s)", (name,))
    conn.commit()
    
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("select id, name, wins, (wins+losses) as matches \
                    from players natural join players_matches_record \
                    order by wins desc")              
    results=cursor.fetchall()
    return results
    conn.close()
    


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("insert into matches(winner_id, loser_id) values(%s, %s)", (winner, loser))
    conn.commit()
    
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """     
    
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("select a.id, a.name \
                   from (select id, name, wins \
                         from players natural join players_matches_record \
                         order by wins desc) as a")
    results=cursor.fetchall()
    p=len(results)
    b=[]
    
    for i in range(0,p,2):
        c=()
        c+=results[i]
        c+=results[i+1]
        b.append(c)
        
    return b
    conn.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
