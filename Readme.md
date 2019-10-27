# goodreads-scraper-visualizer   

Minimalist logger written in python.

Currently only provides three functions for logging

1. **Method entry logging**

2. **Method exit logging**

3. **Normal logging**

Both Method entry logging and Method exit logging are only *INFO* level logging by default

Supports *3 levels of logging* - *INFO, ERROR, DEBUG*. These are mutually exclusive (ie not hierarchial)

Supports *2 modes of logging*:

1. **FILE** - Writes logs to a file in the logs folder 

2. **CONSOLE** - Logs to the standard output console


**Log format - [<log level> <timestamp>] [Module name]-[Method name] <log text>**
	
### REQUIREMENTS
	
1. logger.properties file

2. logs folder


logger.properties file needs to have [logger properties] at the root
	
### SAMPLE USAGE
	
```from YALogger.custom_logger import Logger 
	Logger.initialize_logger(logger_prop_file_path = '.\logger.properties',log_file_path = './logs') 
	Logger.perform_method_entry_logging('foo','bar')
	Logger.perform_method_exit_logging('foo','bar') 
	Logger.log('info', 'foo','bar','this is the log text')```


### License

This is an open source tool licensed under GPL v3.0. Copy of the license can be found
[here](https://github.com/DivyenduDutta/goodreads-scraper-visualizer/blob/master/LICENSE.md).
