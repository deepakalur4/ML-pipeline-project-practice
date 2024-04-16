import sys
import os

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"Error occocured in the file name {file_name} and line no {exc_tb.tb_lineno} and the error is {error}"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error=error_message,error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message
