import csv
import argparse

def normalize(in_file:str, out_file:str):
    with open(in_file, "r", encoding='utf-8') as fi, open(out_file, "w", encoding='utf-8', newline='') as fo:
        reader = csv.DictReader(fi, delimiter=';', quotechar="'", doublequote=True)
        headers = ['id', 'address']
        writer = csv.DictWriter(fo, fieldnames=headers, delimiter=';')
        writer.writeheader()
        for row in reader:
           proc_string = row["address"]
           id_string = row['id'] 
           proc_string = proc_string.replace('"','').replace("("," (")
           print(proc_string)
           writer.writerow({'id' : id_string, 'address' : proc_string})



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bad_csv", help="BAD file input")
    parser.add_argument("out_csv", help="Processed file")
    args = parser.parse_args()
    print("First step. Clear string ...") 
    normalize(args.bad_csv, args.out_csv)