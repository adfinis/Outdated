# Outdated

This Application is meant to make it easier to know what Project has outdated Packages, Outdated Packages are Packages that have gone out of Long Term Support (short lts). There is a colour-code to what state a Project is in:

Green: Project is up to date

Yellow: One or more Packages released a new lts version, you "should" upgrade to it now since the other version is still in support

Red: One or more Packages are outdated

Gray: There are no Packages added to this Project.

---

## How to __start__ the __application__?

First install Docker-Compose and Poetry, after that download or clone this project, then rename .env.dist file and change the values of the variables to your liking. Then run ```docker compose up -d``` this will start the database.
For starting the Django App, please wait until the database is properly started after that run ```poetry run python outdated/manage.py runserver```.
