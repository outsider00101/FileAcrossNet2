# FileAcrossNet2
Library for transmitting files across network.

  Variables:
    
    defaultWriteOperationsMode = "w"
    defaultReadOperationsMode = "r"
    defaultBinReadOperationsMode = "rb"
    defaultBinWriteOperationsMode = "wb"
    defaultEncodeDecode = "utf-8"
  
  Functions:
    
    fileSender( self, sendTo, fileName, *encode, *readOperationMode )
    fileReciever( self, From, *fileName, *decode, *writeOperationMode )
    binFileSender( self, sendTo, fileName, *binReadOperationMode )
    binFileReciever( self, From, *fileName, *binWriteOperationMode )

  Descriptions:
    
    If in fileReciever or binFileReciever fileName is not defined, they will use fileName from fileSender or binFileSender
    I tried to make ability to change the variables containment through defining (FileAcrossNet.defaultWriteOperationsMode = "a+")
      but it's not work. I'll make it soon.
    Library tested on text files, .png, .exe
