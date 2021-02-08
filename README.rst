Guide for setting up a fractopo environment on notebooks.csc.fi
===============================================================

Requires University of Turku or GTK credentials. Usage is not officially
supported by CSC.

Setup
-----

1. Go to notebooks.csc.fi and log in with University of Turku
   credentials or GTK-credentials.

   -  *Haka Login* -> *University of Turku* -> *Select*
   -  *Virtu* -> *Government Identification Service* -> *Select*

2. Click on Launch new below ``Course Practical Deep Learning - 2020``
   or ``Geo-Python Lite`` heading. This will start a new temporary
   Python notebook environment (Prefer ``Geo-Python Lite`` if
   available). The initialization will take some seconds.
3. Click on ``Open in browser`` after the link has popped up under
   Access column.
4. ``Geo-Python Lite`` environment requires a password input stage but
   if no password prompt is visible when opened you can skip 5. and 6.
5. Copy the password presented and proceed (proceeding will also
   automatically copy the password to clipboard.)
6. Input the password in the upper right corner prompt and proceed.

You will now be presented with a Jupyter Lab Python environment. This
environment is temporary. Default lifetime is 5-10 hours. After
leaving/time runs out all data in the environment will be destroyed.
Therefore setup must always be performed and results should be
downloaded to your local storage.

6. Click on the + icon in the top left corner.

7. Under Other, click on Terminal.

8. We will now install the ``fractopo`` Python package to the
   environment. Copy the following text exactly to the opened terminal
   prompt and press Enter:

   .. code:: bash

      pip install git+https://github.com/nialov/fractopo#egg=fractopo

   -  The installation will take some time.

9. After installation is finished, congratulations, you may now use
   ``fractopo`` to validate and analyze trace map data.

Uploading data to the environment
---------------------------------

Next-up you probably want to upload some data to the environment for
validation and analysis.

1. Click on the up-arrow symbol in the top left corner. You may hover
   over the symbols to find the right one (``Upload Files``).
2. You can now select files to upload. You cannot directly upload
   directories (You can make new directories directly in the environment
   by clicking on the folder+ symbol.)
3. Trace validation and analysis both require a file with traces and a
   file with a target area.

Trace validation
----------------

Trace validation doesn't require interaction within the notebook and can
instead be done from the terminal, the same window we used to install
``fractopo``.

1. If you don't have the terminal open, open a new one (click on +
   symbol -> ``Terminal``). You can clear a terminal of outputs by
   typing ``clear`` and pressing enter.

2. To make sure the command is installed and working, paste the
   following to the terminal and press enter:

   .. code:: bash

      tracevalidate --help

   -  If the command works you will see a brief description of the
      ``tracevalidate`` tool.
   -  If the command throws an error, try closing the terminal and
      opening a new terminal and trying again. If it still does not
      work, repeat the Setup process from earlier.

3. The ``tracevalidate`` tool requires passing the trace and area data
   in the following way:

   .. code:: bash

      tracevalidate TRACEDATA AREADATA

   -  Additionally the tool should be supplied with a few options:

   .. code:: bash

      tracevalidate TRACEDATA AREADATA --snap-threshold 0.01 --fix --summary

   -  ``--snap-threshold`` represents the snapping threshold the data
      has been digitized with in meters (depends on coordinate system)
      i.e. ``0.01`` equals to 1 cm. For drone orthophotography data in
      ETRS-TM35FIN coordinate system values between 0.01 and 0.001 are
      usually fine. You may/should experiment if your data differs in
      source and coordinate system.
   -  ``--fix`` Allows automatic fixing of e.g. multi-geometry
      collection transformation to single geometries when the collection
      only actually consists of the single geometry. Highly recommended
      but will slightly alter the geometry data that is passed.
   -  ``--summary`` will post a small summary of validation results in
      the terminal after finishing.

4. To summarize, paste the following code to the terminal and replace
   ``TRACEDATA`` and ``AREADATA`` with paths to your data files, e.g.:

   .. code:: bash

      tracevalidate traces.gpkg target_area.gpkg --snap-threshold 0.01 --fix --summary

   -  If your files are in a folder, prefix the path with the folder
      name e.g.:

   .. code:: bash

      tracevalidate MYFOLDER/traces.gpkg MYFOLDER/target_area.gpkg --snap-threshold 0.01 --fix --summary

   -  You can *tab-complete* file paths on the terminal window by
      pressing **Tab** with a partial or empty filename. E.g. if your
      traces are in a file named *traces.gpkg* you can type *tr* and
      press tab to autocomplete the filename. If there are colliding
      filenames e.g., *traces_2.gpkg* in the same directory the
      completion will only occur until the common path between the
      files.
   -  Press Enter to run the command (as usual).

5. The tool will create a new folder in the same folder as the trace
   data with the validated data when finished.

   -  Folder name is ``validated_DAY_MONTH_YEAR_HOUR_MIN``.
   -  You should look at the summary data printed on the terminal screen
      after the tool has finished to determine if and how the data is
      invalid.

6. Fixing validated data should be done on your GIS-software of choice.

7. Data can be downloaded from the environment by right-clicking on
   files/folders in the file explorer on the left and selecting
   ``Download``.

   -  The validated traces data contains a new column with the
      validation errors. After fixing the data, re-upload it to the same
      (or new environment) and try validation again.
   -  See
      https://fractopo.readthedocs.io/en/latest/validation/errors.html
      for explanations of validation errors.
   -  ``SHARP TURNS`` errors are not major and do not have to be fixed
      but other errors are typically destructive in further analysis and
      the data may error in the analysis section.

8. If the trace data passed validation, you may go to the analysis
   section.

Trace network analysis
----------------------

Trace network analysis happens in the notebook environment. I've
prepared a template notebook that you can simply fill with your trace
and area data paths and some analysis will be performed by then just
simply running the notebook without further edits.

First we must download the template notebook repository with ``git``.

1. Open a new terminal and paste in the following text:

   .. code:: bash

      git clone https://github.com/nialov/fractopo-help.git --depth 1

   -  This will clone a repository from the address specified to the
      environment.
   -  The repository will be in a ``fractopo-help`` directory.

2. If you do not see the file browser at the left of the screen, open it
   with the folder symbol at the very left of the screen.

3. Navigate to the ``fractopo-help`` directory by double-clicking.

   -  You can press the small folder icon to return to base working
      directory if you've navigated to some other folder already.

4. Copy the ``network.ipynb`` to your working folder.

   -  Right click file to Copy.
   -  Right click in directory to Paste.

5. Double-click on the ``network.ipynb`` notebook file in your working
   folder.

6. Navigate to the ``Data`` section.

   -  The cell with:

   .. code:: python

      trace_data = ""
      area_data = ""
      name = ""

   -  Is the starting section for analysis. Follow the guidance within
      the notebook itself to complete the network analysis.

Final notes
-----------

The environment is **temporary**. Download all results when you are
finished.
