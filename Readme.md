# Yet Another Logger    [![Documentation Status](https://readthedocs.org/projects/yalogger/badge/?version=latest)](https://yalogger.readthedocs.io/en/latest/?badge=latest) ![PyPI](https://img.shields.io/pypi/v/YALogger) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/DivyenduDutta/YALogger/blob/master/LICENSE.md) [![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Minimalist logger written in python.

Currently only provides three functions for logging. Also currently log() only supports logging text and dict, whereas
for other python objects it logs the type only. Enhancement open in issues.

1. **Method entry logging**

2. **Method exit logging**

3. **Normal logging**

Both Method entry logging and Method exit logging are only *INFO* level logging by default

Supports *3 levels of logging* - *INFO, ERROR, DEBUG*. These are mutually exclusive (ie not hierarchial)

Supports *2 modes of logging*:

1. **FILE** - Writes logs to a file in the logs folder 

2. **CONSOLE** - Logs to the standard output console

Uploaded to PIP - [PIP repo](https://pypi.org/project/YALogger).


**Log format - [log_level timestamp] [Module name]-[Method name] <log text>**

## Documentation

Hosted on [Read The Docs](https://yalogger.readthedocs.io/en/latest/).

Achieved via Sphinx (as the doc build tool), reStructuredText as the markup and hosted on Read The Docs website.

## INSTALLATION

run 
```
pip install YALogger
```

## IMAGE
Log file looks like source

![alt text](https://github.com/DivyenduDutta/YALogger/blob/master/images/log%20output%20file.PNG)

logger.properties looks like so

![alt text](https://github.com/DivyenduDutta/YALogger/blob/master/images/logger%20properties.PNG)

	
## REQUIREMENTS
	
1. logger.properties file

2. logs folder


logger.properties file needs to have **[logger properties]** at the root
	
## SAMPLE USAGE
	
```from YALogger.custom_logger import Logger 
Logger.initialize_logger(logger_prop_file_path = '.\logger.properties',log_file_path = './logs') 
Logger.perform_method_entry_logging('foo','bar')
Logger.perform_method_exit_logging('foo','bar') 
Logger.log('info', 'foo','bar','this is the log text')
```

Look for sample usage code in sample folder

Refer to [sample logger.properties](https://github.com/DivyenduDutta/YALogger/blob/master/Yet%20Another%20Logger/sample/logger.properties).

Ensure logs folder is present 


## License

This is an open source tool licensed under GPL v3.0. Copy of the license can be found
[here](https://github.com/DivyenduDutta/goodreads-scraper-visualizer/blob/master/LICENSE.md).
