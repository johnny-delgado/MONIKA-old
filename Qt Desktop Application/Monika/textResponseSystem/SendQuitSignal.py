import TextFileHandler
import PathInitializer


#path = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/" #the absolute path to this folder
path = PathInitializer.path

TextFileHandler.setStatus(path + "KeepLoopRunning.txt", "Toggle", "0")