#!/bin/bash

for ((i=$1; i<=$2; i+=1))
do
  prefix=""
  if [ $i -le 99 ]; then
    prefix="0"
  fi
  tesseract "./resources/image_exports/My belief _ essays on life and art - Hesse, Hermann, 1877-1962_Page_${prefix}${i}_Image_0002.jpg" - -l eng
done
