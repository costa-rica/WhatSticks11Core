
# What Sticks 11 Core

![What Sticks Logo](wsLogo180.png)

## Description
These packages provide configuration variables and database schemas for the What Sticks Flask API, website, and service applications. What Sticks 11 Core is made up of two custom Python packages, ws_config and ws_models.

## Installation Instructions
To install the What Sticks 11 Core, clone the repository and install the required dependencies:
```
git clone [repository-url]
cd WhatSticks11Core
pip install -e .
```



## Usage
After installation, import the modules into your Python projects as needed:

```python
from ws_config import ConfigLocal, ConfigDev, ConfigProd
from ws_models import Base, create_engine, inspect, sess, engine, text, \
    Users, \
    CommunityPosts, CommunityComments,NewsPosts, NewsComments, \
    UserLocationDay, Locations, WeatherHistory, \
    OuraToken, OuraSleepDescriptions, \
    AppleHealthQuantityCategory, AppleHealthWorkout, \
    AppleHealthExport
```


## Contributing

We welcome contributions to the What Sticks 11 Core project.


For any queries or suggestions, please contact us at nrodrig1@gmail.com.