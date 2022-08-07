# Notes for website creation

Anything returned from functions defined with the @view.routes("string") is html returned to the screen

## Jinja Tutorial

To have a base html reference do 
```
{% extends "base.html" %}
```

To set Title in jinja:
```
{% block title %}Login{% endblock %}
```

### For setting main content of a page
```
{% block content %}

<h1>This is Content</h1>

{% endblock %}
```

You can pass variables into html template by setting it in render_template("htmlname.html", variable=value)

For writing Boolean functions to pass to template do the following inside a block:
```
{% if TorF1 == True %}
Yes it is true!
{% elif TorF2 %}
Second one is true
{% else %}
No it is not true
{% endif %}
{% endblock %}
```

for a block container do :
```
<div class="container">
	{% block content %}
	{% endblock %}
</div>
```
models.py file is for notes and dtb models

You can roll the website into a .whl file, just with the requirement that you need to run the `main.py` file, however no changes to it is nessessary