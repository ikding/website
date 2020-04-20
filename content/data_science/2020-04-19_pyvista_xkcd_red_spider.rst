PyVista tutorial: Red Spiders Cometh
####################################

:date: 2020-04-19
:tags: data_science, misc
:slug: pyvista-red-spiders-cometh
:authors: I-Kang Ding


.. image:: https://user-images.githubusercontent.com/7269845/79694828-e897c600-8240-11ea-8d09-9681be469f46.gif
    :align: center
    :alt: red-spiders-cometh-gif-link
    :target: https://ikding.github.io/xkcd_red_spider_3d/
    :width: 500 px


PyVista is a Python package for 3D plotting and mesh analysis through a streamlined interface for the Visualization Toolkit (VTK). I learned how to use the package in the past few weeks, and decided to build something fun to explore Python-based 3D visualization on the web.

I had so much fun learning how to use the package, I decided to write up the process as a tutorial. Hope you found it helpful!


What should I build?
--------------------

As a engineering / programming nerd, I have always been a big fan of `XKCD comics <https://xkcd.com>`_. (In fact, I've been known to possess an uncanny set of esoteric knowledge about XKCD comic references, and I often put a healthy dosage of xkcd comics in my `conference talks <{filename}./2020-01-08_building_python_community_among_analysts.rst>`_... but that's a topic for another post!) So, when I was thinking of 2D scenes that I want to render, I immediately think of XKCD's `red spiders <https://www.explainxkcd.com/wiki/index.php/Category:Red_Spiders>`_.

.. image:: https://user-images.githubusercontent.com/7269845/79707786-9a5be480-828b-11ea-85ea-2e9b99982b5a.png
    :align: center
    :alt: xkcd-oh-god-spiders
    :width: 150 px

Red spiders appear in at least 7 different XKCD comics, although not many recently. After looking through the xkcd spider comic, I landed on the `Red Spiders Cometh <https://xkcd.com/126/>`__ scene. This post will walk through how we can turn this 2D scene:

.. image:: https://imgs.xkcd.com/comics/red_spiders_cometh.jpg
    :align: center
    :alt: xkcd-red-spiders-cometh-2d
    :width: 500 px

To a 3D scene that you can view and zoom `on the web <https://ikding.github.io/xkcd_red_spider_3d/>`_:

.. image:: https://user-images.githubusercontent.com/7269845/79694828-e897c600-8240-11ea-8d09-9681be469f46.gif
    :align: center
    :alt: red-spiders-cometh-gif-link
    :target: https://ikding.github.io/xkcd_red_spider_3d/
    :width: 500 px


Installing ``PyVista``
----------------------

PyVista has an excellent collection of documentation. Following through the `Installation instructions <https://docs.pyvista.org/getting-started/installation.html#>`_, I was able to ``pip install`` into my conda environment:

.. code-block:: bash

   pip install pyvista


Hello spider (our arachnid solider)
-----------------------------------

In this tutorial, we'll stick with the stock spider model that is available in PyVista examples.

(Side note: XKCD spider actually should only have six legs, but I am not good enough with editing 3D models to remove legs, so the stock spider will have to do for now.)

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

Say hi to our spider soldier:

.. image:: https://user-images.githubusercontent.com/7269845/79674503-d753a880-81b1-11ea-8d78-30839de1775a.png
    :align: center
    :alt: spider
    :width: 500 px


Hello spider on a box (our assault unit)
----------------------------------------

In the xkcd comic, our spider foot solder doesn't just float around in free space. We need to give it a transport - a box! Fortunately, PyVista provides an easy way to plot a box, *right out-of-the-box*.

Now let's put our spider on its own box. We had to do some scaling, rotation, and translation to make our soldier land on its own transport with all eight legs. Also, we took care to make sure that the center of our box is at the origin, which will make our task later of multiplying our assault unit easier.

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


And now we have a assault unit! *Our solider stares, with resolve, into the distance.*

.. image:: https://user-images.githubusercontent.com/7269845/79675534-67462200-81b3-11ea-86e9-fb9342005c5f.png
    :align: center
    :alt: spider-on-box
    :width: 500 px


