import os 
import sys

class CreditException(Exception):
    
    def __init__(self,error_message:Exception,error_details:sys):
        super().__init__(error_message)
        self.error_message =CreditException.error_message_details(error=error_message,error_details=error_details)

#defined a function to get detailed error message 
    @staticmethod
    def error_message_details(error:Exception,error_details:sys):
          _,_,exc_tb  = error_details.exc_info()
          line_number =exc_tb.tb_frame.f_code.co_filename

    #extracting file name from exception traceback
          file_name = exc_tb.tb_frame.f_code.co_filename

    #preparing error message
          error_message = f"Error occured python script name [{file_name} line no. [{exc_tb.tb_lineno}] error_message [{str(error)}]"

          return error_message

    def __str__(self):
          return CreditException.__name__.__str__()
