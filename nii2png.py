#!/usr/bin/env python

import scipy, numpy, shutil, os, nibabel
import scipy.misc
import sys, getopt

import imageio


def main(argv):
    inputdirectory = ''
    outputdirectory = ''
    image_array = None
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('nii2png.py -i <inputdirectory> -o <outputdirectory>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('nii2png.py -i <inputdirectory> -o <outputdirectory>')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputdirectory = arg
        elif opt in ("-o", "--output"):
            outputdirectory = arg

    print('Input folder is ', inputdirectory)
    print('Output folder is ', outputdirectory)

    # set fn as your 4d nifti file
    for inputfile in os.listdir(inputdirectory):
        if inputfile != ".DS_Store":
            image_array = nibabel.load(inputfile).get_fdata()

            if len(image_array.shape) == 3:
                    # set 4d array dimension values
                    nx, ny, nz = image_array.shape

                    print('Reading NIfTI file...')

                    total_slices = image_array.shape[2]

                    slice_counter = 0
                    # iterate through slices
                    for current_slice in range(0, total_slices):
                        # alternate slices
                        if (slice_counter % 1) == 0:

                            data = image_array[:, :, current_slice]

                            # alternate slices and save as png
                            if (slice_counter % 1) == 0:
                                image_name = str(current_slice+1) + ".png"
                                imageio.imwrite(image_name, data)

                                # output save path - you may want to modify this
                                out_name = outputdirectory  + inputfile[:-4] + '/'

                                if not os.path.exists(outputdirectory):
                                    os.makedirs(outputdirectory)

                                if not os.path.exists(out_name):
                                    os.makedirs(out_name)

                                src = image_name
                                shutil.move(src, out_name)
                                slice_counter += 1

                    print('Finished converting images')
            else:
                print('Not a 3D image. Please try again.')

# call the function to start the program
if __name__ == "__main__":
   main(sys.argv[1:])
