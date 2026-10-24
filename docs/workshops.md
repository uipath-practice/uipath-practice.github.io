# Workshops

A workshop is a sequence of exercises run together in one session. Pick one, or compose your own from the [catalog](index.md).

{% for w in workshops %}
## {{ w.title }}

**Audience:** {{ w.audience }} · **Status:** {{ w.status }}

| # | Exercise | Duration |
|---|---|---|
{% for s in w.sequence %}{% set e = exercise_by_ref.get(s.exercise) %}| {{ loop.index }} | {% if e %}[{{ e.title }}]({{ e.page }}){% else %}{{ s.exercise }}{% endif %} | {{ s.duration }} |
{% endfor %}
{% endfor %}
