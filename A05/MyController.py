from PySide.QtCore import *
from PySide.QtGui import *

from MyView import *
from MyModel import *


class MyController(QWidget):
  """
  MVC pattern: Creates a controller - mvc pattern.
  """
  def __init__(self, parent=None):
      """
      Create a new controller with a object MyView and a object MyModel
      using the mvc pattern.
      :param parent:
      """
      super().__init__(parent)
      self.myForm = MyView.Ui_Form()
      self.myForm.setupUi(self)
      self.myModel = MyModel.MyModel()
      # connect the buttons with the clicked signal
      self.connectButtons()
      # start a new game
      self.start()