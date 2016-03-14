from flask.ext.assets import Bundle

css_all = Bundle('scss/base.scss',
                 filters = 'scss,cssutils',
                 output = 'gen/compiled.css')
