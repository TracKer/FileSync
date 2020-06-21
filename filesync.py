from Misc.CommandLineHandler import CommandLineHandler


commandLineHandler = CommandLineHandler()
if commandLineHandler.getAction() == 'init':
    # 1. Run file system watcher
    # 2. Run file system indexer
    # 2.1. Write index data to .fs_tracker
    pass
elif commandLineHandler.getAction() == 'watch':
    # 1. Run file system watcher
    pass
