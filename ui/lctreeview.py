
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

#used to bold the currently shown landclass/imported file
class BoldDelegate(QtGui.QStyledItemDelegate):

    def paint(self, painter, option, index):
        if index.data(QtCore.Qt.UserRole) == 1:
            option.font.setWeight(QtGui.QFont.Bold)
            
        QtGui.QStyledItemDelegate.paint(self, painter, option, index)    
        
#Extended class for showing the landclasses that can do drag-drop
class LCTreeViewModel(QtGui.QStandardItemModel):
    def __init__(self):
        super(LCTreeViewModel,self).__init__()
    def mimeData(self, indexes):
        i = indexes[0]
        md = QtCore.QMimeData()
        md.setText(i.data())
        return md
        
    def mimeTypes(self):
        return ['text/plain']
    def dropMimeData(self, data, action, row, column, parent):
        
        item = QtGui.QStandardItem(data.text())
        p = self.itemFromIndex(parent) # get the real parent
        
        #findItem is not working, not sure why
        #but make sure we aren't dropping the same thing 
        for i in range(0,p.rowCount()):
            if p.child(i).text() == data.text():
                return False
        item.setDropEnabled(False)
        item.setDragEnabled(False)
        p.appendRow(item)
        return True
#Extended class that can do drag-drop    
class LCTreeView(QtGui.QTreeView):
    def __init__(self,parent):
        super(LCTreeView,self).__init__(parent)
        self.setItemDelegate(BoldDelegate(self))
        
        
     
    def dropEvent(self, event):
        super(LCTreeView,self).dropEvent(event)
    
    def dragEnterEvent(self, event):
        event.accept()
    
    def dragmoveEvent(self,event):
        event.accept()
        
    