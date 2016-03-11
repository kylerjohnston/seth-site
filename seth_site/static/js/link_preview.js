$.embedly.defaults.key = '92a082bc764d495591e6f49c7fb7199d';

var width = document.getElementById('post').offsetWidth;
$('.post a').embedly({query:
                     {maxwidth: width},
                     'method': 'after',
});
