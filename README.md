# plistsubtractor
Read a plist file, write out any embedded plist files.

## Output Files
Embedded plist files are written with the same filename up to the ```.plist``` filename extension, adding the key name representing the embedded plist data at the end of the filename (e.g. the embedded plist data in the key ```dndEffectiveOverrides``` in the ```com.apple.nano.plist``` file will produce a new file called ```com.apple.nano-dndEffectiveOverrides.plist```.  If the filename already exists, a sequential identifier is added to the filename (```-1```, ```-2```, ```-3```, etc.)  Output files are written in the current working directory when the plistsubtractor script is run.

## Examples

```
$ ls com.apple.nano.plist
com.apple.nano.plist
$ plistsubtractor.py com.apple.nano.plist
Writing com.apple.nano-dndEffectiveOverrides.plist
$ ls -l com.apple.nano*
-rw-r--r--  1 jwright  staff   764 Dec 26 19:35 com.apple.nano-dndEffectiveOverrides.plist
-rw-r--r--  1 jwright  staff  1046 Dec 26 16:21 com.apple.nano.plist
```

You can specify multiple filenames in one command:

```
$ ls
com.apple.Accessibility.plist       com.apple.NanoMail.plist            com.apple.companionappd.plist       com.apple.nano.plist
com.apple.Carousel.plist            com.apple.NanoMusicSync.plist       com.apple.healthd.plist             com.apple.nanopassbook.plist
com.apple.ET.plist                  com.apple.ToneLibrary.plist         com.apple.mobilecal.plist           com.apple.nanosystemsettings.plist
com.apple.MobileSMS.plist           com.apple.bulletinboard.apps.plist  com.apple.mobilephone.plist         com.apple.stockholm.plist
$ plistsubtractor.py *.plist
Writing com.apple.Carousel-IconPositions.plist
Writing com.apple.NanoMail-NanoMailIncludeMail.plist
Writing com.apple.mobilephone-kVoicemailForReplicationKey.plist
Writing com.apple.nano-dndEffectiveOverrides.plist
```

Combined with find, whee!

```
$ find ~/Library/ -type f -name \*.plist -print0 | xargs -0 plistsubtractor.py
Writing Saved Status-Saved Status Array.plist
Writing Info-iBooks Data 2.plist
Writing Info-iBooks Data 2-1.plist
Writing Info-iBooks Data 2-1-2.plist
Writing Info-iBooks Data 2-1-2-3.plist
Writing Info-iBooks Data 2-1-2-3-4.plist
Writing Info-iBooks Data 2-1-2-3-4-5.plist
Writing Info-iBooks Data 2-1-2-3-4-5-6.plist
Writing Info-iBooks Data 2-1-2-3-4-5-6-7.plist
Writing Saved Status-Saved Status Array-1.plist
Writing com.apple.commerce.knownclients-com.apple.appstore:453.plist
Writing com.apple.commerce.knownclients-com.apple.appstore:376.plist
Writing com.apple.commerce.knownclients-com.apple.appstore:459.plist
Writing com.apple.commerce.knownclients-com.apple.ibooks:453.plist
Writing com.apple.commerce.knownclients-com.apple.ibooks:376.plist
Writing Info-FFSegmentStoreStoredFrameIndexes.plist
```

## Questions?

Joshua Wright
@joswr1ght
jwright@hasborg.com
