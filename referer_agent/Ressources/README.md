/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c

Des commentaires dans le code source expliquent que la 1ere etape consiste a arriver sur cette page depuis le site "https://www.nsa.gov/"
On utilise l'option -e OU --referer pour simuler cette action
La deuxieme etape consiste a "utiliser" le browser "ft_bornToSec"
On utilise l'option -A pour cette action
Ce qui donne : curl -e https://www.nsa.gov/ -A ft_bornToSec "http://192.1.1.3/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c"
Get the flag
