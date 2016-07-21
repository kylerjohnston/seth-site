from flask.ext.assets import Bundle

css_all = Bundle('css/bootstrap.min.css',
                 'scss/base.scss',
                 filters = 'scss,cssutils',
                 output = 'gen/compiled.css')

fontawesome = Bundle('font-awesome-4.6.3/scss/font-awesome.scss',
                     filters = 'scss,cssutils',
                     output = 'gen/fontawesome.css')

js_all = Bundle('js/jquery-1.9.1.min.js',
                'js/bootstrap.min.js',
                output = 'gen/compiled.js')
