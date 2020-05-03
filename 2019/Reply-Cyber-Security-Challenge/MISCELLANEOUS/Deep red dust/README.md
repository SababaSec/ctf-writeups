# Deep red dust

## Problem

> Armstrong, the Astronaut-in-Chief has sent an email saying he's leaving the Mars mission. This is very odd, especially as Armstrong has spent decades working on the project. His email contains an attachment in an unknown format. What is it? R-boy must dig deeper to find out what's going on – help him investigate.

[Deep_Red_Dust](Deep_Red_Dust)

## Solution

We are given a file called `Deep_Red_Rust` which seems to be a ZIP archive:

```bash
$ file Deep_Red_Dust
Deep_Red_Dust: Zip archive data, �T�!A+BL��~b�n5�F�5�3�-D_�f��:Wa�|U�><Y�����������U8Q��
```

However, looking at the hexdump, we see the following:

```
00000000: 5242 4f59 0d0a 1a0a 0000 000d 4948 4452  RBOY........IHDR
00000010: 0000 0400 0000 02eb 0806 0000 0060 4ef5  .............`N.
00000020: f800 0000 0473 4249 5408 0808 087c 0864  .....sBIT....|.d
00000030: 8800 0000 1974 4558 7453 6f66 7477 6172  .....tEXtSoftwar
00000040: 6500 676e 6f6d 652d 7363 7265 656e 7368  e.gnome-screensh
00000050: 6f74 ef03 bf3e 0000 2000 4944 4154 789c  ot...>.. .IDATx.
```

The first 4 bytes are set to `RBOY`, which is a non-standard header. But the string `IHDR` seems to indicate a PNG image.

We used `hexedit` to replace the first 4 bytes with `89 50 4E 47`, which are the PNG magic bytes.

We get the following image, which contains the text `K33pItS3cr3t` written in the sand:

![Image with K33pItS3cr3t written in the sand](Deep_Red_Dust.png)

The ZIP file detected by the `file` command is embedded in the image and we can extract it using `binwalk` with the `-e` flag. The ZIP file was password-protected and the password was, of course, `K33pItS3cr3t`.

On extracting the ZIP file, we are left with a file called `Goodbye.docm`. The `.docm` extension is used for MS Word documents with macros enabled.

Using [oletools](https://github.com/decalage2/oletools) to extract the macro VBA code, we get the following:

```
$ olevba Goodbye.docm 
olevba 0.54.2 on Python 2.7.16 - http://decalage.info/python/oletools
===============================================================================
FILE: Goodbye.docm
Type: OpenXML
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file: word/vbaProject.bin - OLE stream: u'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Private Sub CommandButton1_Click()
If Not (TextBox1.TextLength = 0) Then
Dim tbox As String
tbox = TextBox1.Text
Dim encrypt As Variant
encrypt = Array(52, 54, 60, 40, 72, 64, 42, 35, 93, 26, 38, 110, 3, 47, 56, 26, 64, 1, 49, 33, 71, 38, 7, 25, 20, 92, 1, 9)
Dim inputChar() As Byte
inputChar = StrConv(tbox, vbFromUnicode)
Dim plaintext(28) As Variant
Dim i As Integer
For i = 0 To 27
plaintext(i) = inputChar(i Mod TextBox1.TextLength) Xor encrypt(i)
Next
MsgBox "Congrats!!"
End If
End Sub
```

We can deduce that the macro takes an input from a text box and uses it to XOR the encrypted flag. Since we know the flag format, we can use this knowledge to obtain the first five letters from the key.

Using Python,

```py
>>> import sys
>>> encrypted = [52, 54, 60, 40, 72]
>>> flag_format = '{FLG:'
>>> for i, j in zip(encrypted, flag_format):
...   print(chr(i ^ ord(j)))
... 
Oppor
```

The first 5 characters of the key are `'Oppur'`. Judging by the Mars-themed challenge, we suspected that the key might be `'Opportunity'`. Luckily for us, this was correct:

```py
>>> encrypted = [52, 54, 60, 40, 72, 64, 42, 35, 93, 26, 38, 110, 3, 47, 56, 26, 64, 1, 49, 33, 71, 38, 7, 25, 20, 92, 1, 9]
>>> key = "Opportunity"
>>> 
>>> for i in range(len(encrypted)):
...   print(chr(encrypted[i] ^ ord(key[i % len(key)])))
... 
{FLG:4_M4n_!s_Wh4t_H3_Hid3s}
```
