import split_folders
import argparse

def split_images(input_directory, output_directory,type,value):
    if(type == "ratio"):
        # Split with a ratio.
        # To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
        split_folders.ratio(input_directory, output_directory, seed=1337, ratio=value) # default values
    elif(type == "fixed"):
        # Split val/test with a fixed number of items e.g. 100 for each set.
        # To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
        split_folders.fixed(input_directory, output_directory, seed=1337, fixed=value, oversample=False) # default values
    else:
        print("Invalid input")
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="split_data")  #add description and then 2 arguments 
    parser.add_argument('-id', '--input_directory', type=str, required=True, help='Original directory')
    parser.add_argument('-od', '--output_directory', type=str, required=True, help='Output directory')
    parser.add_argument('-t', '--type', type=str, required=True, help='either ratio or fixed')
    parser.add_argument('-v', '--value_of_split', type=int, nargs=2, required=True, metavar=('train', 'validation'), help='Image size')
    args = parser.parse_args()  #parse the arguments
    split_images(args.input_directory, args.output_directory,args.type,args.value_of_split)