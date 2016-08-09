============
Installation
============

Installation for the project is actually too easy. Ensure you have Docker installed, then just run this simple command:

::

    docker-compose up # builds all containers and runs it

We have five containers that we use:

- **Web** - main container that runs the Django process
- **Node** - compiles our ReactJS code
- **Docs** - compiles the Sphinx code using the ``docs/watchdocs.py`` script.
- **Db** - PostgreSQL database container.
- **Redis** - the Redis container for message passing for Django channels.
