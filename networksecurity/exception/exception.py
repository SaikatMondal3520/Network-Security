import sys

class NetworkSecurityException(Exception):
  def __init__(self,error_mesage,error_details:sys):
    self.error_message=error_mesage
    _,_,exc_tb = error_details.exc_info()

    self.lineno=exc_tb.tb_lineno
    self.file_name=exc_tb.tb_fraem.f_code.co_filename

  def __str__(self):
    return"Error occured in Python Script name [{0}] line number [{1}] error message[{2}]".format(
      self.file_name, self.lineno, str(self.error_mesage))


if __name__=='__main__':
  try:
    a=1/0
    print("This will not be printed", a)
  except Exception as e:
    rasie NetworkSecurityException(e,sys)
