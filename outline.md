## Course contents

This course will introduce the participants to 3D visualization using Mayavi
and VTK. Mayavi is an Open Source, Python package for general purpose 3D
visualization. Mayavi uses VTK (http://www.vtk.org) under the covers and
provides a very Python-friendly API. In particular, Mayavi provides the
following features:

- A full-blown application for visualization of data.
- A Python library for 3D visualization.
- Easy interoperability with NumPy.
- Widgets to embed 3D visualization in UI toolkits.

VTK is an extremely powerful visualization library. VTK contains more than
2000 classes that provides functionality for 3D graphics, visualization, and
image processing. It provides visualization algorithms for scalar, vector, and
tensor data. It is implemented in C++ and provides wrappers to several
languages including Python.

The course will first start with using `mayavi.mlab` to quickly produce
visualizations that are useful for scientists and engineers. VTK will then be
introduced and covered in a little detail. VTK datasets will be explored in
some detail. The commonly used VTK sources and filters will be explored. The
course will then look at Mayavi in greater detail and introduce the
participants to the traits package. Using this, participants could create
their own dialogs and widgets that embed Mayavi in them.

The course will be completely hands-on with plenty of exercises.

## Outline

We hope to broadly cover the following areas.

- Quick Introduction to Mayavi
   - History
   - Overview of features

- Using `mayavi.mlab` for visualization
   - Using the UI
   - Plotting simple data: lines and points
   - More complex data: surfaces, meshes, volumes
   - Scalar and vector visualization
   - Annotation
   - Saving results

- Animating the visualizations with `mayavi.mlab`
   - Automation
   - Using script recording

- The Mayavi pipeline
   - Introduction
   - An introduction to datasets and why they matter
   - Mayavi datasets and the Mayavi pipeline

- VTK datasets
   - Data and its representation
   - Creating VTK datasets
   - Creating datasets with Python
      - Image data
      - Structured grids
      - Polygonal data
      - Unstructured grids
   - Example: Creating grids from unstructured points

- The Mayavi application
   - Introduction to features
   - Using the command line arguments
   - Visualizing data files
   - Available modules
   - Available filters
   - Integration with `mlab` and scripting

- An introduction to VTK and TVTK
   - VTK features and history
   - VTK architecture
   - The VTK pipeline
   - TVTK

- Sources, filters, and modules by example

- Miscellaneous features
   - Using with IPython
   - Using with Jupyter notebooks
   - Generating ray-tracing output

## Required knowledge

- Familiarity with Python and numpy.
- Basic Object Oriented Programming with Python.
