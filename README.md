# python_arduino_pyqt5
this project show how to use pyqt5 to control arduino by python language.
1. first you need have a arduino board, here i use arduino uno .
2.you need to install lib of arduino Firmata ; 
    /*
      Firmata is a generic protocol for communicating with microcontrollers
      from software on a host computer. It is intended to work with
      any host computer software package.

      To download a host software package, please click on the following link
      to open the list of Firmata client libraries in your default browser.

      https://github.com/firmata/arduino#firmata-client-libraries

      Copyright (C) 2006-2008 Hans-Christoph Steiner.  All rights reserved.
      Copyright (C) 2010-2011 Paul Stoffregen.  All rights reserved.
      Copyright (C) 2009 Shigeru Kobayashi.  All rights reserved.
      Copyright (C) 2009-2016 Jeff Hoefs.  All rights reserved.

      This library is free software; you can redistribute it and/or
      modify it under the terms of the GNU Lesser General Public
      License as published by the Free Software Foundation; either
      version 2.1 of the License, or (at your option) any later version.

      See file LICENSE.txt for further informations on licensing terms.

      Last updated August 17th, 2017
    */
3. python also need to install lib pyfirmata,for example :from pyfirmata import Arduino, util
  you can use pip install pyfirmata command to install this lib.
  
4.you need to install pyqt5 , i suggestion you install from douban fichier miroir:
  pip install PyQt5 -i https://pypi.douban.com/simple
  intall pyqt5 tools use:pip install PyQt5-tools -i https://douban.com/simple
5.you can search how to use qtdesigner from www.baidu.com
