
url=$1

if [ $# -eq 0 ]; then
 url="https://hackaday.com/blog/feed/"
fi


curl -s $url | grep --color=none '<title>'
