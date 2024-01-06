# libgpiod standalone Python 3 bindings

This is a repackaged distribution of the [libgpiod](https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about)
Python bindings.

The upstream project on kernel.org builds the libgpiod C library and Python extensions as part of an
autotools build, which can be cumbersome for local installation or Python virtualenvs. This repo is
all of the same code repackaged as a standalone Python module which doesn't require libgpiod itself
to be installed. Instead, all the core libgpiod code is compiled into the Python extension module.

## Build Instructions

**Requirements**

* Python 3 and setuptools
* A C compiler (probably gcc) that can build Python C extension modules
* Recent Linux kernel headers, version 4.8 or greater

Building is the usual process for Python setuptools packages, e.g.

```
python3 setup.py build
python3 setup.py build_ext -i
python3 setup.py install
```

## Structure

Most of the code here is taken verbatim from libgpiod, which is hosted at
https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about

* `gpiod/` - the core libgpiod code, from the 'include/' and 'lib/' folders, plus the
  `bindings/python/gpiodmodule.c` file
* `examples/` - taken from `bindings/python/examples` folder
* `setup.py` - Python module setup script, the only original content in this repo

## License
libgpiod is licensed under the LGPL v2.1 or later, and so is my setup.py. See the COPYING file and
headers of individual source files for more information.
