# meteogrammer
Gets meteogram from yr, and stylizes it with imagemagick. End goal is to hang the picture like a live updated painting.

Hopefully with some form of e-ink display.
probably with a piZero

The command:

<pre><code>feh --reload 10 --fullscreen meteogram.png
</code></pre>

Will auto reload the image every 10 seconds.. which is probably a totally overkill interval..

From a non x environment i would use:
<pre><code>
fbi -T 2 -d /dev/fb1 -noverbose -t 300 /home/pi/meteogrammer/*.png -cachemem 0
</code></pre>
(found in showMeteogram.sh)

(Even though you ask fbi nicely to not cache anything, it still will, unless the slideshow consists of at least 3 images. 
This is worked around by creating 2 symlinks to the meteogram.png as detailed by [Jamie Jackson here](http://blog.jacobean.net/?p=941))

It would be the responsibility of the user to update the meteogram image periodically by running the meteogram.sh command in an appropriate location.
Here's a crontab that runs it every 15 minutes:
<pre><code>
*/15 * * * * /home/pi/meteogrammer/refreshMeteogram.sh > /home/pi/meteogrammer/cron.log
</code></pre>
