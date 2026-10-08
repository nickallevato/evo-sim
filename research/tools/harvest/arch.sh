cd /home/na/projects/evo-sim/sources/raw/day/tags/arch
for m in 06 07 08 09; do for p in $(seq 1 30); do u="https://voxday.net/2026/$m/page/$p/"; [ $p = 1 ] && u="https://voxday.net/2026/$m/"; code=$(curl -sL -A 'Mozilla/5.0' -w "%{http_code}" "$u" -o a-$m-$p.html); echo "$m $p $code"; [ "$code" != 200 ] && rm -f a-$m-$p.html && break; sleep 1; done; done
