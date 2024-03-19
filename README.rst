Guide for setting up a fractopo environment on notebooks.csc.fi
================================================================

Requires *CSC*, *HAKA* or *Virtu* credentials for login.

Guide changes
-------------

2024-03-19
~~~~~~~~~~

``fractopo`` version locked to 0.6.0. Updated documentation to fit
changes of ``fractopo`` and ``notebooks.csc.fi``.

2022-02-02
~~~~~~~~~~

``fractopo`` version locked to 0.2.5. Fixed length distribution description
attribute call.

2022-01-13
~~~~~~~~~~

``fractopo`` version locked to 0.2.3. Added notebook for analysing trace data
when you do not want to determine topological properties of the trace network
due to e.g. topologically invalid data. The notebook allows trace length
distributions and azimuth rose plotting.

2021-09-22
~~~~~~~~~~

``fractopo`` version locked to 0.2.1 and ``tracevalidate`` is now a subcommand
of ``fractopo``. Look carefully at new example commands and run ``fractopo
--help`` and ``fractopo tracevalidate --help`` to see always up-to-date
available commands and help.

Setup
-----

1. Go to notebooks.csc.fi and log in with your credentials of choice.
   E.g.

   -  *Haka Login* -> *University of Turku* -> *Select*
   -  *Virtu* -> *Government Identification Service* -> *Select*

2. Click on the *Start session* button on the right side of the screen
   for the ``Jupyter Machine Learning`` or ``Geo-Python 2023``
   environment.
3. Wait for the environment to be created. The web page should
   automatically enter the ``Jupyter Lab`` environment.

   -  You will now be presented with a Jupyter Lab Python environment.
      This environment is temporary. Default lifetime is 4-8 hours
      depending on the environment. After leaving/time runs out all data
      in the environment will be destroyed with the exception of data in
      the ``my-work`` folder of the ``Geo-Python 2023`` environment.
      Therefore setup must always be performed and results should be
      downloaded to your local storage.

4. Click on the + icon in the top left corner.

5. Under Other, click on Terminal.

6. We will now install the ``fractopo`` Python package to the
   environment. Copy the following text exactly to the opened terminal
   prompt and press Enter:

   .. code:: bash

      pip install fractopo==0.6.0

   -  The installation will take some time.

7. After installation is finished, congratulations, you may now use
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

      fractopo tracevalidate --help

   -  If the command works you will see a brief description of the
      ``tracevalidate`` tool/subcommand.
   -  If the command throws an error, try closing the terminal and
      opening a new terminal and trying again. If it still does not
      work, repeat the Setup process from earlier.

3. The ``tracevalidate`` tool requires passing the trace and area data
   in the following way:

   .. code:: bash

      fractopo tracevalidate TRACE_FILE AREA_FILE

   -  Additionally the tool should be supplied with a few options:

   .. code:: bash

      fractopo tracevalidate TRACE_FILE AREA_FILE --snap-threshold 0.001

   -  ``--snap-threshold`` represents the snapping threshold the data
      has been digitized with in meters (depends on coordinate system)
      i.e. ``0.001`` equals to 1 mm. For drone orthophotography data in
      ETRS-TM35FIN coordinate system values between 0.01 and 0.001 are
      usually fine. You may/should experiment if your data differs in
      source and coordinate system.

4. To summarize, paste the following code to the terminal and replace
   ``TRACE_FILE`` and ``AREA_FILE`` with paths to your data files, e.g.:

   .. code:: bash

      fractopo tracevalidate traces.gpkg target_area.gpkg --snap-threshold 0.001

   -  If your files are in a folder, prefix the path with the folder
      name e.g.:

   .. code:: bash

      fractopo tracevalidate MYFOLDER/traces.gpkg MYFOLDER/target_area.gpkg --snap-threshold 0.001

   -  You can *tab-complete* file paths on the terminal window by
      pressing ``<Tab>`` with a partial or empty filename. E.g. if your
      traces are in a file named *traces.gpkg* you can type *tr* and
      press ``<Tab>`` to autocomplete the filename. If there are colliding
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

Trace network analysis  can either be done in a notebook or using
the command-line, similarly to trace validation.

Analysis using the command-line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

General instructions for using the command-line from the trace
validation section above apply also here for e.g. ``<Tab>`` completion.

1. If you don't have the terminal open, open a new one (click on +
   symbol -> ``Terminal``). You can clear a terminal of outputs by
   typing ``clear`` and pressing enter.

2. To make sure the command is installed and working, paste the
   following to the terminal and press enter:

   .. code:: bash

      fractopo network --help

3. The ``network`` tool requires passing the trace and area data
   in the following way:

   .. code:: bash

      fractopo network TRACE_FILE AREA_FILE

   -  Additionally the tool should be supplied with a few options:

   .. code:: bash

      fractopo network TRACE_FILE AREA_FILE --snap-threshold 0.001 --determine-branches-nodes --name NAME

   - ``--determine-branches-nodes`` enables determination of the
      topology including defining the branches and nodes of the trace
      data.

   -  ``--name NAME`` will be used to define the name used in e.g.
      figure titles.

   -  Use ``fractopo network --help`` to see full listing of options that
      can be used.

4. To summarize, paste the following code to the terminal and replace
   ``TRACE_FILE`` and ``AREA_FILE`` with paths to your data files
   and ``NAME`` with a name for your trace data. e.g.:

   .. code:: bash

      fractopo network traces.gpkg target_area.gpkg --snap-threshold 0.001 --determine-branches-nodes --name NAME

5. The tool will create a new folder in the current folder with
   the analysis results.

   -  Folder name is ``NAME_outputs``.

Analysis in a notebook
~~~~~~~~~~~~~~~~~~~~~~

I've prepared a template notebook that you can simply fill with your
trace and area data paths and some analysis will be performed by then
just simply running the notebook without further edits.

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

4. Copy the ``network.ipynb`` and ``network_no_topology.ipynb`` to your working
   folder.

   -  Right click file to Copy.
   -  Right click in directory to Paste.
   -  Note that after copying the notebooks, the paths to the default
      data (``KB11``) included in the ``fractopo-help`` repository are
      no longer valid and you **must** supply paths to your own data to
      run the notebooks.

5. Double-click on the ``network.ipynb`` notebook file in your working
   folder. (Or ``network_no_topology.ipynb`` if you want to analyse
   data that is topologically invalid.)

6. Navigate to the ``Data`` section.

   -  The cell with:

   .. code:: python

      trace_data = ""
      area_data = ""
      name = ""

   -  Is the starting section for analysis. Follow the guidance within
      the notebook itself to complete the network analysis.
   -  You can *tab-complete* within quotes for filepaths in the notebook
      as well.

7. After filling the data section, you can run the notebook from the
   beginning by pressing the *Restart the kernel and run all cells*
   button at the top of the notebook. The button has a double arrow
   symbol pointing to the right.

Final notes
-----------

The environment is **temporary**. Download all results when you are
finished.
