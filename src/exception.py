import sys
from src.logger import logging

# Errors can be corrected during compilation of source code or even at runtime. It can syntax error or semantic error. 
# Exceptions are caused during run time when the interpreter gets some unexpected data.
# They are handled using try and except technique. 


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    return error_message

# We have created function over here which will give message, how your message should look like inside file w.r.t custom exception
# then we have created custom exception class which is inhiriting from Exception class 

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# if __name__=="__main__":
    
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e,sys)