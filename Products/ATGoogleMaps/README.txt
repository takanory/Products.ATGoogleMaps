Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

    >>> browser.open(portal_url)

We have the login portlet, so let's use that.

    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.

We then test that we are still on the portal front page:

    >>> browser.url == portal_url
    True

And we ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True


-*- extra stuff goes here -*-
The GMarker content type
===============================

In this section we are tesing the GMarker content type by performing
basic operations like adding, updadating and deleting GMarker content
items.

Adding a new GMarker content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'GMarker' and click the 'Add' button to get to the add form.

    >>> browser.getControl('GMarker').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'GMarker' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'GMarker Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'GMarker' content item to the portal.

Updating an existing GMarker content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New GMarker Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New GMarker Sample' in browser.contents
    True

Removing a/an GMarker content item
--------------------------------

If we go to the home page, we can see a tab with the 'New GMarker
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New GMarker Sample' in browser.contents
    True

Now we are going to delete the 'New GMarker Sample' object. First we
go to the contents tab and select the 'New GMarker Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New GMarker Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New GMarker
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New GMarker Sample' in browser.contents
    False

Adding a new GMarker content item as contributor
------------------------------------------------

Not only site managers are allowed to add GMarker content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'GMarker' and click the 'Add' button to get to the add form.

    >>> browser.getControl('GMarker').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'GMarker' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'GMarker Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new GMarker content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The GMap content type
===============================

In this section we are tesing the GMap content type by performing
basic operations like adding, updadating and deleting GMap content
items.

Adding a new GMap content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'GMap' and click the 'Add' button to get to the add form.

    >>> browser.getControl('GMap').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'GMap' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'GMap Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'GMap' content item to the portal.

Updating an existing GMap content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New GMap Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New GMap Sample' in browser.contents
    True

Removing a/an GMap content item
--------------------------------

If we go to the home page, we can see a tab with the 'New GMap
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New GMap Sample' in browser.contents
    True

Now we are going to delete the 'New GMap Sample' object. First we
go to the contents tab and select the 'New GMap Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New GMap Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New GMap
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New GMap Sample' in browser.contents
    False

Adding a new GMap content item as contributor
------------------------------------------------

Not only site managers are allowed to add GMap content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'GMap' and click the 'Add' button to get to the add form.

    >>> browser.getControl('GMap').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'GMap' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'GMap Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new GMap content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The A Google Map type content type
===============================

In this section we are tesing the A Google Map type content type by performing
basic operations like adding, updadating and deleting A Google Map type content
items.

Adding a new A Google Map type content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'A Google Map type' and click the 'Add' button to get to the add form.

    >>> browser.getControl('A Google Map type').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'A Google Map type' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'A Google Map type Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'A Google Map type' content item to the portal.

Updating an existing A Google Map type content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New A Google Map type Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New A Google Map type Sample' in browser.contents
    True

Removing a/an A Google Map type content item
--------------------------------

If we go to the home page, we can see a tab with the 'New A Google Map type
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New A Google Map type Sample' in browser.contents
    True

Now we are going to delete the 'New A Google Map type Sample' object. First we
go to the contents tab and select the 'New A Google Map type Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New A Google Map type Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New A Google Map type
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New A Google Map type Sample' in browser.contents
    False

Adding a new A Google Map type content item as contributor
------------------------------------------------

Not only site managers are allowed to add A Google Map type content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'A Google Map type' and click the 'Add' button to get to the add form.

    >>> browser.getControl('A Google Map type').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'A Google Map type' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'A Google Map type Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new A Google Map type content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)



