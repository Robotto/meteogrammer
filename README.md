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
fbi
</code></pre>
in some sort of slideshow mode so it would update the image every -t seconds ...

It would be the responsibility of the user to update the meteogram image periodically by running the meteogram.sh command in an appropriate location.

Here's a crontab that runs it every 15 minutes:
<pre><code>
*/15 * * * * /home/pi/meteogrammer/meteogram.sh > /home/pi/meteogrammer/cron.log
</code></pre>
