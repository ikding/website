PyVista tutorial: Red Spiders Cometh
####################################

:date: 2020-04-19
:tags: data_science
:slug: pyvista-red-spiders-cometh
:authors: I-Kang Ding
:summary: Short version for index and feeds


PyVista is a Python package for 3D plotting and mesh analysis through a streamlined interface for the Visualization Toolkit (VTK). I learned how to use the package in the past few weeks, and decided to build something fun for me, to explore Python-based 3D visualization on the web. Moreover, I had so much fun learning how to use the package, I decided to write up the process as a tutorial. Hope you found it helpful!


What should I build?
--------------------

As a engineering / programming nerd, I have always been a big fan of `XKCD comics <https://xkcd.com>`_. (In fact, I've been known to possess an uncanny set of esoteric knowledge about XKCD comic references, and I often put a healthy dosage of xkcd comics in my `Conference talks <{filename}./2020-01-08_building_python_community_among_analysts.rst>`_... but that's a topic for another post!) So, when I was thinking of 2D scenes that I want to render, I immediately think of XKCD's `red spiders <https://www.explainxkcd.com/wiki/index.php/Category:Red_Spiders>`_.

Red spiders appear in at least 7 different XKCD comics, although not many recently. After looking through the xkcd spider comic, I landed on the `Red Spiders Cometh <https://xkcd.com/126/>`_ scene.

.. image:: https://imgs.xkcd.com/comics/red_spiders_cometh.jpg
    :align: center
    :alt: xkcd-red-spiders-cometh
    :width: 600 px


Installing ``PyVista``
----------------------

PyVista has an excellent collection of documentation. Following through the `Installation instructions <https://docs.pyvista.org/getting-started/installation.html#>`_, I was able to ``pip install`` into my conda environment:

.. code-block:: bash

   pip install pyvista


Hello spider (our solider)
--------------------------

In this tutorial, we'll stick with the stock spider model that is available in PyVista examples. (Side note: XKCD spider actually should only have six leges, but I am not good enough with editing 3D models to remove legs, so the stock spider will have to do for now.)

We can easily make our spider come to life in 3D using just a few lines of code:

.. code-block:: python

    # hello_spider.py
    import pyvista as pv
    from pyvista import examples


    if __name__ == "__main__":
        pv.set_plot_theme("document")
        plotter = pv.Plotter()
        spider = examples.download_spider()

        plotter.add_mesh(spider, color="red")  # spider
        plotter.show()

Our arachnid foot soldier:

.. image:: https://user-images.githubusercontent.com/7269845/79674503-d753a880-81b1-11ea-8d78-30839de1775a.png
    :align: center
    :alt: spider
    :width: 500 px


Hello spider on a box (our assault unit)
----------------------------------------

In the xkcd comic, our spider foot solder doesn't just float around in free space. We need to give it a transport - a box! Fortunately, PyVista provides a easy (you may even say "out-of-box") way to plot a box. Now let's put our spider on its own box. We had to do some scaling, rotation, and translation to make our soldier land on its own transport with all eight legs. Also, we took care to make sure that the center of our box is the origin, which will make our later task of multiplying our assault unit easier.

.. code-block:: python

    # hello_spider_on_box.py
    import pyvista as pv
    from pyvista import examples


    def get_unit_cell_box() -> pv.PolyData:
        """Return a box unit. The box has length 1 in all 3 dimensions, and is
        centered at the origin.

        Having the box centered at origin will make it easier for rotating the
        spider on a box.

        Returns:
            pv.PolyData: ``pv.Polydata`` containing the box unit.
        """
        default_box = pv.Box()
        default_box.points /= 2
        return default_box


    def get_unit_cell_spider() -> pv.PolyData:
        """Return a spider unit. The spider has legspan that is slightly smaller
        than the box face, and is in a position so it appears to be standing on the
        box unit.

        Having the spider unit standing on the box centered at origin will make it
        easier for rotating the spider on a box.

        Returns:
            pv.PolyData: ``pv.Polydata`` containing the spider unit.
        """
        default_spider = examples.download_spider()
        default_spider.points /= 6
        default_spider.translate([-0.5, -0.5, 0.4])
        default_spider.rotate_z(-110)
        return default_spider


    def main() -> pv.Plotter:
        """Main function for rendering the 3D scene for spider on a box.

        Args:
            None

        Returns:
            pv.Plotter: pyvista plotter for plotting the 3D scene.
        """
        plotter = pv.Plotter()
        spider = get_unit_cell_spider()
        box = get_unit_cell_box()

        plotter.add_mesh(spider, color="red")  # spider
        plotter.add_mesh(box, color="tan", show_edges=True)  # box

        return plotter


    if __name__ == "__main__":
        pv.set_plot_theme("document")
        p = main()
        p.show()


And now we have a assault unit! The solider stares with resolve into the distance.

.. image:: https://user-images.githubusercontent.com/7269845/79675534-67462200-81b3-11ea-86e9-fb9342005c5f.png
    :align: center
    :alt: spider-on-box
    :width: 500 px


Hello buildings
---------------

If you look at the original comic, you would notice that the spider army has a target of their invasion - namely, the numerous buildings at a distance. Unfortunately there were no "stock buildings" that I can find in pyvista examples, but PyVista does have the ability to read in a host of 3D file types, so I did a google search and found this `Buildings and Skyscrapers <https://sketchfab.com/3d-models/buildings-and-skyscrapers-b35a7a00d6414f93a3d380965dfd169b>`_ 3D model (``.obj`` file), created by `Angel V Mendez <https://sketchfab.com/Angel.V.Mendez>`_ on Sketchfab, and made available through creative commons licensing. I downloaded the ``.obj`` file and save them to disk, and I can simply use ``pyvista.read()`` function to read them.

.. code-block:: python

    """Get a simple building."""
    import os

    import pyvista as pv

    DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "data")


    def get_buildings() -> pv.PolyData:
        """Return a set of buildings, which was downloaded from sketchfab and saved
        in project file.

        Returns:
            pv.PolyData: ``pv.Polydata`` containing the buildings.
        """
        default_buildings = pv.read(
            os.path.join(
                DATA_DIR, "buildings-and-skyscrapers", "source", "buildings.obj"
            )
        )
        default_buildings.rotate_x(90)
        default_buildings.translate([-4, -4, 0])
        return default_buildings


    def main(color_buildings="lightgray") -> pv.Plotter:
        """Main function for rendering the 3D scene.

        Args:
            color_buildings (str, optional): color of the buildings. Defaults to
            "lightgray".

        Returns:
            pv.Plotter: pyvista plotter for plotting the 3D scene.
        """
        plotter = pv.Plotter()
        buildings = get_buildings()
        buildings.points *= 1
        buildings.translate([0, 0, -10])
        plotter.add_mesh(buildings, color=color_buildings, show_edges=True)

        return plotter


    if __name__ == "__main__":
        pv.set_plot_theme("document")
        p = main()
        p.show()


Our unsuspecting victim.

.. image:: https://user-images.githubusercontent.com/7269845/79676756-41228100-81b7-11ea-9e84-05f09750753f.png
    :align: center
    :alt: buildings
    :width: 500 px