Hello buildings
---------------

If you look at the `original comic <https://xkcd.com/126/>`_, you would notice that the spider army has a target of their invasion - namely, the numerous buildings at a distance. Unfortunately there were no "stock buildings" that I can find in PyVista examples, but PyVista does have the ability to read a variety of 3D file types, so I did a google search and found this `Buildings and Skyscrapers <https://sketchfab.com/3d-models/buildings-and-skyscrapers-b35a7a00d6414f93a3d380965dfd169b>`_ 3D model (``.obj`` file), created by `Angel V Mendez <https://sketchfab.com/Angel.V.Mendez>`_ on Sketchfab, and made available through creative commons licensing. I downloaded the ``.obj`` file and save them to disk, and I can simply use ``pyvista.read()`` function to read them.

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


The spiders, they are multiplying
---------------------------------

You cannot hope to conquer a small-sized city with a single giant spider alone. We'll need a lot more. Fortunately, we can easily multiply our spider-on-a-box assault unit through code. We can also rotate and translate the assault units to make each spider solider occupy different faces of the box. We can even scale the size of our assault unit through a simple multiplication / division!

This is where placing our unit spider-box assault unit in the origin (coordinate ``(0, 0, 0)``) is helpful. The `rotate_x <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_x>`_, `rotate_y <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_y>`_, and `rotate_z <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_z>`_ methods in ``pv.PolyData`` will rotate the meshes with respect to x, y, or z axis (right-handed coordinate). Placing our assault unit at the origin will allow us to rotate our assault unit as many times we want, and the spider will be able to cling snugly with the box. After we are happy with the rotational placement, we can call `translate <https://docs.pyvista.org/core/common.html#pyvista.Common.translate>`_ method to spread out our assault units to other locations.


.. code-block:: python

    """Main script to kick off a pyvista 3D visualization window.

    To run::
        python xkcd_red_spider/hello_spider_army.py
    """
    from typing import List, Tuple, Union

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


    def process_spider_box_unit_cell(
        spider: pv.PolyData = get_unit_cell_spider(),
        box: pv.PolyData = get_unit_cell_box(),
        scale: float = 1.0,
        rotation: List[Tuple[str, float]] = None,
        translation: List[Union[int, float]] = None,
    ) -> Tuple[pv.PolyData, pv.PolyData]:
        """Process the spider-box unit cell through operations including scaling,
        rotations, and translations.

        Args:
            spider (pv.PolyData, optional): Polydata containing the spider unit.
                Defaults to get_unit_cell_spider().
            box (pv.PolyData, optional): Polydata containing the box unit. Defaults
                to get_unit_cell_box().
            scale (float, optional): scaling factor. Defaults to 1.0.
            rotation (List[Tuple[str, float]], optional): list of steps for
                rotation, in the form of list of tuples, and the tuple containing
                the direction (``"x"``, ``"y"``, or ``"z"``) in the first element,
                and the degrees in the second direction. Example:
                ``[("x", 90), ("z", 180)]``. Under the hood, the
                `rotate_x <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_x>`_,
                `rotate_y <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_y>`_, and
                `rotate_z <https://docs.pyvista.org/core/common.html#pyvista.Common.rotate_z>`_
                methods in ``pv.PolyData`` are called. Defaults to None.
            translation (List[Union[int, float]], optional): Length of 3 list or
                array to translate the polydata. Under the hood, the
                `translate <https://docs.pyvista.org/core/common.html#pyvista.Common.translate>`_
                method in ``pv.PolyData`` is called. Defaults to None.

        Returns:
            Tuple[pv.PolyData, pv.PolyData]: A tuple of ``pv.Polydata`` containing the spider and box.
        """
        spider.points *= scale
        box.points *= scale

        if isinstance(rotation, list):
            for step in rotation:
                if step[0] == "x":
                    spider.rotate_x(step[1])
                if step[0] == "y":
                    spider.rotate_y(step[1])
                if step[0] == "z":
                    spider.rotate_z(step[1])

        if isinstance(translation, list):
            spider.translate(translation)
            box.translate(translation)

        return (spider, box)


    def main() -> pv.Plotter:
        """Main function for rendering the 3D scene for spider on a box.

        Args:
            None

        Returns:
            pv.Plotter: pyvista plotter for plotting the 3D scene.
        """
        plotter = pv.Plotter()
        spider_1, box_1 = process_spider_box_unit_cell(
            spider=get_unit_cell_spider(), box=get_unit_cell_box(), scale=1.0
        )
        spider_2, box_2 = process_spider_box_unit_cell(
            spider=get_unit_cell_spider(),
            box=get_unit_cell_box(),
            scale=1.2,
            rotation=[("y", 90)],
            translation=[2, 0, 0],
        )
        spider_3, box_3 = process_spider_box_unit_cell(
            spider=get_unit_cell_spider(),
            box=get_unit_cell_box(),
            scale=1.4,
            rotation=[("x", 90)],
            translation=[4, 0, 0],
        )
        spider_4, box_4 = process_spider_box_unit_cell(
            spider=get_unit_cell_spider(),
            box=get_unit_cell_box(),
            scale=1.6,
            rotation=[("z", 90)],
            translation=[6, 0, 0],
        )

        plotter.add_mesh(spider_1, color="red")
        plotter.add_mesh(spider_2, color="red")
        plotter.add_mesh(spider_3, color="red")
        plotter.add_mesh(spider_4, color="red")

        plotter.add_mesh(box_1, color="tan")
        plotter.add_mesh(box_2, color="tan")
        plotter.add_mesh(box_3, color="tan")
        plotter.add_mesh(box_4, color="tan")

        return plotter


    if __name__ == "__main__":
        pv.set_plot_theme("document")
        p = main()
        p.show()


