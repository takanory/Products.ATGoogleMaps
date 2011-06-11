.. contents::

Introduction
============
This product provides maps, marker and polyline content for Plone from Archetypes.

See example maps at http://takanory.net/plone/develop/atgooglemaps/sample/.

Dependencies
============
- Plone: Plone 3.3+

Installation
============
buildout
--------
- Just add Products.ATGoogleMaps to the eggs section of your buildout configuration and run buildout.::

    eggs =
        ..
        Products.ATGoogleMaps

- Restart Zope.
- Go to the Site Setup page in the Plone interface and click on the Add/Remove Products link. Choose ATGoogleMaps (check its checkbox) and click the Install button.

Licence
=======
Distributed under the GPL v2.

See LICENSE.txt and LICENSE.GPL for details.
