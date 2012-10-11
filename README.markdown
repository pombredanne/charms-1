#charms

Collection of charms used by tsuru.

Creating charms
---------------

To enable new environments, you need to create a new charm. A charm
has a directory structure explained below:

<pre>
+-centos/
| +-django/
|   +-hooks/
|   | +-install
|   | +-dependencies
|   | +-start
|   | +-stop
|   | +-restart
|   +-metadata.yaml
+-precise/
  +-nodejs/
    +-hooks/
    | +-install
    | +-dependencies
    | +-start
    | +-stop
    | +-restart
    +-metadata.yaml
</pre>

### Metadata file

Every charm must have a metadata.yml to describe the charm. It's
described in juju docs - https://juju.ubuntu.com/docs/write-charm.html

### Hooks

Every environment needs 5 hooks. Every hook must be created with
execution permission. The hooks as described below:

#### install

This script used to install the packages your environment needs
to be ready for deploy.

#### dependencies

This script is used to install your application dependencies when you
deploy it (e.g. pip install, npm install, bundle install).

#### start

This script starts your application.

#### stop

This script stops your application.

#### restart

This script restarts your application. It's used every time you deploy
your application.




