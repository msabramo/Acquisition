##############################################################################
#
# Copyright (c) 1996-2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
import Acquisition

def checkContext(self, o):
    # Python equivalent to aq_inContextOf
    from Acquisition import aq_base, aq_parent, aq_inner
    subob = self
    o = aq_base(o)
    while 1:
        if aq_base(subob) is o:
            return True
        self = aq_inner(subob)
        if self is None: break
        subob = aq_parent(self)
        if subob is None: break
    return False

class B(Acquisition.Implicit):
    color='red'

    def __init__(self, name='b'):
        self.name = name

    def _aq_dynamic(self, attr):
        if attr == 'bonjour': return None

        def dynmethod():
            chain = ' <- '.join(repr(obj) for obj in Acquisition.aq_chain(self))
            print repr(self) + '.' + attr
            print 'chain:', chain

        return dynmethod

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.name)

class A(Acquisition.Implicit):

    def __init__(self, name='a'):
        self.name = name

    def hi(self):
        print self, self.color

    def _aq_dynamic(self, attr):
        return None

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.name)

def test_dynamic():
    r'''
    The _aq_dynamic functionality allows an object to dynamically provide an
    attribute.
    
    If an object doesn't have an attribute, Acquisition checks to see if the
    object has a _aq_dynamic method, which is then called. It is functionally
    equivalent to __getattr__, but _aq_dynamic is called with 'self' as the
    acquisition wrapped object where as __getattr__ is called with self as the
    unwrapped object.

    Let's see how this works. In the examples below, the A class defines
    '_aq_dynamic', but returns 'None' for all attempts, which means that no new
    attributes should be generated dynamically. It also doesn't define 'color'
    attribute, even though it uses it in the 'hi' method.

        >>> A().hi()
        Traceback (most recent call last):
        ...
        AttributeError: color
    
    The class B, on the other hand, generates all attributes dynamically,
    except if it is called 'bonjour'.
    
    First we need to check that, even if an object provides '_aq_dynamic',
    "regular" Aquisition attribute access should still work:

        >>> b=B()
        >>> b.a=A()
        >>> b.a.hi()
        A('a') red
        >>> b.a.color='green'
        >>> b.a.hi()
        A('a') green

    Now, let's see some dynamically generated action. B does not define a
    'salut' method, but remember that it dynamically generates a method for
    every attribute access:

        >>> b.a.salut()
        B('b').salut
        chain: B('b')

        >>> a=A('a1')
        >>> a.b=B('b1')
        >>> a.b.salut()
        B('b1').salut
        chain: B('b1') <- A('a1')

        >>> b.a.bonjour()
        Traceback (most recent call last):
        ...
        AttributeError: bonjour

        >>> a.b.bonjour()
        Traceback (most recent call last):
        ...
        AttributeError: bonjour

    '''

def test_wrapper_comparissons():
    r'''

    Test wrapper comparisons in presence of _aq_dynamic

        >>> b=B()
        >>> b.a=A()
        >>> foo = b.a
        >>> bar = b.a
        >>> assert( foo == bar )
        >>> c = A('c')
        >>> b.c = c
        >>> b.c.d = c
        >>> b.c.d == c
        True
        >>> b.c.d == b.c
        True
        >>> b.c == c
        True

    Test contextuality in presence of _aq_dynamic

        >>> checkContext(b.c, b)
        True
        >>> checkContext(b.c, b.a)
        False

        >>> assert b.a.aq_inContextOf(b)
        >>> assert b.c.aq_inContextOf(b)
        >>> assert b.c.d.aq_inContextOf(b)
        >>> assert b.c.d.aq_inContextOf(c)
        >>> assert b.c.d.aq_inContextOf(b.c)
        >>> assert not b.c.aq_inContextOf(foo)
        >>> assert not b.c.aq_inContextOf(b.a)
        >>> assert not b.a.aq_inContextOf('somestring')
'''
