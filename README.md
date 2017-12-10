# photo-organiser
When importing photos from a digital camera, often they are dumped into a single directory.

This is a small python project to assist my learning of the language, which will aim to:
* Find photo files in a specified directory
* Read Exif data to determine date taken
* Organise the photos into directories like so:
  * Option 1: `YYYY-MM-DD/`
  * Option 2: `YYYY/MM/DD/`
* (Undecided) allow an option that converts between one directory structure and another? In case the user changes their mind

## Example

```
user@host ~ $ python photo-organiser.py ~/Pictures

Scanning: /home/user/Pictures

 /home/user/Pictures
 └── DSC_0144.JPG
 |   └── Year:  2017
 |   └── Month:   11
 |   └── Day      11
 └── DSC_0128.JPG
 |   └── Year:  2017
 |   └── Month:   11
 |   └── Day      11
 └── DSC_0272.JPG
 |   └── Year:  2017
 |   └── Month:   12
 |   └── Day       7

[...]
```
