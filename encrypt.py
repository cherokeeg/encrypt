#!/usr/bin/python

#import gtk # used in windows
import sys

class encode():
  birthday = 8382
  key = 100

  def ascii_list(self, s):
    """return a list of ascii values of the characters in string s"""
    return [ord(c) for c in s]

  def byte_list(self, c):
    """return a list of bytes values of the"""
    return [chr(s) for s in c]

  def encrypt(self, strContent_param):
    listBytes = self.ascii_list(strContent_param)
    i = 0
    for byte in listBytes:
      if ((byte > 47) and (byte < 58)):
        listBytes[i] = byte - 48
      elif ((byte > 64) and (byte < 91)):
        listBytes[i] = byte - 55
      elif ((byte > 96) and (byte < 123)):
        listBytes[i] = byte - 61
      else:
        break
      listBytes[i] = (self.birthday + i * self.key) % 62 + listBytes[i]
      if (listBytes[i] > 61):
        listBytes[i] = listBytes[i] - 62
      if ((listBytes[i] >= 0) and (listBytes[i] < 10)):
        listBytes[i] = listBytes[i] + 48
      elif ((listBytes[i] > 9) and (listBytes[i] < 36)):
        listBytes[i] = listBytes[i] + 55
      elif ((listBytes[i] > 35) and (listBytes[i] < 62)):
        listBytes[i] = listBytes[i] + 61
      else:
        break
      i = i + 1
    listChar = self.byte_list(listBytes)
    return ''.join(listChar)

def main(args):
  en = encode()
  encryption = en.encrypt(args[1])
  print encryption
#  cb = gtk.clipboard_get()
#  cb.set_text(encryption)
#  cb.store()

if __name__ == "__main__":
  main(sys.argv)
