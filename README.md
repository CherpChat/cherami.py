USAGE:

Place __init__.py and api.py into a folder named 'cherami' in your python project.

Then within your code, use it as such:

```py
from cherami.api import API

cherami_api = API('token goes here', "https://cherami.chat") # or https://staging.cherami.chat

notifs = cherami_api.notifications()
```