Here is our mathematically-generated, 4-unit spider assault squad.

.. image:: https://user-images.githubusercontent.com/7269845/79691762-50451580-822f-11ea-9c40-0c6555549e92.png
    :align: center
    :alt: spider-assult-squad
    :width: 500 px


Commencing assault
------------------

Now we have everything we need to put together our 3D scene for "Red spiders cometh". What I did then was to manually label the coordinates of the assault unit in the original 2D scene, and translate them into coordinates that my Python program can understand. I also reproduced the rotational steps to make them into the right orientation.

.. image:: https://user-images.githubusercontent.com/7269845/79692776-fc3d2f80-8234-11ea-8be1-4f227eef0b0a.jpeg
    :align: center
    :alt: red-spiders-cometh-coord-label
    :width: 600 px

.. code-block:: python

    from typing import Dict, List, Tuple

    # Hand-crafted spider army coords that mimic the xkcd comic: Red Spiders Cometh
    # https://xkcd.com/126/
    XKCD_SPIDER_ARMY_COORD = {
        (1, 0): None,
        (0, 3): [("z", -90), ("y", 180)],
        (-1, -2): [("z", 0), ("y", 180)],
        (3, -2): [("z", 0), ("y", 180)],
        (5, 2): [("z", 180), ("y", -90)],
        (6, -1): [("z", 90)],
        (8, 1): None,
        (10, -1): [("y", -90)],
        (-2, 2): [("z", -90)],
        (-4, 2): [("y", 90)],
        (-6, -1): [("y", 180)],
        (-8, 2): [("x", -90)],
        (-8, -2): [("y", 90)],
        (-10, -3): None,
    }

    def get_xkcd_spider_army(
        spider_army_coord: Dict[Tuple[int, int], List[Tuple[str, int]]] = None,
        extra_spider: bool = True,
    ) -> List[Tuple[pv.PolyData, pv.PolyData]]:
        """Generate the xkcd spider army through the army coordinates.

        Args:
            spider_army_coord (Dict[Tuple[int, int], List[Tuple[str, int]]], optional): Coordinates
                and rotation steps of the red spider army. Check XKCD_SPIDER_ARMY_COORD for the
                example setting. Defaults to None.
            extra_spider (bool, optional): whether or not to add extra spiders on two boxes, to
                improve fidelity with the original comic. Defaults to True.

        Returns:
            List[Tuple[pv.PolyData, pv.PolyData]]: list of (spider, box) ``pv.PolyData`` tuples.
        """
        if spider_army_coord is None:
            spider_army_coord = XKCD_SPIDER_ARMY_COORD

        spider_army = []
        for spider_unit_coord, spider_unit_rotation in spider_army_coord.items():
            spider_army.append(
                process_spider_box_unit_cell(
                    spider=get_unit_cell_spider(),
                    box=get_unit_cell_box(),
                    rotation=spider_unit_rotation,
                    translation=list(spider_unit_coord) + [0],
                )
            )

        # Add two extra spiders for fidelity with xkcd comic
        if extra_spider and (spider_army_coord == XKCD_SPIDER_ARMY_COORD):
            spider_army += [
                process_spider_box_unit_cell(
                    spider=get_unit_cell_spider(),
                    box=get_unit_cell_box(),
                    rotation=[("x", 90)],
                    translation=[-1, -2, 0],
                ),
                process_spider_box_unit_cell(
                    spider=get_unit_cell_spider(),
                    box=get_unit_cell_box(),
                    rotation=[("z", 180)],
                    translation=[-4, 2, 0],
                ),
            ]

        return spider_army

