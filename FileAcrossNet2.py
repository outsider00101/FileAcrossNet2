'''
AUTHOR: outsider001
'''
import os

#defaultWriteOperationsMode = "a+"
#defaultReadOperationsMode = "r"

class NotBinaryFile( Exception ):
    pass

class BinaryFile( Exception ):
    pass

class BinaryFileIsEmpty( Exception ):
    pass

class FileAcrossNet():
    def __init__( self, *args, **kwargs ):
        self.defaultWriteOperationsMode = "w"
        self.defaultReadOperationsMode = "r"

        self.defaultBinReadOperationsMode = "rb"
        self.defaultBinWriteOperationsMode = "wb"

        self.defaultEncodeDecode = "utf-8"

        if kwargs.get( self.defaultWriteOperationsMode ) != None:
            self.defaultWriteOperationsMode = kwargs.get( self.defaultWriteOperationsMode )
        if kwargs.get( self.defaultReadOperationsMode ) != None:
            self.defaultReadOperationsMode = kwargs.get( self.defaultReadOperationsMode )
        if kwargs.get( self.defaultBinReadOperationsMode ) != None:
            self.defaultBinReadOperationsMode = kwargs.get( self.defaultBinReadOperationsMode )
        if kwargs.get( self.defaultBinWriteOperationsMode ) != None:
            self.defaultBinWriteOperationsMode = kwargs.get( self.defaultBinWriteOperationsMode )
        if kwargs.get( self.defaultEncodeDecode ) != None:
            self.defaultEncodeDecode = kwargs.get( self.defaultEncodeDecode )

    def fileSender( self, sendTo, fileName, *args, **kwargs ):
        self.readOperationMode = FileAcrossNet().defaultReadOperationsMode
        self.Encode = FileAcrossNet().defaultEncodeDecode
        if kwargs.get( "readOperationMode" ) != None:
            self.readOperationMode = kwargs.get( "readOperationMode" )
        if kwargs.get( "encode" ) != None:
            self.Encode = kwargs.get( "encode" )
        sendTo.send( fileName.encode( self.Encode ) )
        file = open( fileName, self.readOperationMode )
        linesList = file.readlines()
        linesEnumeration = len( linesList )
        #print( int( linesEnumeration ) )
        linesEnumeration = int( linesEnumeration )
        sendTo.send( str( linesEnumeration ).encode( self.Encode ) )
        for line in linesList:
            sendTo.send( line.encode( self.Encode ) )
        file.close()

    
    def fileReciever( self, From, *args, **kwargs ):
        self.writeOperationMode = FileAcrossNet().defaultWriteOperationsMode
        self.Decode = FileAcrossNet().defaultEncodeDecode
        fileName = From.recv( 1024 )
        self.fileName = fileName.decode( self.Decode )
        if kwargs.get( "writeOperationMode" ) != None:
            self.writeOperationMode = kwargs.get( "writeOperationMode" )
        if kwargs.get( "fileName" ) != None:
            self.fileName = kwargs.get( "fileName" )
        if kwargs.get( "decode" ) != None:
            self.Decode = kwargs.get( "decode" )
        linesEnumeration = From.recv( 1024 )
        linesEnumeration = linesEnumeration.decode( self.Decode )
        linesEnumeration = int( linesEnumeration )
        file = open( self.fileName, self.writeOperationMode )
        #print( f"{linesEnumeration} : {type(linesEnumeration)}" )
        while linesEnumeration != 0:
            line = From.recv( 1024 )
            file.write( line.decode( self.Decode ) )
            linesEnumeration = linesEnumeration - 1
        file.close()
    
    def binFileSender( self, sendTo, fileName, *args, **kwargs ):
        self.binReadOperationMode = FileAcrossNet().defaultBinReadOperationsMode
        if kwargs.get( "binReadOperationMode" ) != None:
            self.binReadOperationMode = kwargs.get( "binReadOperationMode" )
        sendTo.send( fileName.encode( "utf-8" ) )
        file = open( fileName, self.binReadOperationMode )
        lines = file.readlines()
        #print( len( lines ) )
        sendTo.send( str( len( lines ) ).encode( "utf-8" ) )
        for line in lines:
            sendTo.send( line )
        file.close()

    def binFileReciever( self, From, *args, **kwargs ):
        self.binWriteOperationMode = FileAcrossNet().defaultBinWriteOperationsMode
        fileName = From.recv( 1024 )
        print( fileName )
        self.fileName = fileName.decode( "utf-8" )
        if kwargs.get( "binWriteOperationMode" ) != None:
            self.binWriteOperationMode = kwargs.get( "binWriteOperationMode" )
        if kwargs.get( "fileName" ) != None:
            self.fileName = kwargs.get( "fileName" )
        linesEnumeration = From.recv( 1024 )
        linesEnumeration = int( linesEnumeration.decode( "utf-8" ) )
        file = open( self.fileName, self.binWriteOperationMode )
        while linesEnumeration != 0:
            print( linesEnumeration )
            line = From.recv( 1024 )
            file.write( line )
            linesEnumeration = linesEnumeration - 1
        file.close()