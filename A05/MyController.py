from PySide import QtCore,QtGui

from A05.MyModel import *
from A05 import MyView



class MyController(QtGui.QWidget):
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

MyController()