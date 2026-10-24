# Product coverage

Which exercise exercises which product. One row per exercise, one column per product.

<div class="coverage" markdown>

| Exercise |{% for p in products %} {{ product_name(p) }} |{% endfor %}
|---|{% for p in products %}:-:|{% endfor %}
{% for c in courses %}{% for e in c.exercises %}| [{{ e.title }}]({{ e.page }}) |{% for p in products %} {% if p in (e.products or []) %}●{% endif %} |{% endfor %}
{% endfor %}{% endfor %}

</div>
