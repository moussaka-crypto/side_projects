def getNode(name, list):
   return next(( i for i in list if i.name == name), -1)