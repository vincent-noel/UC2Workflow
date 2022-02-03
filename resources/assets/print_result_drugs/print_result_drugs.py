import sys, argparse, os, json

print("Final result analysis")

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("result_folder", type=str,
                    help="Input list of genes (.csv)")
                    

parser.add_argument("report_folder", type=str, 
                    help="File with list of druggable nodes")

args = parser.parse_args()
args.result_folder = os.path.realpath(args.result_folder)
args.report_folder = os.path.realpath(args.report_folder)

print("Results folder : " + args.result_folder)
print("Report folder : " + args.report_folder)