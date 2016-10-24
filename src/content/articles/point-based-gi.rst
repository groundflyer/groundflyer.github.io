========================
Point-based GI in Mantra
========================

:date: 2016-10-23
:modified: 2016-10-23
:category: Houdini
:tags: mantra, vex
:slug: point-based-gi
:lang: en
:status: published
:summary:
   This light shader I wrote few years ago just for fun, but it turned out a very useful thing.
   I'll briefly explain this shader in the article.

   .. image:: images/pbgi.jpg
      :width: 800px
      :height: 450px
      :align: center

.. image:: images/pbgi.jpg
      :width: 800px
      :height: 450px
      :align: center

This technique seems very similar to the former Renderman GI pipeline [@Christensen10], but here we use point clouds only for irradiance caching.

Light shader
============

The shader is based on two passes:

* bake pass:

  1. compute irradiance

  2. write the computed value

* beauty pass:

  1. read a few closest points

  2. filter its values

Light shader creation
	In main menu click File -> New Operator Type...
	Choose **Operator Style** - **VEX Type**, **Network Type** - **Light Shader Operator**,
	set name and label. Now in Type Properties window in tab ``Code`` we can wire code in `VEX light context`__.

__ http://www.sidefx.com/docs/houdini15.5/vex/contexts/light

The global illumination computed with `irradiance()`_ function and cached into a point cloud file using `pcwrite()`_.

.. code-block:: c
   :linenos: inline

   vector n = normalize(N);

   vector Cd = irradiance(Ps, n,
		"samples", samples,
		"environment", envmap,
		"envlight", space);

   vector wP = ptransform("space:world", Ps);
   vector wN = ntransform("space:world", n);

   if (!(getraylevel() + getglobalraylevel()))
	pcwrite(pcfile, "P", wP, "N", wN, "Cd", Cd);

Point position and normal should be transformed into the world space. It's obligatory, exception only if you use the same camera for both bake and beauty pass.

To avoid stray calls of `pcwrite()`_ we assure that the current shading point is on zero level.

Reading and filtering block:

.. code-block:: c

   int handle = pcopen(pcfile, "P", wP, radius, maxpoints, "preload", 1);
   Cl = pcfilter(handle, "Cd");
   pcclose(handle);

The ``maxpoints`` value is a sample count for filtering.

Final code:

[gist:id=5be8cf68d58838f7b9ce91164c7d41c4]

Scene setup
===========

Create Template Light and set parameter Light Shader to our light shader SHOP.

Create two Mantra ROPs: one for bake pass, second for beauty pass.

For bake pass create a new Take and add the **Mode** parameter on the light shader to the take, setting value to **Write** accordingly.
Then specify this take in the bake ROP.
Use only Micropoly render engine for baking: it generates regular point cloud grid.
Output Image is useless, so you can set it to ``/dev/null`` - on Linux, or ``NUL`` on Windows.

Beauty pass should work fine with any render engine.

The saved point cloud is available through File SOP.

.. vimeo:: 187550386
   :width: 800
   :height: 450
   :align: center

Optimization
============

Usually I disable hiding on the bake ROP. Resulting point clouds with Uniform Geometry Measuring are more regular. To increase/decrease point cloud density change Shading Quality Multiplier on the ROP or on objects.

To get deeper diffuse bounces shader must be more complicated. `getglobalraylevel()`_ and `renderstate()`_ functions should useful tom implement this feature.

The `pcfilter()`_ function implements weighted arithmetic mean with weights based on distance to a point. I prefer a custom filter routine which takes point normal into account:

.. math::

   C = \frac{\sum_{i=0}^N C_i}{\sum_{i=0}^N \left(\frac{\cos \theta_i}{r_i}\right)^2}

where :math:`C` - resulted value, :math:`N` - number of points, :math:`C_i` -  color value of :math:`i`th point, :math:`\theta_i` - angle between shading point and :math:`i`th point and :math:`r_i` - distance to the point.

It is possible to do all the calculations in a single pass only.
To implement this you need to generate point cloud at rendertime using `pcgenerate()`_, then iterate over points with `pcunshaded()`_ setting up position and normal using `sample_geometry()`_ and finally compute irradiance.
The filter step remains unchanged.
This light however will always produce flicker artifacts.

Method cons
===========

Comparing to modern path tracing this method is a vintage:

1. inflexibility
  
2. two passes
  
3. wasting io operations
  
4. potential flickering
  
5. only diffuse bounces
  
6. ignoring BSDF
  
7. complicated scene setup
  
8. one value per point: two-sided materials are not supported

.. _irradiance(): http://www.sidefx.com/docs/houdini15.5/vex/functions/irradiance
.. _pcwrite(): http://www.sidefx.com/docs/houdini15.5/vex/functions/pcwrite
.. _pcopen(): http://www.sidefx.com/docs/houdini15.5/vex/functions/pcopen
.. _pcfilter(): http://www.sidefx.com/docs/houdini15.5/vex/functions/pcfilter
.. _getglobalraylevel(): http://www.sidefx.com/docs/houdini15.5/vex/functions/getglobalraylevel
.. _renderstate(): http://www.sidefx.com/docs/houdini15.5/vex/functions/renderstate
.. _pcunshaded(): http://www.sidefx.com/docs/houdini15.5/vex/functions/pcunshaded
.. _sample_geometry(): http://www.sidefx.com/docs/houdini15.5/vex/functions/sample_geometry
.. _pcgenerate(): http://www.sidefx.com/docs/houdini15.5/vex/functions/pcgenerate
