# Cancer Cell Nuclei Segmentation
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)



| ![VideoBlocks](https://static1.olympus-lifescience.com/modules/imageresizer/599/856/ffd2cef388/700x504p350x252.jpg)  | ![](https://i.ibb.co/8bng010/opening.jpg) | ![GraphicStock](https://i.ibb.co/N1jVVcy/Markers.jpg) |
|:---:|:---:|:---:|
| |  |  |

> The aim of this project is to segment the cell nuclei from the rest of the image using watershed technique to help microbiologists and life science researchers

---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description
* The conventional method used was granulometry. However the accuracy rate of granulometry is highly dependent on cell overlapping. For objects containing highly overlapped cells, the method fails to accurately measure the size of the components.

* The Watershed Segmentation algorithm has many applications and is quite useful for segmenting overlapping objects. The project uses both OTSU binarization and Watershed to threshold and segment the cell nuclei from the tissues. The image show the cell nuclei as blue as they have been dyed with [DAPI](https://en.wikipedia.org/wiki/DAPI) to make segmentation easier as one only needs to extract the Blue Channel from RGB. 

#### Technologies

- [OpenCV](https://pypi.org/project/opencv-python/)
- [Numpy](https://pypi.org/project/numpy/)
- [Matplotlib](https://pypi.org/project/matplotlib/)


---

### :rocket: Results
| ![Original](https://i.ibb.co/BZq4JFD/Original.jpg)  | ![](https://i.ibb.co/BBxm5Jc/Boundaries-overlayed-from-colored-grains.jpg) 
|:---:|:---:|
| Original Image | Segmented by Boundaries |

[Back To The Top](#read-me-template)

---

## References
> [About Osteosacroma](https://www.cancer.org/cancer/osteosarcoma/about.html)
 
> [MBoC](https://www.molbiolcell.org/doi/10.1091/mbc.E18-08-0545)

[Back To The Top](#read-me-template)

---

## License

MIT License

Copyright (c) [2017] [James Q Quick]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

- Linkedin - [Rohan Sirohia](https://www.linkedin.com/in/rohan-sirohia)
- Twitter - [@sirohia_rohan](https://twitter.com/sirohia_rohan)

[Back To The Top](#read-me-template)
