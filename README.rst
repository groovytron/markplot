.. image:: https://travis-ci.org/groovytron/markplot.svg?branch=master
    :target: https://travis-ci.org/groovytron/markplot

Simple script capable of generating plots and csv files from projects'
journal files containing a :code:`Markdown` table. The journals must have
the same format as the example `journal-sample.md <journal-sample.md>`_ file.

Install
-------

Markplot is a python package, so it can be installed like this:

.. code-block:: console

    pip install markplot

CLI
---

Markplot includes a simple CLI. It only takes files as arguments. For examples:

.. code-block:: console

    $ markplot journal-sample.md
    Projects' information has been written in 'generated' directory.

The above example uses the sample file and generates files named
:code:`generated/journal-sample/hours_journal-sample.csv` and
:code:`generated/journal-sample/time_histogram_journal-sample.png`.

Docs
----

The :code:`--help` arg will make it show a usage page:

.. code-block:: console

    $ markplot --help
    Usage: markplot [OPTIONS] [JOURNALS]...

      This script simply generates feedbacks from projects' journals. Output is
      generated in a directory called «generated».

      Generate one feedback from a journal:
          feedbackgenerator journal.md

      Generate two feedbacks from two journals:
          feedbackgenerator journal1.md journal2.md

    Options:
      --help  Show this message and exit.
