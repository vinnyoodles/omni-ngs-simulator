# Omni NGS Simulator

A web-based suite of tools to simulate NGS data.

## Running with Docker

`Makefile` contains the commands to build and run all docker services.

To manually build all services:
```bash
docker-compose build
```

To manually run all services:
```bash
docker-compose up
```

## Adding new simulators

### 1. Add an entry in the [simulator dictionary](https://github.com/vinnyoodles/omni-ngs-simulator/blob/2b1b9f480e03d412f0478a653a6ebb2684f5c36f/app/simulators/__init__.py#L1)

It should have the following format:

```
title:       title that will be rendered in html
caption:     description of the simulator that will be rendered in html
route:       url path name (follows /simulators)
arguments:   list of argument names in the order that they must appear in the qsub script
tags:        list of keywords used for searching
ready:       boolean dictating whether or not the simulator is production ready
```

### 2. Create flask form class

Use the [base class](https://github.com/vinnyoodles/omni-ngs-simulator/blob/2b1b9f480e03d412f0478a653a6ebb2684f5c36f/app/forms.py#L32) as the parent class.

Any additional parameters/form fields that are not included in the base class must be added in the simulator specific class.
The documentation for the form fields can be [found here](https://flask-wtf.readthedocs.io/en/stable/index.html)

### 3. Create form html file

The simulator requires an html file that is specific to it and all of its parameters/fields.
It should be placed under the `app/templates/simulators` directory and should be named the same as the route entry in the dictionary.

### 4. Create qsub script

The service expects there to exist a qsub script for every simulator and calls it [here](https://github.com/vinnyoodles/omni-ngs-simulator/blob/b64a885476b31adf424aec8b7941f1a0796355a7/app/tasks.py#L81). The qsub script should contain the following:

- qsub parameters
    - walltime, queue, allocation, etc...
- initial update request
    - this is important for two reasons: first it updates the job status as `running` and second it populates the job command information
    - the job argument interpolation is done individually in each qsub script, look at [interpolated_command](https://github.com/vinnyoodles/omni-ngs-simulator/blob/b64a885476b31adf424aec8b7941f1a0796355a7/arc/dwgsim.qsub#L29) variable in any of the existing qsub scripts
- job command
- final update request
    - this updates the job status to be `finished` and sends the email notification

### Examples

- [grinder](https://github.com/vinnyoodles/omni-ngs-simulator/pull/30/files)
- [simhtsd](https://github.com/vinnyoodles/omni-ngs-simulator/pull/29/files)