And now, you can see the re-created scene of "Red Spiders Cometh" in 3D!

.. image:: https://user-images.githubusercontent.com/7269845/79693265-a0c07100-8237-11ea-92e8-eeecc00e7bcc.png
    :align: center
    :alt: red-spiders-cometh-static
    :width: 500 px


Commemorate our conquest on the web
-----------------------------------

So far, we've been rendering the 3D scene with PyVista on the local machine. One cool thing about PyVista is: you can easily export your scene, and use `vtkjs <https://kitware.github.io/vtk-js/index.html>`_ to allow our scene of conquest to be rendered in a website.

All it takes is one line of `export_vtkjs <https://docs.pyvista.org/plotting/plotting.html#pyvista.BasePlotter.export_vtkjs>`_ code to export our scene to ``.vtkjs``:

.. code-block:: python

    vtkjs_file_path = os.path.join(DATA_DIR, "red_spiders_cometh")
    p.export_vtkjs(vtkjs_file_path)

Then, we'll be able to render the scene from within a browser! (I borrowed the code from another repo, `dennissergeev/exoconvection-apj-2020 <https://github.com/dennissergeev/exoconvection-apj-2020>`_)

So now, here I present to you, `Red Spiders Cometh <https://ikding.github.io/xkcd_red_spider_3d/>`__, now in 3D! (Clicking the gif will bring you to the website that you can play with yourself.

.. image:: https://user-images.githubusercontent.com/7269845/79694828-e897c600-8240-11ea-8d09-9681be469f46.gif
    :align: center
    :alt: red-spiders-cometh-gif-link
    :target: https://ikding.github.io/xkcd_red_spider_3d/
    :width: 500 px


Last words
----------

I have really enjoy my experience using PyVista so far. The library has a really extensive documentation and use cases, and I have had numerous cases where I was fiddling with things to see if they work in PyVista, and it turned out to work in my first try, which is always a pleasant surprise when you are playing with a new tool.

All the code examples (along with a more modularized code base) can be found in this repo: `ikding/xkcd_red_spider_3d <https://github.com/ikding/xkcd_red_spider_3d>`_. Enjoy!

P.S. in case anyone is interested, here are all six XKCD comics in which the red spider was referenced:

* `8: Red Spiders <https://xkcd.com/8/>`_
* `43: Red Spiders 2 <https://xkcd.com/43/>`_
* `47: Counter-Red Spiders <https://xkcd.com/47/>`_
* `126: Red Spiders Cometh <https://xkcd.com/126/>`_
* `427: Bad Timing <https://xkcd.com/427/>`_
* `442: xkcd Loves the Discovery Channel <https://xkcd.com/442/>`_
