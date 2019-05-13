# ckanext-iauthfunctions-about

ckan extension for setting access for the route `/about`

# Overview

The extension set the access for the `/about` page. Only the user name as `hp` **(not uppercase)** can see the `/about` page

But note that **admin_user** always have the access to all the stuff, so you may want to use the normal user to try the extension

# Set up

1. download the extension using `git clone https://git.indocresearch.org/ckanext/ckanext-iauthfunctions-about.git`

2. run the `python setup.py develop` to install the plugin

3. add the `ckanext-iauthfunctions` to `ckan.plugins` attribute in the `development.ini` file

4. replace the function `def about()` in file `ckan/ckan/views/home.py` below:

```
def about():
    u''' display about page'''
    try:
        p.toolkit.get_action('my_auth')(None, None)
    except p.toolkit.NotAuthorized:
        p.toolkit.abort(403, 'Not authorized to see this tab')

    return base.render(u'home/about.html', extra_vars={})
```

5. then run the command `paster serve /etc/ckan/default/development.ini` **under the virtual environment**


