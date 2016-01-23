==============================================================================
example.p4p5
==============================================================================

An example to show how to build a Plone add-on compliant for both Plone 4 and Plone 5.

Content
--------

It is a very simple add-on generated with `mr.bob <https://github.com/plone/bobtemplates.plone>`_.

It contains:

- a basic Dexterity type (named Task),
- a CSS and a JS (`chart.css` and `chart.js`),
- a view (`/@@all-charts`) which draw a ugly chart about the tasks and which involves `chart.css` and `chart.js`.

Profiles
--------

There are 3 Generic Setup installation profiles for installing:

- `base`, which contains the non version-specific setup (in our case, that's the Task content-type),
- `plone4`, which contains JS and CSS declaration for Plone 4, and depends on `base`,
- `plone5`, which contains JS and CSS declaration for Plone 5, and depends on `base`.

The `plone4` or `plone5` profile will automatically imported when we install the add-on depending on the portal's current version.

Similarly, for unistalling, there are 3 Generic Setup installation profiles (`uninstall-base`, `uninstall-plone4` and `uninstall-plone5`), and it works the same way.

CSS/JS declaration in Plone 5
-----------------------------

The Plone 5 approach regarding CSS and JS is based on the current front-end development practices.
So when we develop the front-end part of our add-on, we might create patterns, have a bunch of LESS files for theming, etc. (see `Mockup <https://mockup-training.readthedocs.org/en/latest/>`_ ), and at the end the all thing is compiled into one single JS and one single CSS, which are declared in a **bundle**.

In our case, we do not want to use the Plone 5 front-end stack because it would not apply to Plone 4, making the project less maintainable. So the trick is to declare our existing original `chart.css` and `chart.js` as a bundle directly (even if they are not the result of any compilation). Here is how we do it (in `registry.xml`):

.. code-block:: xml

    <records prefix="plone.bundles/examplep4p5"
        interface='Products.CMFPlone.interfaces.IBundleRegistry'>
        <value key="enabled">True</value>
        <value key="jscompilation">++resource++example.p4p5/chart.js</value>
        <value key="csscompilation">++resource++example.p4p5/chart.css</value>
        <value key="last_compilation">2016-01-01 00:00:00</value>
        <value key="compile">False</value>
        <value key="depends">plone</value>
    </records>

License
-------

The project is licensed under the GPLv2.
