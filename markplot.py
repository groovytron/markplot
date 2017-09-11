#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import click

outdir = "generated"


def generate_feedback(journal):
    mdreader = csv.reader(journal, delimiter="|", quotechar="|")
    headers = next(mdreader)
    headers = tuple([h.strip() for h in headers])

    next(mdreader)
    histogram = dict()
    activities = []

    for row in mdreader:
        activity_type, task, date, description, minutes = tuple(
            [item.strip() for item in row])
        minutes = int(minutes)

        activities.append(
            tuple([activity_type, task, date, description, minutes]))

        if histogram.get(activity_type, None) is None:
            histogram[activity_type] = minutes
        else:
            histogram[activity_type] += minutes

    n_groups = len(histogram.keys())
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {"ecolor": 0.3}

    plt.bar(
        index, [t / 60 for t in histogram.values()],
        bar_width,
        alpha=opacity,
        color="b",
        error_kw=error_config,
        label="Julien M'Poy")

    plt.xlabel("Activity type")
    plt.ylabel("Spent time (in minutes)")
    plt.title("Time spent on the project overview")
    plt.xticks(index + bar_width / 2, tuple(histogram.keys()))
    plt.legend()
    figure = plt.gcf()
    figure.set_size_inches(17.5, 10.5)

    filename = journal.name
    project_name = filename[0:filename.find(".")]

    output_dir = outdir + "/" + project_name + "/"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    figure.savefig(
        output_dir + "time_histogram_" + project_name + ".png", dpi=100)

    with open(output_dir + "hours_" + project_name + ".csv", "w") as out:
        csv_out = csv.writer(out)
        csv_out.writerow(headers)
        for row in activities:
            csv_out.writerow(row)


@click.command()
@click.argument("journals", nargs=-1, type=click.File("r"))
def cli(journals):
    """This script simply generates feedbacks from projects' journals. Output
    is generated in a directory called «generated».

    \b
    Generate one feedback from a journal:
        feedbackgenerator journal.md

    \b
    Generate two feedbacks from two journals:
        feedbackgenerator journal1.md journal2.md
    """

    if len(journals) <= 0:
        exit("Missing argument [JOURNALS]. Type 'markplot --help'"
             " to get examples.")

    for j in journals:
        generate_feedback(j)

    print("Projects' information has been written in 'generated' directory.")
