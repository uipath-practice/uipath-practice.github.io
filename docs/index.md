# Workshops and Trainings Factory

**WTFactory** is where the UiPath Partner Success team builds and runs its hands-on workshops. This is the catalog. Each course is a participant handbook on its own site; each exercise is a complete business case with the environment prepared for you.

{% for c in courses %}
## [{{ c.title }}]({{ c.site }})

{{ c.summary }}

**Audience:** {{ c.audience }}

{% if c.exercises %}
| Exercise | What you build | Level | Products | Before you start |
|---|---|---|---|---|
{% for e in c.exercises %}| [{{ e.title }}]({{ e.page }}) | {{ e.summary }} | {{ e.level or '' }} | {% for p in e.products or [] %}{{ product_name(p) }}{% if not loop.last %}, {% endif %}{% endfor %} | {% for pr in e.prerequisites or [] %}{% set x = exercise_by_ref.get(pr) %}{% if x %}[{{ x.title }}]({{ x.page }}){% else %}{{ pr }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %} |
{% endfor %}
{% endif %}
{% endfor %}

<small>Catalog generated {{ generated }}.</small>
