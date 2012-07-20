#charms

collection of charms used by the team. Currently available charms:

    * django: Python web framework. Setup using nginx, gunicorn and virtualenv.
    * nodejs: Node.JS


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
