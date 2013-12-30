import os
import sys
#import Image
import filecmp
import shutil

class chitra:
  def __init__(self):
    self.get_argv()
    
  def get_argv(self):
    self.path = sys.argv[1]
    if self.path == '-delete':
      self.del_backup()
    elif self.path == '-about':
      self.show_about()
    else:
      self.get_images()
      self.check_images()
    
  def get_images(self):
    self.image_list = []
    
    for root, dirs, files in os.walk(self.path):
      for name in files:
	if name.lower().endswith('.jpg'):
	  self.image_list.append(os.path.join(root,name))

  def check_images(self):
    length = len(self.image_list)
    for i in xrange(0,length-1):
      for j in xrange(i+1,length):
	if len(self.image_list)==2:
	  print 'Checking',self.image_list[i],'and',self.image_list[j]
	  self.check_two(length)
	else:
	  print 'Checking',self.image_list[i],'and',self.image_list[j]
	  if((filecmp.cmp(self.image_list[i],self.image_list[j]))==True):
	    print self.image_list[i],' and ',self.image_list[j],' are duplicate images.'
	    self.menu(self.image_list[i],length)

  def menu(self,path,lth):
    print '1. Preview Image'
    print '2. Delete Image'
    print '3. Backup and Delete Image'
    print '4. Ignore Image'
    print '5. Exit'
    ch = int(raw_input('Enter your choice:(1/2/3/4/5):'))
    
    if ch == 1:
      self.thumbnail(path)
      self.menu(path,lth)
    if ch == 2:
      self.delete(path,lth)
    if ch == 3:
      self.bdelete(path,lth)
    if ch == 4:
      pass
    if ch == 5:
      exit()
      
  def thumbnail(self,path):
    size = 550,550
    im = Image.open(path)
    im.thumbnail(size)
    im.show()
    pass
    
  def delete(self,path,lth):
    os.remove(path)
    self.get_images()
    self.check_images()

  def create_dir(self):
    usr_home = os.environ['HOME']
    self.chitra_dir = usr_home + '/.chitra'
    if not os.path.exists(self.chitra_dir):
      os.mkdir(self.chitra_dir)
            
  def bdelete(self,path,l):
    self.create_dir()
    shutil.copy(path,self.chitra_dir)
    self.delete(path,l)
      
  def del_backup(self):
    os.system('rm ~/.chitra/*')  
    
  def check_two(self,lth):
    if((filecmp.cmp(self.image_list[0],self.image_list[1]))==True):
	print self.image_list[0],' and ',self.image_list[1],' are duplicate images.'
	self.menu(self.image_list[0],lth)
	sys.exit(0)
    
  def show_about(self):
    print "Chitra"
    print "(c) 2011 Sayan Chowdhury"
    print "http://gitorius.org/chitra"
    print "Sayan Chowdhury <sayan.chowdhury2012@gmail.com>"
    
if __name__ == '__main__':
    obj = chitra()