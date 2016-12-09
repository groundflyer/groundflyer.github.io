========
Tinyfarm
========

:date: 2016-12-03
:modified: 2016-12-09
:category: Houdini
:tags: mantra, linux, bash
:slug: tinyfarm
:lang: en
:summary:
   Sometimes Houdini consumes too much RAM when sending a scene to render
   so Mantra goes to swap and slows down badly.
   
   In such cases it's better to generate IFD's and render them separately, when Houdini is closed and RAM is mostly free.

   I written this shell script to render multiple IFD files in convenient way.

   .. image:: images/tinyfarm.jpg
      :width: 800px
      :height: 450px
      :align: center

.. image:: images/tinyfarm.jpg
   :width: 800px
   :height: 450px
   :align: center

Just run this script in the directory containing IFD's to render them all.

To stop rendering simply Ctrl-C the process,
it will wait for the current render job to finish,
then it cleans up the IFD and exits.
If you have no time to wait,
do Ctrl-C again - this cancels the current job by killing Mantra process.

The script also prints out some useful info with Mantra-like timestamp:
the name of the file being rendered, finished render status,
elapsed and estimated time.

There are just a few optional parameters, run script with -h flag to see them:

* directory where to look for IFD files

* -k: do not remove an IFD after successful render

* -m: send additional options to mantra; see mantra -h

Example:

.. code-block:: sh

   tinyfarm.bash /path/to/cool/project -m -V 1a

starts rendering in `/path/to/cool/project` with level 1 rendering statistics and verbose Alfred-style progress reporting.

The directory you specified is not the only place where script is looking for IFDs, but in the **SUBPATH** too.
I usually save IFDs to `$HIP/render/ifds`.
Redefine the **SUBPATH** variable if you use other directory for IFDs.

The script itself:

[gist:id=35809025716bd91d37f9b431056db7c8]
