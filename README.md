# Omni NGS Simulator

A web-based suite of tools to simulate NGS data.

## Building docker image

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

### 1. Add the simulator specific dictionary values into `SIMULATORS` in `app/simulators/__init__.py`.

The documentation for the dictionary can be found in [app/tasks.py](https://github.com/vinnyoodles/omni-ngs-simulator/blob/a310525bcc8197711ac0d8925e0dbf4dd7503e38/app/tasks.py#L9-L48)

An example of the dictionary format for the command `echo` would be:

```python
'echo': {
    'command': 'echo',
    'arguments': ['string_to_echo']
    'defaults': { },
    'format': '{string_to_echo}'
    'stdout': True,
    'title': 'echo',
    'caption': 'Write arguments to the standard output'
    'route': 'echo_route'
}

...

@instance.route('/simulators/echo')
def echo_route():
    return render_template(...)
```

### 2. Add flask specific route for the simulator in `app/routes.py`.

This route has to match the `route` key in the dictionary specified in step 1.
The python function requires two decorators. The first decorator specifies the route's url, REST methods and other parameters.
The second decorator requires users to be logged in to visit the page.

```python
@instance.route('/simulators/example_simulator', methods=['GET', 'POST'], strict_slashes=False)
@login_required
```

### 3. Add form class in `app/forms.py`.

The form class is for validation and helps with creating the HTML file.
The class can inherit from `BaseSimulatorForm` because of some shared fields.
There shouldn't be anything new or different from the existing forms in `app/forms.py`, but the libraries used are [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) and [WTForms](https://wtforms.readthedocs.io/en/stable/index.html).

### 4. Create HTML file for the simulator and its form.

The file should be created in `app/templates/simulators`. Also, make sure to include the boilerplate code for rendering the headers and other parts.

```HTML
{% extends "container.html" %}

{% block content %}
    <div class="text-center" style="padding-top:20px">
        <h3 style="padding-bottom:10px">NAME OF SIMULATOR</h3>
        <div class="row">
            <div class="col-lg-6 offset-lg-3 text-center">
                <form action="" class="form job-form" method="POST" enctype="multipart/form-data" role="form">
                    {{ form.hidden_tag() }}

                    <div class="form-group row">
                        {{ form.name.label(class_='col-4 col-form-label')}}
                        <div class="col-8">
                            {{ form.name(class_='form-control', placeholder='Default - Job ID')}}
                        </div>
                    </div>

                    <div class="form-group row">
                        <div class="custom-file">
                            {{ form.file(class_='custom-file-input', accept='.fasta', required='') }}
                            {{ form.file.label(class_='custom-file-label') }}
                        </div>
                    </div>

                    <!-- Enter simulator specific forms here -->

                    {{ form.submit(class_='btn btn-outline-primary btn-block') }}
                </form>
            </div>
        </div>
    </div>
{% endblock %}
```

The HTML file requires a few parameters to be passed in, they are passed in from the route function.
The parameters that are expected are, in the following order:
    - path to the HTML file (relative to `routes.py`)
    - title (keyword argument) used in other html files
    - form (keyword argument) used to populate form fields

```python
@instance.route('/simulators/echo')
def echo_route():
    form = ExampleSimulatorForm()
    return render_template('simulators/example.html', title='Example', form=form)
```

### 5. Install simulator and its dependencies on machine

In order to run the simulator, it has to be configured to run. Ideally, the simulator should be placed in $PATH so it does not require an absolute path. The simulator would be run using the `command` key in the dictionary specified in the first step.


