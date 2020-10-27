# NIfTI Image Converter (nii2png) for Python
Neuroimaging `.nii` to `.png` converter for AI projects based on Alexander Adam Laurence's version. 
The code has been modified to work on directory subfiles and only supports Python3 3D files `.nii` files. Rotation functionalities have also been excluded for speed. 

You may want to change how the files are saved based on your specificaitons. Should be between lines 53 and 68 in `nii2png.py`. 

## Environment
Python 3.7 

```
nii2png.py
```

1. Select your working directory.
2. Specify output directory - will create if not there. 
3. Let it run.
4. Your png files are now in the specified output folder.

## Python Usage

1. Let's run the file and start converting images! Please ensure that your output folder ends with a slash to avoid errors.

```
$ python3 nii2png.py -i <inputfolder> -o <outputfolder>
```

or

```
$ python3 nii2png.py --input <inputfolder> --ouput <outputfolder>
```

## Example

```
python3 /Volumes/DS_Projects/nifti_to_png/nii2png.py -i /Volumes/DS_Projects/archive/uncompressed_stacks/ -o /Volumes/DS_Projects/archive/image_stacks/
```
## Permissions

You may need to make the file executable by running the command below. 

```
$ chmod +x nii2png.py
```

Optional: You can also move `nii2png.py` into your bin directory, and it will be runnable from anywhere.

<p align="left">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.7|%203.8-brightgreen.svg" alt="Python supported"></a>
</p>

