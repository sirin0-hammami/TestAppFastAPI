class NotFoundException(BaseException):
    def __init__(self, message = "Data not found"):
        self.message = message
        super().__init__(self.message)
    
    