class SubrunnerError(Exception):
    """Base subrunner error"""
    pass

class CommandNotFoundError(SubrunnerError):
    """Command not founded"""
    pass