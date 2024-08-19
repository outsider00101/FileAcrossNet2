# FileAcrossNet2
Library for transmitting files across network.

Contains:
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
    if in fileReciever or binFileReciever fileName is not defined, they will use fileName from fileSender or binFileSender
