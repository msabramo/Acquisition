Changelog
=========

4.1 (2014-12-18)
----------------

- Bump dependency on ``ExtensionClass`` to match current release.

4.0.3 (2014-11-02)
------------------

- Skip readme.rst tests when tests are run outside a source checkout.

4.0.2 (2014-11-02)
------------------

- Include ``*.rst`` files in the release.

4.0.1 (2014-10-30)
------------------

- Tolerate Unicode attribute names (ASCII only).  LP #143358.

- Make module-level ``aq_acquire`` API respect the ``default`` parameter.
  LP #1387363.

- Don't raise an attribute error for ``__iter__`` if the fallback to
  ``__getitem__`` succeeds.  LP #1155760.


4.0 (2013-02-24)
----------------

- Added trove classifiers to project metadata.

4.0a1 (2011-12-13)
------------------

- Raise `RuntimeError: Recursion detected in acquisition wrapper` if an object
  with a `__parent__` pointer points to a wrapper that in turn points to the
  original object.

- Prevent wrappers to be created while accessing `__parent__` on types derived
  from Explicit or Implicit base classes.

2.13.8 (2011-06-11)
-------------------

- Fixed a segfault on 64bit platforms when providing the `explicit` argument to
  the aq_acquire method of an Acquisition wrapper. Thx to LP #675064 for the
  hint to the solution. The code passed an int instead of a pointer into a
  function.

2.13.7 (2011-03-02)
-------------------

- Fixed bug: When an object did not implement ``__unicode__``, calling
  ``unicode(wrapped)`` was calling ``__str__`` with an unwrapped ``self``.

2.13.6 (2011-02-19)
-------------------

- Add ``aq_explicit`` to ``IAcquisitionWrapper``.

- Fixed bug: ``unicode(wrapped)`` was not calling a ``__unicode__`` 
  method on wrapped objects.

2.13.5 (2010-09-29)
-------------------

- Fixed unit tests that failed on 64bit Python on Windows machines.

2.13.4 (2010-08-31)
-------------------

- LP 623665: Fixed typo in Acquisition.h.

2.13.3 (2010-04-19)
-------------------

- Use the doctest module from the standard library and no longer depend on
  zope.testing.

2.13.2 (2010-04-04)
-------------------

- Give both wrapper classes a ``__getnewargs__`` method, which causes the ZODB
  optimization to fail and create persistent references using the ``_p_oid``
  alone. This happens to be the persistent oid of the wrapped object. This lets
  these objects to be persisted correctly, even though they are passed to the
  ZODB in a wrapped state.

- Added failing tests for http://dev.plone.org/plone/ticket/10318. This shows
  an edge-case where AQ wrappers can be pickled using the specific combination
  of cPickle, pickle protocol one and a custom Pickler class with an
  ``inst_persistent_id`` hook. Unfortunately this is the exact combination used
  by ZODB3.

2.13.1 (2010-02-23)
-------------------

- Update to include ExtensionClass 2.13.0.

- Fix the ``tp_name`` of the ImplicitAcquisitionWrapper and
  ExplicitAcquisitionWrapper to match their Python visible names and thus have
  a correct ``__name__``.

- Expand the ``tp_name`` of our extension types to hold the fully qualified
  name. This ensures classes have their ``__module__`` set correctly.

2.13.0 (2010-02-14)
-------------------

- Added support for method cache in Acquisition. Patch contributed by
  Yoshinori K. Okuji. See https://bugs.launchpad.net/zope2/+bug/486182.

2.12.4 (2009-10-29)
-------------------

- Fix iteration proxying to pass `self` acquisition-wrapped into both
  `__iter__` as well as `__getitem__` (this fixes
  https://bugs.launchpad.net/zope2/+bug/360761).

- Add tests for the __getslice__ proxying, including open-ended slicing.

2.12.3 (2009-08-08)
-------------------

- More 64-bit fixes in Py_BuildValue calls.

- More 64-bit issues fixed: Use correct integer size for slice operations.

2.12.2 (2009-08-02)
-------------------

- Fixed 64-bit compatibility issues for Python 2.5.x / 2.6.x.  See 
  http://www.python.org/dev/peps/pep-0353/ for details.

2.12.1 (2009-04-15)
-------------------

- Update for iteration proxying: The proxy for `__iter__` must not rely on the
  object to have an `__iter__` itself, but also support fall-back iteration via
  `__getitem__` (this fixes https://bugs.launchpad.net/zope2/+bug/360761).

2.12 (2009-01-25)
-----------------

- Release as separate package.
