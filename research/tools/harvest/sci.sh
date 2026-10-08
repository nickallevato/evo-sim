cd /home/na/projects/evo-sim/sources/raw/day/tags
for p in 2 3 4 5 6 7 8; do code=$(curl -sL -A 'Mozilla/5.0' -w "%{http_code}" https://voxday.net/tag/science/page/$p/ -o science-$p.html); echo "science $p $code"; sleep 1; done
for p in 2 3; do code=$(curl -sL -A 'Mozilla/5.0' -w "%{http_code}" https://voxday.net/tag/mittens/page/$p/ -o mittens-$p.html); echo "mittens $p $code"; sleep 1; done
