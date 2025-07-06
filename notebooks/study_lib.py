from tempfile import TemporaryDirectory
from pathlib import Path
import subprocess
import shutil
import copy
from collections import defaultdict

import numpy as np
import tomlkit
import awkward as ak
import pandas as pd
from IPython.display import display

MODULE_PATH = Path(__file__).parent
VOTING = MODULE_PATH / "voting"


def do_run(config, trials) -> ak.Array:
    with TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)
        config_file = temp_dir / "config.toml"
        with open(config_file, "w") as fout:
            tomlkit.dump(config, fout)
        pq_file = temp_dir / "results.parquet"
        cp = subprocess.run(
            [
                VOTING,
                "-c",
                config_file,
                "-o",
                pq_file,
                "-t",
                str(trials),
            ],
            check=False,
            capture_output=True,
        )
        last_config_file = "/tmp/voting_last_config.toml"
        shutil.copyfile(config_file, last_config_file)
        if cp.returncode != 0:
            print(cp.stderr)
            raise ValueError(f"voting process failed -- see perhaps {last_config_file}")
        results = ak.from_parquet(pq_file)
    return results


def config_series(base_config, parameter, pvalues):
    """
    Generates a sequence of configs based on the base config, with a dotted parameter
    taking on a given sequence of values.
    Returns a generator that yields tuples of (param_name, value, config)
    """
    config = copy.deepcopy(base_config)
    parameters = [int(p) if p.isnumeric() else p for p in parameter.split(".")]
    last_parameter = parameters.pop()
    for val in pvalues:
        conf_item = config
        for p in parameters:  # drill down into config
            conf_item = conf_item[p]
        assert last_parameter in conf_item, f"No such parameter {last_parameter}"
        conf_item[last_parameter] = val
        param_name = parameters[-1] if parameters else last_parameter
        yield (param_name, val, config)


def run_experiment(config_seq, trials=2000, pi=False, sm=False, with_results=False):
    """
    pi: show percent elections that are non-ideal
    sm: Show smith set stats: avg_nsmith is average number of candidates in the Smith set (1 if no cycle)
    {method}_insm: *percent* of time this method's winner is in the Smith set
    """
    iexp = 0
    table_data = defaultdict(list)
    for config_tuple in config_seq:
        if isinstance(config_tuple, tuple):
            (pname, pval, config) = config_tuple
        else:
            (pname, pval, config) = ("config_num", iexp, config_tuple)
        iexp += 1  # Only for the case that config_seq is a list of configs.

        results = do_run(config, trials)
        table_data[pname].append(pval)
        if sm:
            table_data["avg_nsmith"].append(ak.mean(results.num_smith))
        results_list = []
        for f in results.methods.fields:
            mean_regret = ak.mean(results.methods[f].regret)
            table_data[f"{f}_mR"].append(mean_regret)
            if pi:
                percent_ideal = (
                    ak.count(results.methods[f].regret[results.methods[f].regret == 0])
                    / trials
                    * 100.0
                )
                table_data[f"{f}_pi"].append(percent_ideal)
            if sm:
                in_smith = results.in_smith[
                    np.arange(len(results)), results.methods[f].winner
                ]
                table_data[f"{f}_insm"].append(
                    np.count_nonzero(in_smith) / len(in_smith) * 100
                )
            if with_results:
                results_list.append(results)
    # print(repr(table_data))
    df = pd.DataFrame(table_data)
    if results_list:
        df.attrs["results"] = results_list
    return df


def run_experiment_smith(config_seq, trials=2000):
    iexp = 0
    table_data = defaultdict(list)
    for config_tuple in config_seq:
        if isinstance(config_tuple, tuple):
            (pname, pval, config) = config_tuple
        else:
            (pname, pval, config) = ("config_num", iexp, config_tuple)
        iexp += 1  # Only for the case that config_seq is a list of configs.

        results = do_run(config, trials)
        fields = get_fields(results)
        table_data[pname].append(pval)
        table_data["avg_nsmith"].append(ak.mean(results.num_smith))
        for f in fields:
            mean_regret = ak.mean(results[f]["regret"])
            table_data[f"{f[2:]}_mR"].append(mean_regret)
            num_in_smith = 0
            for ins, winner in zip(results.in_smith, results[f].winner):
                if ins[winner]:
                    num_in_smith += 1
            table_data[f"{f[2:]}_in_smth"].append(num_in_smith / len(results))

    # print(repr(table_data))
    return pd.DataFrame(table_data)
