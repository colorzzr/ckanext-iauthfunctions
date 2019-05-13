# ckanext-iauthfunctions-about

ckan extension for setting access for the route `/about`

# Overview

The extension set the access for the `/about` page. Only the user name as `hp` **(not uppercase)** can see the `/about` page

But note that **admin_user** always have the access to all the stuff, so you may want to use the normal user to try the extension

# Set up

1. download the extension using 

```
git clone https://git.indocresearch.org/ckanext/ckanext-iauthfunctions-about.git
```

2. Active the virtual environment

```
cd ckanext-iauthfunctions-about
. /usr/lib/ckan/default/bin/activate
```

3. to install the plugin

```
python setup.py develop
```

4. add the `iauthfunctions` to `ckan.plugins` attribute in the `development.ini` file

5. replace the function `def about()` in file `ckan/ckan/views/home.py` below:

```
def about():
    u''' display about page'''
    try:
        p.toolkit.get_action('my_auth')(None, None)
    except p.toolkit.NotAuthorized:
        p.toolkit.abort(403, 'Not authorized to see this tab')

    return base.render(u'home/about.html', extra_vars={})
```

6. then run the command **under the virtual environment**

```
paster serve /etc/ckan/default/development.ini
```


