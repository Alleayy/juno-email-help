project = 'Email Help'
author = 'Your Name'
release = '1.0'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

{% extends "!layout.html" %}

{% block meta %}
  {{ super() }}
  <meta name="google-site-verification" content="vWuKdfn7mBaw-KlLRh8j_GtlIs4FQ-h0VcG-WO8D8ns" />
  <meta name="msvalidate.01" content="YOUR_BING_VERIFICATION_CODE">
{% endblock %}


html_js_files = [
    'chat.js',
    '_static/chat.js',
]
