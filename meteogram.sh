#!/bin/bash
curl http://www.yr.no/sted/Danmark/Midtjylland/aarhus/meteogram.png > meteogramRaw.png
#convert -colorspace Gray meteogramRaw.png -negate -shave 9x4 -chop 0x21 -sketch 1 meteogram.png
convert -colorspace Gray meteogramRaw.png -negate -shave 9x4 -chop 0x21 -sketch 2 meteogram.png
#rm meteogramRaw.png