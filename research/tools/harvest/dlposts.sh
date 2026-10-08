#!/bin/bash
# usage: dlposts.sh listfile (lines: url)
while read -r u; do
  d=$(echo "$u" | sed -E 's#https://voxday.net/([0-9]{4})/([0-9]{2})/([0-9]{2})/.*#\1-\2-\3#')
  s=$(echo "$u" | sed -E 's#https://voxday.net/[0-9]{4}/[0-9]{2}/[0-9]{2}/([^/]*)/?#\1#' | cut -c1-60)
  f="blog/blog-$d-$s.html"
  [ -s "$f" ] && continue
  curl -sL -A 'Mozilla/5.0' "$u" -o "$f" || echo FAIL $u
  sleep 1
done < "$1"
