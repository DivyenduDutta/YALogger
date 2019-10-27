from YALogger.custom_logger import Logger
def func():
	print('Doing some king of evaluation inside func()')
	

'''
Change properties file to use other options.
'''
Logger.initialize_logger(logger_prop_file_path = '..\logger.properties',log_file_path = '../logs') 
Logger.perform_method_entry_logging(module_name = 'foobar',method_name = 'func')
Logger.perform_method_exit_logging(module_name = 'foobar',method_name = 'func') 
Logger.log('info', 'foobar','func','this is the log text')
