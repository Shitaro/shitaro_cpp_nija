#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import glob

ninja="""cxxflags = -Wextra -g -O2 -std=c++11
cxx = clang++

rule compile 
  command = $cxx $cppflags -c $in -o $out

rule link
  command = $cxx $in -o $out

"""

target='build ../bin/main : link '
object=''
files=glob.glob('*.cpp')
for file in files:
    name,ext=os.path.splitext(file)
    object=object+'build '+name+'.o : compile '+file+'\n'
    target=target+name+'.o '
    
f=open('build.ninja','w')
ninja=ninja+object+target+'\n'
f.write(ninja)
f.close()
