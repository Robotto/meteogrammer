#!/bin/bash
homedir=~
eval homedir=$homedir
cd $homedir/meteogrammer
curl --silent http://www.yr.no/sted/Danmark/Midtjylland/aarhus/avansert_meteogram.png > meteogramRaw.png
#convert -colorspace Gray meteogramRaw.png -shave 9x4 -chop 0x35 -gravity East -chop 408x0 -resize 480x320\!  -fill yellow -tint 100 -negate meteogram.png
convert meteogramRaw.png -shave 9x8 -chop 0x35 -gravity East -chop 408x0 -resize 480x320\! meteogram.png
rm meteogramRaw.png
echo "Done at $(date)"
