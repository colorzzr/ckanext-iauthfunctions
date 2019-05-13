# ckanext-iauthfunctions-about

ckan extension for setting access for the route `/about`

# Overview

The extension set the access for the `/about` page. Only the user name as `hp`<bold>(not uppercase)</bold> can see the `/about` page

# Set up

1. run the `python setup.py develop` to install the plugin

2. add the `ckanext-iauthfunctions` to `ckan.plugins` attribute in the `development.ini` file

3. replace the function `def about()` in file `ckan/ckan/views/home.py` below:

```
def about():
    u''' display about page'''
    try:
        p.toolkit.get_action('my_auth')(context, data_dict)
    except p.toolkit.NotAuthorized:
        p.toolkit.abort(403, 'Not authorized to see this tab')

    return base.render(u'home/about.html', extra_vars={})
```

4. then run the command `paster serve /etc/ckan/default/development.ini` <bold>under the virtual environment</bold>


