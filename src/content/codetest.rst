================================
Various test of Restuctured Text
================================

:date: 2016-10-19
:modified: 2016-10-19
:category: TestCategory
:tags: testtag, code, math, cite, gist
:slug: testingrst
:lang: en

It's a test article, it have to be removed

Code
----
Python Code
___________

.. code-block:: python

   for i in range(10)
	print('Suck {}'.format(i))

C-Code with numbers
___________________

.. code-block:: c
   :linenos: table

   #include <stdio.h>

   int main()
   {
      printf("Hello, thing\n");
		
      return 0;
   }

Math
----

Displayed math
______________

.. math::
   F(\eta,k,\cos \theta) = \frac{(\eta-1)^2 + 4\eta(1-\cos \theta)^5 + k^2}{(\eta+1)^2+k^2}

Inline math
___________

Bla, bla bla :math:`a = \text{lerp}(2\eta, 0, \min(\cos\theta, 0.15))`, bibl [@Knaus:2011:PPM:1966394.1966404]

Gist test
---------

[gist:id=c362f0ad488e3b289394,file=keras_prediction.py]

Here must be bibliography

