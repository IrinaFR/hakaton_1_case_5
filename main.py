import csv
import argparse

def normalize(in_file:str):
    file_open = open
    with file_open(in_file, "r", encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';', quotechar="'", doublequote=True)
        for row in reader:
            proc_string = row["address"] 
            proc_string = proc_string.replace('"','').replace("("," (")
            print(proc_string)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bad_csv", help="BAD file input")
    parser.add_argument("out_csv", help="Processed file")
    args = parser.parse_args()
    print("First step. Clear string ...") 
    normalize(args.bad_csv)
    

