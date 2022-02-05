import os
from pycompss.api.task import task
from pycompss.api.container import container
from pycompss.api.parameter import COLLECTION_IN
from pycompss.api.parameter import FILE_IN
from pycompss.api.parameter import DIRECTORY_OUT

PRINT_DRUG_RESULTS_CONTAINER = "/home/javier/github/projects/PerMedCoE/UC2Workflow/resources/images/printResults.sif"


def parse_arguments():
    """
    Parse the given arguments
    """
    import argparse
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
    return args


def merge_reduce(f, data):
    """ Apply function cumulatively to the items of data,
    from left to right in binary tree structure, so as to
    reduce the data to a single value.

    :param f: function to apply to reduce data
    :param data: List of items to be reduced
    :return: result of reduce the data to a single value
    """
    from collections import deque
    q = deque(range(len(data)))
    while len(q):
        x = q.popleft()
        if len(q):
            y = q.popleft()
            data[x] = f(data[x], data[y])
            q.append(x)
        else:
            return data[x]

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(returns=1)
def merge_mutants(mutant_a, mutant_b):
    return mutant_a.union(mutant_b)

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(returns=1)
def merge_targets(target_a, target_b):
    return target_a.union(target_b)

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(result_path=FILE_IN, returns=1)
def read_result_file(result_path):
    import json
    with open(result_path, 'r') as result_file:
        result = json.load(result_file)
    return result

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(returns=2)
def get_mutant_target(result):
    mutant = set(list(result.keys()))
    target = set(list(list(result.values())[0].keys()))
    return mutant, target

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(returns=1, results=COLLECTION_IN)
def create_dfs(mutants, targets, cell_lines, results):
    import numpy, pandas
    dfs = {}
    for target in targets:
        dfs.update({
            target: pandas.DataFrame(
                numpy.zeros((len(list(mutants)),
                             len(list(cell_lines)))),
                list(mutants),
                list(cell_lines)
            )
        })
    position = 0
    for result in results:
        for mutant, mutant_val in result.items():
            for gene, gene_val in mutant_val.items():
                dfs[gene].loc[mutant, cell_lines[position]] = gene_val
        position += 1
    return dfs

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(report_folder=DIRECTORY_OUT)
def print_results(dfs, report_folder):
    import seaborn
    import matplotlib.pyplot as plt

    # Create report folder if not exists
    if not os.path.exists(report_folder):
        os.makedirs(report_folder, exist_ok=True)

    for target, df in dfs.items():
        plt.figure(figsize=(10,5),dpi=100)
        ax = plt.axes()
        seaborn.heatmap(df, ax = ax, annot=True)

        ax.set_title(target)
        plt.subplots_adjust(left=0.3)
        plt.savefig(os.path.join(report_folder, (target + ".png")))


def main():
    print("Final result analysis")

    args = parse_arguments()
    cell_lines = os.listdir(args.result_folder)

    print("Cell lines: " + str(cell_lines))

    results = []
    mutants = []
    targets = []
    for cell_line in cell_lines:
        result_path = os.path.join(args.result_folder, cell_line, "sensitivity.json")
        result = read_result_file(result_path)
        results.append(result)  # avoid reading twice
        mutant, target = get_mutant_target(result)
        mutants.append(mutant)
        targets.append(target)
    merged_mutants = merge_reduce(merge_mutants, mutants)
    merged_targets = merge_reduce(merge_targets, targets)

    print("mutants: " + str(merged_mutants))
    print("targets: " + str(merged_targets))

    dfs = create_dfs(merged_mutants, merged_targets, cell_lines, results)

    print_results(dfs, args.report_folder)


if __name__=="__main__":
    main()
