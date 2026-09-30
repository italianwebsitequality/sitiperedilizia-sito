#!/bin/bash
# PNG di Codex (_src/foto/<cartella>/<nome>.png) -> webp ottimizzati in img/
cd "$(dirname "$0")/.." || exit 1
for f in _src/foto/*/*.png; do
  [ -f "$f" ] || continue
  d=$(basename "$(dirname "$f")"); n=$(basename "$f" .png)
  if [ "$d" = home ]; then o="$n"; else o="d-$d-$n"; fi
  cwebp -quiet -q 78 -resize 1600 0 "$f" -o "img/$o-L.webp"
  cwebp -quiet -q 72 -resize 800 0 "$f" -o "img/$o-S.webp"
done
# card portfolio (4:5 ritagliate via CSS: basta larghezza 900) e prima/dopo
c(){ [ -f "$1" ] && cwebp -quiet -q 74 -resize 900 0 "$1" -o "img/c-$2.webp"; }
c _src/foto/serramenti/hero.png serramenti; c _src/foto/tetti/hero.png tetti
c _src/foto/impianti/hero.png impianti; c _src/foto/imbiancatura/hero.png imbiancatura
[ -f img/d-edilizia-sopralluogo-L.webp ] && cp img/d-edilizia-sopralluogo-L.webp img/c-rossi-fontana.webp
cp img/d-edilizia-prima-L.webp img/prima-L.webp; cp img/d-edilizia-dopo-L.webp img/dopo-L.webp
