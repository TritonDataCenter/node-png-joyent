import Options
from os import unlink, symlink, popen
from os.path import exists 

srcdir = "."
blddir = "build"
VERSION = "0.0.1"

def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  conf.check(lib='png14', libpath=['/lib', '/usr/lib', '/usr/local/lib', '/usr/local/libpng/lib', '/usr/local/pkg/libpng-1.4.1/lib', '/opt/local/lib'])

def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.target = "png"
  obj.source = "src/common.cpp src/png_encoder.cpp src/png.cpp src/fixed_png_stack.cpp src/dynamic_png_stack.cpp src/module.cpp src/buffer_compat.cpp"
  obj.uselib = "PNG14"
  obj.cxxflags = ["-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-I/opt/local/include"]

def shutdown():
  pass
